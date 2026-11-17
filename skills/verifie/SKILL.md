---
name: verifie
description: "Vérifier qu'un changement marche vraiment avant de le livrer : contrôles rapides (lint, types, tests), tests E2E persistants (un par critère d'acceptation du PLAN), checklist déclenchée par le diff, passe exploratoire sur l'app qui tourne, puis rapport de preuves. Au premier lancement, installe la vérification du projet dans `docs/VERIFICATION.md`. Utilise sur /verifie, \"vérifie\", \"teste tout\", \"est-ce que ça marche ?\", \"c'est prêt ?\", avant de déclarer une phase terminée, ou quand /livre le déclenche. Pair naturel de /planifie (amont, critères) et /livre (aval)."
argument-hint: "[couvre-tout]"
---

# /verifie

Prouve que le code fait ce que le PLAN promet, sur l'app qui tourne, avant toute livraison. Tu ne déclares rien « fait » sans preuve.

Deux modes :
- **Installation** : `docs/VERIFICATION.md` n'existe pas → installe la vérification du projet (section A), puis enchaîne sur l'exécution.
- **Exécution** : `docs/VERIFICATION.md` existe → exécute la vérification (section B).

Argument `couvre-tout` : en plus de l'exécution, écris les E2E manquants pour **tous** les parcours non couverts (rattrapage d'un projet existant).

## Règles non négociables

- **On corrige le code, jamais le test.** Un test existant ne se modifie que si le comportement attendu a changé dans `docs/PRD.md` ou `docs/PLAN.md`, et seulement avec l'accord de l'utilisateur. Un changement ne doit pas pouvoir modifier le contrôle qui le juge.
- **Pas de `sleep`, pas de relance jusqu'au vert.** Un test qui passe à la relance sans changement est **instable** : il compte comme un échec.
- **Pas de test sauté en silence.** Tout ce qui n'a pas tourné apparaît dans le rapport avec la raison.
- **Preuves, pas affirmations.** Chaque ligne du rapport s'appuie sur une sortie de commande, un résultat de test ou une capture.

---

## A. Installation

### A1. Détecte le type de projet

