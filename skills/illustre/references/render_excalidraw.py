#!/usr/bin/env python3
"""Render Excalidraw JSON files to PNG via direct SVG conversion + Playwright screenshot.

This custom renderer bypasses the unreliable Excalidraw CDN approach by converting
each Excalidraw element directly to SVG, then using Playwright to screenshot the
rendered SVG at 2x scale for high-quality output.

Supported element types:
- rectangle (with roundness)
- ellipse
- diamond
- line (with dashed/dotted strokes)
- arrow (with arrowhead)
- text (multiline, with textAlign and vertical centering)

Usage:
    python3 render_excalidraw.py <file.excalidraw> [output.png]
"""
from __future__ import annotations

import base64
import html as html_mod
import json
import math
import sys
from pathlib import Path

# Excalifont is the default Excalidraw font. We embed it as base64 in the
# rendered SVG so output matches what users see inside Excalidraw itself.
_FONT_FILE = Path(__file__).parent / "Excalifont-Regular.woff2"
_FONT_FAMILY = "Excalifont, Virgil, Cascadia Code, Menlo, sans-serif"


def _font_face_css() -> str:
    """Return a @font-face CSS block with Excalifont embedded as base64.

    Returns an empty string if the font file is missing (fallback to
    system fonts in _FONT_FAMILY).
    """
    if not _FONT_FILE.exists():
        return ""
    b64 = base64.b64encode(_FONT_FILE.read_bytes()).decode("ascii")
    return (
        "@font-face{"
        "font-family:'Excalifont';"
        "font-style:normal;font-weight:400;font-display:block;"
        f"src:url(data:font/woff2;base64,{b64}) format('woff2');"
        "}"
    )


def _esc(s) -> str:
    return html_mod.escape(str(s))


def _element_to_svg(el: dict) -> str:
    """Convert a single Excalidraw element to an SVG snippet."""
    t = el.get("type")
    x = el.get("x", 0)
    y = el.get("y", 0)
    w = el.get("width", 0)
    h = el.get("height", 0)
    stroke = el.get("strokeColor", "#000000")
    bg = el.get("backgroundColor", "transparent")
    if bg == "transparent":
        bg = "none"
    sw = el.get("strokeWidth", 2)
    ss = el.get("strokeStyle", "solid")

    dash = ""
    if ss == "dashed":
        dash = f' stroke-dasharray="{sw * 4},{sw * 3}"'
    elif ss == "dotted":
        dash = f' stroke-dasharray="{sw},{sw * 2}"'

    if t == "rectangle":
        rx = 12 if el.get("roundness") else 0
        return (
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" ry="{rx}" '
            f'fill="{bg}" stroke="{stroke}" stroke-width="{sw}"{dash}/>'
        )

    if t == "ellipse":
        cx = x + w / 2
        cy = y + h / 2
        rx = w / 2
        ry = h / 2
        return (
            f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" '
            f'fill="{bg}" stroke="{stroke}" stroke-width="{sw}"{dash}/>'
        )

    if t == "diamond":
        cx = x + w / 2
        cy = y + h / 2
        pts = f"{cx},{y} {x + w},{cy} {cx},{y + h} {x},{cy}"
        return (
            f'<polygon points="{pts}" '
            f'fill="{bg}" stroke="{stroke}" stroke-width="{sw}"{dash}/>'
        )

    if t == "line":
        pts = el.get("points", [[0, 0], [w, h]])
        if len(pts) >= 2:
            poly = " ".join(f"{x + p[0]},{y + p[1]}" for p in pts)
            return (
                f'<polyline points="{poly}" '
                f'fill="none" stroke="{stroke}" stroke-width="{sw}"{dash}/>'
            )
        return ""

    if t == "arrow":
        pts = el.get("points", [[0, 0], [w, h]])
        if len(pts) < 2:
            return ""
        abs_pts = [(x + p[0], y + p[1]) for p in pts]
        poly = " ".join(f"{p[0]},{p[1]}" for p in abs_pts)
        last = abs_pts[-1]
        prev = abs_pts[-2]
        dx = last[0] - prev[0]
        dy = last[1] - prev[1]
        angle = math.atan2(dy, dx)
        arrow_len = 22
        arrow_angle = 0.5
        ax1 = last[0] - arrow_len * math.cos(angle - arrow_angle)
        ay1 = last[1] - arrow_len * math.sin(angle - arrow_angle)
        ax2 = last[0] - arrow_len * math.cos(angle + arrow_angle)
        ay2 = last[1] - arrow_len * math.sin(angle + arrow_angle)
        head = (
            f'<polygon points="{last[0]},{last[1]} {ax1},{ay1} {ax2},{ay2}" '
            f'fill="{stroke}" stroke="{stroke}" stroke-width="1"/>'
        )
        line = (
            f'<polyline points="{poly}" '
            f'fill="none" stroke="{stroke}" stroke-width="{sw}"{dash}/>'
        )
        return line + head

    if t == "text":
        text = el.get("text", "")
        fs = el.get("fontSize", 24)
        color = el.get("strokeColor", "#1A1A1A")
        align = el.get("textAlign", "left")
        anchor = {"left": "start", "center": "middle", "right": "end"}.get(align, "start")
        if anchor == "middle":
            tx = x + w / 2
        elif anchor == "end":
            tx = x + w
        else:
            tx = x
        lines = text.split("\n")
        line_height = fs * 1.25
        total_h = line_height * len(lines)
        # Start baseline (first line)
        start_y = y + (h - total_h) / 2 + fs * 0.85
        parts = []
        for i, line in enumerate(lines):
            ly = start_y + i * line_height
            parts.append(
                f'<text x="{tx}" y="{ly}" '
                f'font-family="{_FONT_FAMILY}" '
                f'font-size="{fs}" font-weight="400" '
                f'fill="{color}" text-anchor="{anchor}">{_esc(line)}</text>'
            )
        return "\n".join(parts)

    return ""


