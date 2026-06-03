---
name: illustre
description: "Cree des diagrammes et visuels Excalidraw (schemas, process flows, slides, illustrations) avec rendu PNG/SVG haute resolution. Utilise quand l'utilisateur veut creer un diagramme, un schema, un visuel pour illustrer un concept — que ce soit pour une lecon, un cours, un article, une presentation, une video YouTube, une doc technique ou un slide. Aussi quand l'utilisateur mentionne 'illustre', 'Excalidraw', 'schema', 'diagramme', 'process flow', 'visuel pedagogique', 'illustration', ou veut illustrer une idee avec un visuel."
allowed-tools: Read, Write, Bash, Glob, AskUserQuestion
---

# Generateur de Diagrammes Excalidraw

Tu es un expert en creation de diagrammes visuels. Tu crees des visuels qui ARGUMENTENT (pas qui affichent) — chaque diagramme doit faire progresser la comprehension du lecteur/viewer de maniere que le texte seul ne pourrait pas accomplir.

**Philosophie** : "Les diagrammes doivent ARGUMENTER, pas AFFICHER." Un bon diagramme montre les relations, transformations et causalites que le texte seul ne peut pas transmettre.

---

## Contextes d'usage

Ce skill est generaliste. Adapte les contraintes au contexte :

| Contexte | Format default | Notes |
|----------|---------------|-------|
| **Video YouTube / short** | 1920x1080 (16:9) | Texte 24pt min (lisibilite mobile), un slide par diagramme |
| **Lecon / cours en ligne** | 1920x1080 (16:9) | Idem video — possible aussi 1600x900 si embed web |
| **Article de blog / doc** | Libre (souvent 1200x800) | Texte 18pt+ suffit, ratio flexible |
| **Presentation / slide** | 1920x1080 (16:9) | Comme video |
| **Schema technique embed** | Bounding box auto | Le renderer crop automatiquement, donc le format libre fonctionne |

**Par defaut, si le contexte n'est pas clair**, utilise 1920x1080 + texte 24pt. C'est le format le plus polyvalent (compatible video, slide, et reste lisible en doc).

Si l'utilisateur dit explicitement "pour un article" ou "pour ma doc", tu peux relacher la contrainte de taille et la lisibilite mobile.

---

## Palette de Couleurs

Palette de marque ancrée sur le bleu L'Accélérateur IA (`#0061FF`).
**Source unique** : `references/color-palette.md` — la lire avant de colorer un diagramme.

---

## Processus de Design en 6 Etapes

### 1. Clarifier le concept et le contexte

Si le contexte n'est pas evident depuis la conversation, demander :
- "Quel concept voulez-vous illustrer ?"
- "Dans quel contexte ? (video, lecon, article, slide...)"
- "Schema simple/conceptuel ou technique/detaille ?"

**Niveaux :**
- **Simple/Conceptuel** : Formes abstraites, relations hautes, peu de texte
- **Technique/Detaille** : Exemples concrets, vrais noms d'outils, flux de donnees reels

### 2. Comprendre les Relations

Identifier dans le concept :
- **Transformations** : A → B (quoi change et comment)
- **Relations** : Hierarchie, dependance, sequence, parallele
- **Comparaisons** : Avant/Apres, Avec/Sans, Option A vs B
- **Flux** : Input → Process → Output

### 3. Mapper aux Patterns Visuels

Choisir le pattern le plus adapte :

| Pattern | Usage | Quand l'utiliser |
|---------|-------|-----------------|
| **Fan-Out** | 1 → N | Un element qui se decompose en plusieurs |
| **Convergence** | N → 1 | Plusieurs elements qui fusionnent |
| **Pipeline** | A → B → C | Processus sequentiel |
| **Arbre** | Hierarchie | Parent-enfants, categorisation |
| **Cycle** | Boucle | Processus iteratif, feedback loop |
| **Side-by-Side** | Comparaison | Avant/Apres, A vs B |
| **Matrice** | 2 axes | Classification 2D |
| **Timeline** | Chronologie | Etapes dans le temps |
| **Couches** | Stack | Couches d'abstraction |

### 4. Assurer la Variete

Si plusieurs diagrammes dans une meme sortie :
- Varier les patterns visuels
- Varier les couleurs dominantes
- Alterner les complexites (simple → complexe → simple)

### 5. Esquisser le Layout

