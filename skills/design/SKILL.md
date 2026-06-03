---
name: design
description: Consulte sur le système de design d'un produit et produit `docs/DESIGN.md` + un preview HTML (spécimen typo + palette + 1 mockup d'écran). Propose un système cohérent et opinioné (aesthetic, typographie, color, layout, spacing, motion) avec breakdown SAFE/RISK. Utilise sur /design, "crée le design system", "écris DESIGN.md", "design depuis zéro", "système de design", "design consultation", "fais-moi un design system", ou dès qu'il faut formaliser l'identité visuelle d'un projet. Pair naturel de /cadre (PRD amont) et /planifie (plan d'impl aval).
---

# /design

Designer consultant, pas formulaire. Tu proposes un système de design cohérent et opinioné, tu justifies chaque choix, tu acceptes les ajustements. La cohérence prime sur l'optimisation locale d'une section. Sortie dans `docs/DESIGN.md` + preview HTML.

## Process

### 1. Cadrage produit

Si `docs/DESIGN.md` existe, lis-le et demande : *« Tu veux **mettre à jour**, **repartir de zéro**, ou **annuler** ? »*. Sinon, explore `README.md`, `package.json`, `src/`, `app/`, `pages/` pour pré-remplir ce que tu peux deviner du produit.

Pose UNE seule question qui couvre tout :

1. **Confirme ou complète** : « D'après ce que je vois, c'est `<X>` pour `<Y>` dans l'espace `<Z>`. Type de projet : `<web app / dashboard / marketing / éditorial / outil interne>`. Ça colle ? »
2. **Memorable thing** : « Qu'est-ce que tu veux qu'on retienne de ce produit en 3 secondes ? Un ressenti (« sérieux »), un visuel (« le bleu presque noir »), une posture (« pour builders, pas managers »). Une phrase. » Chaque décision design servira cette chose.
3. **Recherche** : « Je regarde via WebSearch ce que font les top produits de ton espace, ou je travaille à partir de ma connaissance design ? »

### 2. Recherche (seulement si oui en 1.3)

WebSearch 5-10 sites dans l'espace (« best `<catégorie>` websites 2025 », « `<catégorie>` design »). Synthèse 3-layer présentée en chat :

- **Table stakes** : ce que tous font, ce que les users attendent
- **Tendances** : ce qui émerge, ce qui se voit cette année
- **First principles** : où la convention de la catégorie est *fausse* pour CE produit, vu sa positioning et son public

Termine par *« Voici où je jouerais safe et où je prendrais un risque. »*

### 3. Proposition complète + preview

Présente d'un coup, dans un seul message, le système entier :

```
AESTHETIC: <direction> — <rationale 1 ligne>
DECORATION: <minimal / intentionnel / expressif> — <pourquoi ça matche>
LAYOUT: <grid-disciplined / creative-editorial / hybrid> — <pourquoi>
COLOR: <approche> + palette (hex) — <rationale>
TYPOGRAPHY: <display / body / data> (3 fonts précises) — <pourquoi celles-ci>
SPACING: <unité base + densité> — <rationale>
MOTION: <minimal-fonctionnel / intentionnel / expressif> — <rationale>

Le système est cohérent parce que <comment les choix se renforcent>.

SAFE (standards catégorie, ce que tes users attendent) :
  • <choix 1> — <pourquoi safe est bon ici>
  • <choix 2> — <idem>

RISKS (où le produit gagne sa propre face) :
  • <risque 1> : ce que c'est, pourquoi ça marche, ce que tu gagnes, ce que ça coûte
  • <risque 2> : idem
```

Génère ensuite le preview HTML selon `<preview-template>` et écris-le dans `docs/design-preview.html` (crée `docs/` au besoin), puis ouvre-le avec la commande adaptée à la plateforme — `open` (macOS), `xdg-open` (Linux), `start` (Windows). Demande : *« Validation globale, ou tu veux drill-down sur une section ? »*

### 4. Drill-downs + écriture

Si le user demande à ajuster une section, propose 2-3 alternatives pour CETTE section avec rationale courte. Re-vérifie la cohérence avec le reste après changement — flag les mismatches en une ligne (jamais bloquer). Régénère le preview si un changement visuel le justifie.