def _build_svg(data: dict) -> tuple[str, int, int]:
    """Build the complete SVG string from Excalidraw JSON data.

    Returns:
        (svg_string, width, height)
    """
    elements = [e for e in data.get("elements", []) if not e.get("isDeleted")]
    app_state = data.get("appState", {})
    bg = app_state.get("viewBackgroundColor", "#FFFFFF")

    if not elements:
        raise ValueError("No elements to render")

    min_x = min(e.get("x", 0) for e in elements)
    min_y = min(e.get("y", 0) for e in elements)
    max_x = max(e.get("x", 0) + e.get("width", 0) for e in elements)
    max_y = max(e.get("y", 0) + e.get("height", 0) for e in elements)

    pad = 80
    width = int(max(max_x - min_x + pad * 2, 1920))
    height = int(max(max_y - min_y + pad * 2, 1080))
    tx = pad - min_x
    ty = pad - min_y

    # Shapes first (so text renders on top)
    shapes = [e for e in elements if e.get("type") != "text"]
    texts = [e for e in elements if e.get("type") == "text"]

    svg_parts = [_element_to_svg(e) for e in shapes]
    svg_parts.extend(_element_to_svg(e) for e in texts)

    font_css = _font_face_css()
    style_block = f'<defs><style>{font_css}</style></defs>\n' if font_css else ""

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width}" height="{height}" viewBox="0 0 {width} {height}">\n'
        f'{style_block}'
        f'<rect width="100%" height="100%" fill="{bg}"/>\n'
        f'<g transform="translate({tx},{ty})">\n'
        + "\n".join(svg_parts)
        + "\n</g>\n</svg>"
    )
    return svg, width, height


def render(excalidraw_path: str, output_path: str | None = None) -> str:
    """Render an .excalidraw file to PNG.

    Args:
        excalidraw_path: Path to the .excalidraw JSON file
        output_path: Optional output PNG path. Defaults to same name with .png extension.

    Returns:
        Path to the generated PNG file.

    Side effects:
        Also writes a .svg file alongside the .png for vector-quality use in
        editing software (DaVinci, Final Cut, After Effects, InDesign).
    """
    from playwright.sync_api import sync_playwright

    excalidraw_file = Path(excalidraw_path).resolve()
    if not excalidraw_file.exists():
        raise FileNotFoundError(f"File not found: {excalidraw_file}")

    output_file = Path(output_path).resolve() if output_path else excalidraw_file.with_suffix(".png")
    svg_file = excalidraw_file.with_suffix(".svg")

    with open(excalidraw_file) as f:
        data = json.load(f)

    svg, w, h = _build_svg(data)
    svg_file.write_text(svg, encoding="utf-8")

    html = (
        '<!DOCTYPE html><html><head><meta charset="utf-8"/>'
        '<style>body{margin:0;padding:0;background:white;}</style>'
        f'</head><body>{svg}</body></html>'
    )

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
        page.set_content(html)
        page.wait_for_load_state("domcontentloaded")
        # Wait for @font-face (Excalifont) to be fully loaded before screenshot
        # so text is rendered with the correct typeface instead of a fallback.
        page.evaluate("document.fonts.ready")
        page.screenshot(path=str(output_file), full_page=True, omit_background=False)
        browser.close()

    print(f"Rendered SVG: {svg_file}")
    print(f"Rendered PNG: {output_file}")
    return str(output_file)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 render_excalidraw.py <file.excalidraw> [output.png]")
        sys.exit(1)

    input_path = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        result = render(input_path, out_path)
        print(f"Success: {result}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)