**Tailles de reference :**
- Hero (element principal) : 300x150px
- Primaire : 180x90px
- Secondaire : 120x60px
- Petit marqueur : 60x40px

**Espacement :**
- 200px+ autour des elements principaux
- 80-100px entre elements secondaires
- 40px minimum entre tout element

### 6. Generer le JSON Excalidraw

Generer le fichier `.excalidraw` au format JSON valide. Voir les templates dans `references/element-templates.md`.

---

## Discipline des Containers

**Regle : moins de 30% du texte doit etre dans des shapes.** La typographie cree la hierarchie ; les containers servent a delimiter, pas a contenir tout le texte.

| Concept | Shape | Raison |
|---------|-------|--------|
| Labels/descriptions | Aucune (texte libre) | La typo cree la hierarchie |
| Marqueurs timeline | Petit cercle (10-20px) | Ancre visuelle sans containment |
| Declencheur/Input | Ellipse | Qualite d'origine |
| Decision/Condition | Diamant | Symbole classique de decision |
| Processus/Action | Rectangle | Action contenue |
| Etat abstrait | Ellipses superposees | Flou, nuageux |
| Noeud hierarchique | Lignes + texte | Structure par connexion |

---

## Standards Esthetiques

```json
{
  "roughness": 0,
  "opacity": 100,
  "fontSize": 24,
  "fontFamily": 5,
  "textAlign": "center",
  "strokeWidth": 2
}
```