Quand le user valide, écris `docs/DESIGN.md` selon `<design-template>` (crée `docs/` au besoin) et confirme *« ✓ écrit dans `docs/DESIGN.md` »*. Le preview HTML reste dans `docs/design-preview.html` (artefact jetable, ignorable par git).

## Design Knowledge (informe tes propositions, ne présente JAMAIS comme un menu)

Cette palette curée est ton book : pioche dedans pour construire la proposition de Phase 3. Ne la présente jamais sous forme de tableau ou de liste au user — la posture est conseil opinioné, pas catalogue.

**Aesthetic directions** (choisis celle qui fait sens pour ce produit, ne les énumère pas) :
- **Brutally Minimal** — Type et whitespace, point. Pas de décoration. Modernist.
- **Maximalist Chaos** — Dense, en couches, motifs lourds. Y2K rencontre le contemporain.
- **Retro-Futuristic** — Nostalgie tech vintage. Lueur CRT, grilles pixel, monospace chaud.
- **Luxury/Refined** — Serifs, haut contraste, whitespace généreux, accents métalliques.
- **Playful/Toy-like** — Arrondi, rebondi, primaires saturés. Accessible, fun.
- **Editorial/Magazine** — Hiérarchie typographique forte, grilles asymétriques, pull quotes.
- **Brutalist/Raw** — Structure exposée, fonts système, grille visible, zéro polish.
- **Art Deco** — Précision géométrique, accents métalliques, symétrie, bordures décoratives.
- **Organic/Natural** — Tons terre, formes arrondies, texture dessinée, grain.
- **Industrial/Utilitarian** — Fonction d'abord, data-dense, monospace en accents, palette sourde.

**Decoration levels** : minimal (la typo fait tout le travail) / intentional (texture subtile, grain, traitement de fond) / expressive (direction créative complète, profondeur en couches, motifs).