Explore le repo (`package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, scripts, structure, `CLAUDE.md`, `docs/`). Classe le projet :

| Type | Vérification du comportement | Ce qui est persistant |
|---|---|---|
| **App web** | Playwright E2E sur l'app lancée en local + passe exploratoire navigateur | `e2e/*.spec.*` |
| **API / backend** | Serveur lancé en local, vrais appels HTTP | Tests d'intégration du framework |
| **CLI / script / automatisation** | Commande exécutée sur des entrées réelles, sortie comparée | Tests qui lancent la commande |
| **Lib** | Tests via l'interface publique ; tests de propriétés si logique métier | Tests unitaires + propriétés |
| **Contenu seul** (Markdown, skills, docs) | Contrôles légers : frontmatter valide, liens non cassés, rendu | Script de contrôle léger |

Un projet peut cumuler (web + API). Annonce ta classification en une ligne et fais-la valider.

**Tests de propriétés** : propose-les (fast-check, Hypothesis, proptest selon la langue) quand une phase du PLAN a une ligne « Invariants », ou pour une lib avec de la logique métier. Jamais imposés. Propriétés typiques : aller-retour (encoder puis décoder redonne l'original), invariant (un solde ne devient jamais négatif), idempotence (appliquer deux fois = une fois).

### A2. Établis le « comment »

Trouve dans le repo, sinon demande (une question à la fois, avec ta recommandation) :
- **Contrôles rapides** : la commande unique qui enchaîne lint + types + tests unitaires. S'il n'y en a pas, propose de l'ajouter (ex. script `check` dans `package.json`).
- **Lancer l'app** : commande, port, URL, données de test ou compte de démo nécessaires.
- **Outillage E2E** (web) : si Playwright est absent, propose de l'installer (`npm i -D @playwright/test` puis `npx playwright install chromium`) et de configurer le mode trace (`trace: 'retain-on-failure'`). Attends l'accord avant d'installer.

### A3. Recense les parcours

- **PLAN présent** : la source des parcours est `docs/PLAN.md`. Chaque critère d'acceptation porte un identifiant `P<phase>-C<n>`. Si le PLAN est à l'ancien format (critères non identifiés ou non observables), propose de le convertir via `/planifie` ; en attendant, numérote-les toi-même dans `VERIFICATION.md`.
- **Pas de PLAN** (projet existant ou hors méthode) : explore l'app et/ou interroge l'utilisateur, puis liste les parcours dans une section « Parcours » de `VERIFICATION.md`, identifiants `R-<n>`, chacun au format scénario observable.

**Projet existant, sans tests** : n'écris pas tous les E2E maintenant. Recense tous les parcours avec le statut « pas encore de test » ; seuls les parcours touchés par le diff en cours reçoivent leur E2E à l'exécution. Le rattrapage complet se fait avec `/verifie couvre-tout`, quand l'utilisateur le décide.

### A4. Écris les fichiers

Montre d'abord ce que tu vas écrire, puis écris :

1. `docs/VERIFICATION.md` selon le template ci-dessous.
2. Ajoute au `.gitignore` du projet : `.claude/verifie.json` et les dossiers d'artefacts de test (ex. `test-results/`, `playwright-report/`).
3. Ajoute au `CLAUDE.md` du projet (crée-le si absent) cette section, telle quelle :

```md
## Définition de done

- Une phase du PLAN n'est terminée que lorsque `/verifie` est vert.
- N'annonce jamais « c'est fait » sans le rapport de vérification.
- On corrige le code, jamais un test pour le faire passer.
```

Confirme *« ✓ vérification installée dans `docs/VERIFICATION.md` »*, puis passe à l'exécution (section B).

<verification-template>
# Vérification : <nom du projet>

> Type : <web | API | CLI | lib | contenu seul> · Source des parcours : <docs/PLAN.md | section Parcours ci-dessous>

## Lancer l'app

- Commande : `...`
- URL / port : ...
- Données ou compte de test : ...

## Contrôles rapides

- Commande : `...` (lint + types + tests unitaires)

## Couverture des parcours

| Critère | Scénario (résumé) | Test |
|---|---|---|
| P1-C1 | ... | `e2e/p1-c1-....spec.ts` |
| P1-C2 | ... | pas encore de test |

Couverture : <n>/<total> parcours.

## Parcours

<!-- Seulement si pas de PLAN. Sinon : « Voir docs/PLAN.md ». -->

- **R-1** : je <action>, je vois <résultat observable>.

## Checklist déclenchée par le diff

<!-- Vide au départ. Ne s'alimente qu'à partir de vrais incidents (/investigue, passe exploratoire, demande de l'utilisateur). -->

Aucun item pour l'instant.

## Tests retirés

<!-- Test instable dont la cause reste introuvable, supprimé avec l'accord de l'utilisateur : nom, date, pourquoi. -->

Aucun.
</verification-template>

Format d'un item de checklist (à respecter quand on en ajoute) :

```md
### C-<n> : <ce qui ne doit plus casser>
- **Déclencheur** : <ce qu'on repère dans un diff : fichier, modèle, route, dépendance…>
- **Vérification** : <action concrète et résultat attendu>
- **Origine** : <incident, date, PR ou /investigue>
```

---

## B. Exécution

### B1. Prépare

- Lis `docs/VERIFICATION.md` et, s'il est la source, `docs/PLAN.md`.
- Calcule le diff à vérifier : `git diff HEAD` + fichiers non suivis, et `git diff origin/main...HEAD` si la branche a déjà des commits.
- **Synchronise la couverture** :
  - critère du PLAN sans test **et** touché par le diff (ou argument `couvre-tout`) → écris son E2E ;
  - test dont le critère a disparu du PLAN → **signale-le**, ne le supprime pas.
  - Mets à jour la table « Couverture des parcours ».

Écriture d'un E2E : un fichier par critère, nommé par son identifiant (`e2e/p2-c3-<slug>.spec.ts`), qui suit le scénario du critère (action utilisateur → résultat observable) via les rôles et textes visibles plutôt que des sélecteurs fragiles. Écris-le **avant** de le lancer contre le code : il doit pouvoir échouer.

### B2. Exécute, du moins cher au plus cher

Arrête-toi au premier échec et passe en B3.

1. **Contrôles rapides** : la commande de `VERIFICATION.md`.
2. **E2E** : **tous** les tests persistants, pas seulement ceux du diff. C'est ce qui attrape les régressions d'une phase sur l'autre. Lance l'app si nécessaire.
3. **Checklist** : lis le diff, sélectionne uniquement les items dont le déclencheur correspond, exécute leur vérification.
4. **Passe exploratoire** (si un outil de navigateur est disponible : MCP Playwright, Claude in Chrome…) : parcours ce que le diff vient de changer sur l'app lancée, cherche ce qu'un test scripté ne voit pas (mise en page cassée, état vide manquant, texte illisible, mobile). Capture d'écran pour chaque remarque. Sans outil de navigateur : indique « passe exploratoire non faite (pas d'outil navigateur) ».

Si la suite E2E dépasse ~5 minutes, signale-le dans le rapport et propose de paralléliser ou d'élaguer. Ne saute jamais de test pour gagner du temps.

### B3. En cas d'échec : 3 tours maximum

Un tour = diagnostiquer la cause → corriger le **code** → relancer depuis l'étape qui a échoué.

- **Test instable** (passe à la relance sans changement) : compte comme un échec. Cherche la cause (attente manquante sur un état, donnée partagée, ordre des tests). Si elle reste introuvable, propose de supprimer le test et de le noter dans « Tests retirés », avec l'accord de l'utilisateur.
- **L'attendu a changé** (le PLAN dit autre chose que le test) : arrête-toi, montre l'écart, demande l'accord avant de modifier le test.
- **Encore rouge après 3 tours** : STOP. Rapport avec ce qui a été essayé, ce qui reste rouge, l'hypothèse la plus probable. Propose `/investigue`. Pas de tampon.

### B4. Écris le tampon (seulement si tout est vert)

Calcule l'empreinte de l'état exact du code (arbre git du répertoire de travail, fichiers ignorés exclus, index réel intact) :

```bash
d=$(mktemp -d); cp "$(git rev-parse --git-dir)/index" "$d/index" 2>/dev/null; GIT_INDEX_FILE="$d/index" git add -A && GIT_INDEX_FILE="$d/index" git write-tree; rm -rf "$d"
```

Cette empreinte est égale à `git rev-parse HEAD^{tree}` une fois le code commité tel quel. Le moindre octet changé la modifie.

Écris `.claude/verifie.json` :

```json
{
  "empreinte": "<hash de l'arbre>",
  "date": "<ISO 8601>",
  "resultat": "vert",
  "rapport": "<le rapport B5, en texte>",
  "captures": ["<chemins des captures de la passe exploratoire>"]
}
```

### B5. Rapporte

Toujours ce format, dans le chat :

```
✓ Vérifié — empreinte 3f9a2c1
  Contrôles rapides   ✓ lint, types, 48 tests (12 s)
  E2E                 ✓ 14/14 (P1-C1 … P3-C4) (1 min 40)
  Checklist           ✓ C-2, C-4 déclenchés, OK
  Exploratoire        ⚠ 1 remarque : bouton « Valider » coupé sur mobile (capture : …)
  Couverture          14/15 parcours (R-7 sans test)
  Corrections         aucune
```

- Remplace `✓` par `✗` sur l'étape en échec et `—` sur les étapes non lancées.
- **Corrections** : liste les fichiers de code modifiés pendant les tours de B3. S'il y en a, l'utilisateur doit les voir.
- **Remarques ⚠** : non bloquantes. Elles sont listées, l'humain tranche. Si une remarque est un vrai bug, propose d'en faire un critère, un E2E ou un item de checklist.