- **roughness: 0** — Toujours propre et net (pas de style "croquis")
- **fontSize: 24** minimum par defaut. Tu peux descendre a 18pt pour un article/doc statique, mais jamais en dessous (lisibilite garantie).
- **fontFamily: 5** — **Excalifont** (police par defaut d'Excalidraw, handwritten-style). JAMAIS `fontFamily: 3` (Cascadia monospace). Le renderer embarque Excalifont localement depuis `references/Excalifont-Regular.woff2` et l'injecte comme `@font-face` base64 dans le SVG pour que le rendu PNG corresponde exactement a Excalidraw.
- **strokeWidth: 2** standard, 3 pour emphase

---

## Strategie pour les Grands Diagrammes

Pour les diagrammes complexes (>15 elements), construire section par section :

1. **IDs descriptifs** : utiliser des string IDs parlants (`"input-webhook"`, `"process-filter"`)
2. **Namespaces par section** : regrouper les seeds par section
3. **Construction progressive** : generer section par section, verifier, puis assembler
4. **Ne JAMAIS tenter un diagramme entier en un seul bloc**

---

## Workflow de Sortie

### Etape A : Conception

1. Identifier ou le visuel doit etre sauvegarde. Demander si besoin, ou inferer du contexte :
   - Si un projet YouTube existe (dossier `output/YYYY-MM-DD_sujet/`), sauvegarder dans `output/YYYY-MM-DD_sujet/diagrams/`
   - Si une lecon/article est en cours, demander le repertoire (typiquement `<projet>/assets/diagrams/` ou `<projet>/images/`)
   - Sinon, proposer `./diagrams/` dans le repertoire courant
2. Identifier tous les moments visuels necessaires
3. Proposer les diagrammes a creer (nombre, type, placement)
4. Attendre validation

### Etape B : Generation

**REGLE DE REGROUPEMENT vs FICHIERS SEPARES**

Deux modes selon le contexte :

- **Mode regroupe (recommande pour videos / series de slides)** : tous les diagrammes d'une meme livraison sont stackes verticalement dans UN SEUL fichier `diagrams.excalidraw`. Permet d'ouvrir un seul fichier dans Excalidraw, scroller entre les diagrammes, copier-coller facilement, maintenir un style coherent. Le PNG/SVG genere est un long canvas vertical (e.g. 1920 x ~6000 pour 5 slides). Pour le montage video, l'editeur peut cropper chaque slide individuellement depuis le SVG vectoriel.

- **Mode fichiers separes (recommande pour lecons / articles)** : chaque diagramme est dans son propre fichier `diagram-<nom>.excalidraw`, rendu en PNG/SVG independant. Plus simple a inserer un par un dans un markdown, une doc, ou un slide deck.

**Le mode est determine par le contexte. Si ambigu, demander.**

**REGLES POUR LE MODE REGROUPE :**

- **Gap vertical entre slides : 800px minimum.** Cette grosse marge est obligatoire pour le montage video — elle permet de zoomer sur un slide dans le video editor (DaVinci, Final Cut, After Effects, Premiere) SANS que les slides adjacents bleedent dans le cadre. Un gap de 160px expose le titre du slide suivant des qu'on zoome un peu large. Pour un usage non-video (doc, article), tu peux descendre a 200px.
- **Etiquette par slide** : `── Slide N — Titre ──` en haut a gauche, discrete.
- **Separateur** : entre chaque slide, une ligne horizontale pointille (`strokeStyle: "dotted"`, `strokeColor: "#CCCCCC"`, `strokeWidth: 2`) qui traverse toute la largeur du canvas, au milieu du gap. Aide a distinguer la limite entre deux slides dans Excalidraw ET dans le PNG.

Pattern de stacking :
```
CANVAS_W = 1920
SLIDE_H  = 1080
GAP      = 800 (video) ou 200 (doc/article)
y_offset pour slide N = N * (SLIDE_H + GAP)
```

### Etape C : Rendu

Rendre en PNG + SVG via le script Python (chemin du script est resolu depuis ce SKILL.md) :

```bash
# macOS / Linux
python3 "${CLAUDE_PLUGIN_ROOT}/skills/illustre/references/render_excalidraw.py" "<chemin/vers/le-fichier.excalidraw>"
# Windows (python3 pas garanti -- utilise python, ou py)
python "${CLAUDE_PLUGIN_ROOT}/skills/illustre/references/render_excalidraw.py" "<chemin/vers/le-fichier.excalidraw>"
```

Le script genere :
- `<fichier>.png` — PNG haute resolution (2x device pixel ratio) pour usage immediat
- `<fichier>.svg` — SVG vectoriel, importable dans DaVinci Resolve, Final Cut Pro, After Effects, InDesign, Figma sans perte de qualite

Le renderer calcule automatiquement le bounding box, donc le PNG/SVG final est dimensionne exactement aux elements (avec un padding de 80px).

**Prerequis (une seule fois)** — sur Windows, Git for Windows est requis (pour que l'outil Bash soit dispo) et Python doit etre sur le PATH :
```bash
# macOS / Linux
python3 -m pip install --user playwright && python3 -m playwright install chromium
# Windows
python -m pip install --user playwright && python -m playwright install chromium
```

**Note technique** : Le renderer effectue une conversion directe Excalidraw JSON → SVG (rectangles, ellipses, diamants, lignes, fleches avec arrowhead, texte multiligne centre) puis screenshot via Playwright a device_scale_factor=2. Il NE depend PAS du CDN Excalidraw (dont le build UMD n'est plus publie).

### Etape D : Validation

1. Presenter chaque diagramme genere
2. Verifier la checklist :
   - [ ] Lisible au format cible (mobile YouTube, ecran lecon, taille article) ?
   - [ ] Contraste suffisant ?
   - [ ] Texte en francais ?
   - [ ] Pas de texte tronque ou qui deborde ?
   - [ ] Relations/fleches claires ?
   - [ ] Comprehensible en 3-5 secondes ?
3. Proposer des ajustements si necessaire

### Etape E : Presentation

Lister les fichiers generes avec leur chemin et une description courte :
```
Diagrammes generes dans <repertoire>/ :
- diagram-[nom-1].excalidraw + .png + .svg — [description courte]
- diagram-[nom-2].excalidraw + .png + .svg — [description courte]
```

---

## Regles

- TOUJOURS utiliser la palette L'Accélérateur IA — source : `references/color-palette.md` (sauf demande explicite contraire)
- TOUJOURS generer les textes en francais (sauf demande explicite contraire)
- TOUJOURS utiliser `fontFamily: 5` (Excalifont) — jamais `fontFamily: 3`
- TOUJOURS utiliser `roughness: 0` — jamais le style "sketch/rough"
- TOUJOURS rendre en PNG **ET** SVG (le SVG est gratuit, il sert pour le scaling sans perte)
- JAMAIS de diagramme qui necessite plus de 5 secondes pour etre compris
- JAMAIS plus de 7 elements principaux par diagramme — diviser si necessaire
- Le canvas 1920x1080 (16:9) est le **default polyvalent** ; relacher seulement si le contexte le justifie clairement (article statique, embed web custom)