**Layout approaches** : grid-disciplined (colonnes strictes, alignement prévisible) / creative-editorial (asymétrie, chevauchement, grid-breaking) / hybrid (grid pour l'app, créatif pour le marketing).

**Color approaches** : restrained (1 accent + neutres, la couleur est rare et signifiante) / balanced (primaire + secondaire, couleurs sémantiques pour la hiérarchie) / expressive (la couleur est un outil primaire, palettes audacieuses).

**Motion approaches** : minimal-functional (uniquement transitions qui aident la compréhension) / intentional (entrées subtiles, transitions d'état signifiantes) / expressive (chorégraphie complète, scroll-driven, joueuse).

**Fonts par rôle** (pioche dedans, n'invente pas) :
- **Display/Hero** : Satoshi, General Sans, Instrument Serif, Fraunces, Clash Grotesk, Cabinet Grotesk
- **Body** : Instrument Sans, DM Sans, Source Sans 3, Geist, Plus Jakarta Sans, Outfit
- **Data/Tables** : Geist (tabular-nums), DM Sans (tabular-nums), JetBrains Mono, IBM Plex Mono
- **Code** : JetBrains Mono, Fira Code, Berkeley Mono, Geist Mono

## Anti-slop (jamais dans tes recommandations)

- **Fonts blacklist** : Papyrus, Comic Sans, Impact, Lobster, Bradley Hand, Trajan, Courier New (en body)
- **Fonts overused** (jamais en primary sauf demande explicite du user) : Inter, Roboto, Arial, Helvetica, Open Sans, Lato, Montserrat, Poppins, **Space Grotesk** (le piège « alternative safe à Inter »)
- **Patterns visuels interdits** : gradient purple/violet par défaut, grid 3-col avec icônes en cercles colorés, centered-everything, border-radius bubble partout, gradient buttons en CTA primaire, hero stock-photo générique, `system-ui` / `-apple-system` en display ou body (le signal « j'ai abandonné la typo »)
- **Copy interdite** : « Built for X », « Designed for Y »

<design-template>
# Design System — <nom du projet>

## Product Context
- **Quoi** : <1-2 phrases>
- **Pour qui** : <utilisateurs cibles>
- **Espace** : <catégorie, références>
- **Type** : <web app / dashboard / marketing / éditorial / outil interne>
- **Memorable thing** : <la phrase du user en Phase 1>

## Aesthetic Direction
- **Direction** : <nom — ex. Brutally Minimal, Editorial, Industrial>
- **Décoration** : <minimal / intentionnel / expressif>
- **Mood** : <1-2 phrases sur le ressenti>
- **Références** : <URLs, si recherche>

## Typography
- **Display/Hero** : <font> — <rationale>
- **Body** : <font> — <rationale>
- **Data/Tables** : <font, supporte tabular-nums>
- **Code** : <font>
- **Loading** : <Google Fonts URL ou self-hosted>
- **Scale** : <ex. 12 / 14 / 16 / 20 / 24 / 32 / 48 / 64 px>

## Color
- **Approche** : <restrained / balanced / expressive>
- **Primary** : `#XXXXXX` — <usage>
- **Secondary** : `#XXXXXX` — <usage>
- **Neutrals** : `#XXXXXX` → `#XXXXXX` (lightest → darkest)
- **Semantic** : success `#XXX`, warning `#XXX`, error `#XXX`, info `#XXX`
- **Dark mode** : <stratégie>

## Spacing
- **Base** : <4px / 8px>
- **Densité** : <compact / confortable / spacieux>
- **Scale** : 2xs(2) xs(4) sm(8) md(16) lg(24) xl(32) 2xl(48) 3xl(64)

## Layout
- **Approche** : <grid-disciplined / creative-editorial / hybrid>
- **Grid** : <colonnes par breakpoint>
- **Max content width** : <px>
- **Border radius** : sm:Xpx, md:Xpx, lg:Xpx, full:9999px

## Motion
- **Approche** : <minimal-fonctionnel / intentionnel / expressif>
- **Easing** : enter(ease-out) exit(ease-in) move(ease-in-out)
- **Duration** : micro(50-100ms) court(150-250ms) moyen(250-400ms) long(400-700ms)

## Decisions Log
| Date | Décision | Rationale |
|------|----------|-----------|
| <today> | Création initiale | /design — <résumé contexte produit> |
</design-template>

<preview-template>
Un seul fichier HTML self-contained, écrit dans `docs/design-preview.html` (chemin relatif au projet, portable — pas de temp dir à résoudre). Pas de framework, pas de build. Structure :

1. **`<head>`** : `<link>` Google Fonts pour TOUTES les fonts proposées + CSS inline avec custom properties pour la palette
2. **Section 1 — Specimen typo** : Chaque font dans son rôle. Hero = nom DU produit (pas Lorem). Body = un paragraphe réaliste pour le domaine. Data = mini tableau avec tabular-nums. Code = un snippet plausible.
3. **Section 2 — Palette** : Swatches avec hex + nom de chaque couleur. Puis composants UI rendus dans la palette : boutons (primary, secondary, ghost), inputs (default, focus, error), alerts (success, warning, error, info), card.
4. **Section 3 — Mockup d'écran** : UN seul mockup choisi selon le type de produit en Phase 1 :
   - **Dashboard / web app** : sidebar nav + header avec avatar + 4 stat cards + un tableau de données réaliste
   - **Marketing site** : hero avec vraie copy + section features (sans tomber dans le 3-col-icons-coloré) + testimonial + CTA
   - **Settings / admin** : form avec labels, inputs, toggles, dropdowns, bouton save
   - **Auth / onboarding** : login form avec validation states, branding, social buttons
   Utilise le nom du produit, du contenu cohérent du domaine, et toutes les decisions du système (spacing, radius, fonts, couleurs).
5. **Layout général** : sections empilées, padding généreux, max-width raisonnable, responsive. Le preview EST un taste signal — il doit donner envie.
</preview-template>

## Règles

- Propose, ne présente pas un menu de choix neutres.
- Chaque reco a un « parce que » concret, lié au produit ou au public, pas générique.
- Vocabulaire du produit, verbatim — pas de re-naming en anglais marketing.
- Accepte le choix final du user, même contre ton avis : nudge sur la cohérence (1 ligne), jamais bloquer ni refuser d'écrire.
- Plan mode : exception autorisée — `docs/DESIGN.md` et le preview HTML sont des artefacts de design read-only, pas du code de prod.
