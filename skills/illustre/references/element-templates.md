# Templates d'Elements Excalidraw

Templates JSON copier-coller pour construire des diagrammes. Remplacer les valeurs entre `[BRACKETS]`.

---

## Texte Libre (Sans Container)

```json
{
  "type": "text",
  "id": "[UNIQUE_ID]",
  "x": [X],
  "y": [Y],
  "width": [WIDTH],
  "height": [HEIGHT],
  "text": "[TEXTE]",
  "fontSize": 24,
  "fontFamily": 5,
  "textAlign": "center",
  "verticalAlign": "middle",
  "strokeColor": "#0F172A",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "roughness": 0,
  "opacity": 100,
  "seed": [RANDOM_INT],
  "version": 1,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": null,
  "link": null
}
```

---

## Rectangle (Container)

```json
{
  "type": "rectangle",
  "id": "[UNIQUE_ID]",
  "x": [X],
  "y": [Y],
  "width": [WIDTH],
  "height": [HEIGHT],
  "strokeColor": "[STROKE_COLOR]",
  "backgroundColor": "[FILL_COLOR]",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 0,
  "opacity": 100,
  "seed": [RANDOM_INT],
  "version": 1,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": [
    {"type": "text", "id": "[TEXT_ID]"},
    {"type": "arrow", "id": "[ARROW_ID]"}
  ],
  "link": null,
  "roundness": {"type": 3}
}
```

---

## Texte Centre dans un Shape

```json
{
  "type": "text",
  "id": "[TEXT_ID]",
  "x": [X],
  "y": [Y],
  "width": [WIDTH],
  "height": [HEIGHT],
  "text": "[TEXTE]",
  "fontSize": 24,
  "fontFamily": 5,
  "textAlign": "center",
  "verticalAlign": "middle",
  "strokeColor": "[TEXT_COLOR]",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "roughness": 0,
  "opacity": 100,
  "seed": [RANDOM_INT],
  "version": 1,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": null,
  "containerId": "[PARENT_SHAPE_ID]",
  "link": null
}
```

---

## Ellipse

```json
{
  "type": "ellipse",
  "id": "[UNIQUE_ID]",
  "x": [X],
  "y": [Y],
  "width": [WIDTH],
  "height": [HEIGHT],
  "strokeColor": "[STROKE_COLOR]",
  "backgroundColor": "[FILL_COLOR]",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 0,
  "opacity": 100,
  "seed": [RANDOM_INT],
  "version": 1,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": [],
  "link": null
}
```

---

## Petit Marqueur Dot

```json
{
  "type": "ellipse",
  "id": "[UNIQUE_ID]",
  "x": [X],
  "y": [Y],
  "width": 16,
  "height": 16,
  "strokeColor": "#0047CC",
  "backgroundColor": "#0061FF",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "roughness": 0,
  "opacity": 100,
  "seed": [RANDOM_INT],
  "version": 1,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": [],
  "link": null
}
```

---

## Diamant (Decision)

```json
{
  "type": "diamond",
  "id": "[UNIQUE_ID]",
  "x": [X],
  "y": [Y],
  "width": [WIDTH],
  "height": [HEIGHT],
  "strokeColor": "#B45309",
  "backgroundColor": "#FEF3C7",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 0,
  "opacity": 100,
  "seed": [RANDOM_INT],
  "version": 1,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": [],
  "link": null
}
```

---

## Fleche

```json
{
  "type": "arrow",
  "id": "[UNIQUE_ID]",
  "x": [START_X],
  "y": [START_Y],
  "width": [WIDTH],
  "height": [HEIGHT],
  "points": [[0, 0], [[END_X_OFFSET], [END_Y_OFFSET]]],
  "strokeColor": "[STROKE_COLOR]",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 0,
  "opacity": 100,
  "seed": [RANDOM_INT],
  "version": 1,
  "isDeleted": false,
  "groupIds": [],
  "startBinding": {
    "elementId": "[SOURCE_ELEMENT_ID]",
    "focus": 0,
    "gap": 8
  },
  "endBinding": {
    "elementId": "[TARGET_ELEMENT_ID]",
    "focus": 0,
    "gap": 8
  },
  "startArrowhead": null,
  "endArrowhead": "arrow",
  "link": null
}
```

Pour une fleche courbee, ajouter un point intermediaire :
```json
"points": [[0, 0], [[MID_X], [MID_Y]], [[END_X], [END_Y]]]
```

---

## Ligne (Non-Fleche)

```json
{
  "type": "line",
  "id": "[UNIQUE_ID]",
  "x": [START_X],
  "y": [START_Y],
  "width": [WIDTH],
  "height": [HEIGHT],
  "points": [[0, 0], [[END_X_OFFSET], [END_Y_OFFSET]]],
  "strokeColor": "#334155",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 0,
  "opacity": 100,
  "seed": [RANDOM_INT],
  "version": 1,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": null,
  "link": null
}
```

---

## Separateur Pointille (entre slides)

```json
{
  "type": "line",
  "id": "[UNIQUE_ID]",
  "x": 0,
  "y": [Y_MILIEU_DU_GAP],
  "width": 1920,
  "height": 0,
  "points": [[0, 0], [1920, 0]],
  "strokeColor": "#CCCCCC",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "strokeStyle": "dotted",
  "roughness": 0,
  "opacity": 100,
  "seed": [RANDOM_INT],
  "version": 1,
  "isDeleted": false,
  "groupIds": [],
  "boundElements": null,
  "link": null
}
```

---

## Document Excalidraw Complet (Enveloppe)

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "excalidraw-skill",
  "elements": [
    // Ajouter les elements ici
  ],
  "appState": {
    "viewBackgroundColor": "#ffffff",
    "gridSize": null
  },
  "files": {}
}
```

---

## Tailles de Reference

| Element | Largeur | Hauteur | Usage |
|---------|---------|---------|-------|
| Hero | 300px | 150px | Element principal |
| Primaire | 180px | 90px | Elements cles |
| Secondaire | 120px | 60px | Elements support |
| Petit | 60px | 40px | Marqueurs, labels |
| Dot | 16px | 16px | Points de repere |

---

## Note sur fontFamily

**Toujours utiliser `fontFamily: 5`** (Excalifont, la police par defaut d'Excalidraw, handwritten-style).

**JAMAIS `fontFamily: 3`** (Cascadia monospace). Le renderer embarque Excalifont localement et l'injecte comme `@font-face` base64 dans le SVG pour que le rendu PNG corresponde exactement a ce que l'utilisateur voit dans Excalidraw.
