---
name: planifie
description: Découper un PRD en phases indépendamment livrables par tranches verticales (tracer bullets), puis produire ou étendre `docs/PLAN.md` selon un template fixe (décisions architecturales + phases avec user stories, livrable, critères d'acceptation, dépendances). Utilise sur /planifie, "découpe le PRD", "fais le plan d'implémentation", "casse-moi ça en phases", "écris le plan", "étends le plan", "tracer bullets", "vertical slices", ou dès qu'il faut transformer un PRD en plan d'exécution versionné. Aval naturel de /cadre.
---

# /planifie

Découpe un PRD en phases indépendamment livrables par tranches verticales (tracer bullets). Sortie dans `docs/PLAN.md`.

## Process

### 1. Récupère le PRD

Par défaut, lis `docs/PRD.md`. Si un chemin de fichier est passé en argument, lis-le. Si rien d'utilisable, demande à l'utilisateur de pointer le fichier ou de coller le contenu.

### 2. Mode extension si PLAN existe

Si `docs/PLAN.md` existe déjà, lis-le. Repère les user stories du PRD non couvertes par une phase existante et les incohérences avec un PRD qui a bougé. Ne réécris pas les phases déjà validées ; propose des phases additionnelles ou des extensions ciblées, et signale les contradictions à l'utilisateur avant d'écrire.

Si les critères d'acceptation existants n'ont pas d'identifiant `P<phase>-C<n>` ou ne sont pas au format scénario observable (voir `<règles-critères>`), propose de les convertir. La conversion reformule sans changer le sens ; montre l'avant/après et attends la validation.

### 3. Explore le codebase

Si tu n'as pas déjà exploré le codebase, fais-le pour comprendre l'architecture actuelle, les patterns en place et les couches d'intégration. Si le projet est vierge (greenfield), saute cette étape.

### 4. Identifie les décisions architecturales durables

Avant de découper, identifie les décisions de haut niveau qui ne devraient pas bouger en cours d'implémentation :

- Structure des routes / patterns d'URL
- Forme du schéma de base de données
- Noms des modèles de données clés
- Approche d'authentification / autorisation
- Frontières des services tiers

Elles vont dans l'en-tête du plan, chaque phase peut s'y référer.

### 5. Drafte les tranches verticales

Découpe le PRD en phases **tracer bullets**. Chaque phase est une tranche fine qui traverse TOUTES les couches d'intégration de bout en bout, PAS une tranche horizontale d'une seule couche.

<règles-tranche-verticale>
- Chaque tranche livre un chemin étroit mais COMPLET à travers toutes les couches (schema, API, UI, tests)
- Une tranche terminée est démontrable ou vérifiable seule
- Préfère beaucoup de tranches fines à peu de tranches épaisses
- N'inclus PAS les noms de fichiers, noms de fonctions, ou détails d'implémentation susceptibles de changer
- INCLUS les décisions durables : routes, formes de schéma, noms de modèles
</règles-tranche-verticale>

<règles-critères>
Les critères d'acceptation sont la liste de ce que `/verifie` prouvera : chacun deviendra un test E2E.

- **Identifiant** : `P<phase>-C<n>` (ex. `P2-C3`), stable une fois écrit. Un critère supprimé ne libère pas son numéro.
- **Scénario observable** : *« <acteur> <action>, il/elle voit <résultat observable> »*. Le résultat se constate de l'extérieur : un écran, un message, un fichier produit, une réponse HTTP, une sortie de commande.
- **Pas de jugement intérieur ni de détail d'implémentation** : pas de « le code est propre », « la fonction X est appelée », « l'utilisateur comprend ».
- Couvre aussi les états vides, les erreurs et les cas limites que la phase introduit.
- **Invariants** (optionnel) : si la phase contient de la logique métier, liste les propriétés qui doivent toujours tenir (aller-retour, invariant, idempotence). `/verifie` pourra en faire des tests de propriétés.
</règles-critères>

### 6. Quiz l'utilisateur

Présente le découpage sous forme de liste numérotée. Pour chaque phase :

- **Titre** : nom court descriptif
- **Bloquée par** : autres tranches devant terminer d'abord
- **User stories couvertes** : numéros des user stories du PRD

Puis demande :

- La granularité est-elle bonne ? (trop grossière / trop fine)
- Les dépendances sont-elles correctes ?
- Des phases à fusionner ou découper davantage ?

Itère jusqu'à validation.

### 7. Écris le plan

Crée `docs/` si absent. Écris `docs/PLAN.md` selon le template. En mode extension, intègre les phases additionnelles aux phases existantes sans toucher au contenu déjà validé. Confirme *« ✓ écrit dans `docs/PLAN.md` »*.

<plan-template>
# Plan : <nom de la feature>

> PRD source : <chemin ou identifiant>

## Décisions architecturales

Décisions durables qui s'appliquent à toutes les phases :

- **Routes** : ...
- **Schema** : ...
- **Modèles clés** : ...
- (ajoute/retire des sections selon le contexte)

---

## Phase 1 : <titre>

**User stories** : <liste depuis le PRD>

### Ce qu'on livre

Description concise de cette tranche verticale. Décris le comportement de bout en bout, pas l'implémentation couche par couche.

### Critères d'acceptation

- [ ] **P1-C1** : <acteur> <action>, il/elle voit <résultat observable>
- [ ] **P1-C2** : ...
- [ ] **P1-C3** : ...

### Invariants

<!-- Optionnel, seulement si la phase contient de la logique métier. Sinon, supprime la section. -->

- <propriété qui doit toujours tenir>

## Bloquée par

- Référence à la phase bloquante (s'il y en a)

Ou *« Aucune — démarrable immédiatement »* s'il n'y a pas de bloqueur.

---

## Phase 2 : <titre>

**User stories** : <liste depuis le PRD>

### Ce qu'on livre

...

### Critères d'acceptation

- [ ] **P2-C1** : ...

## Bloquée par

- ...

<!-- Répéter pour chaque phase -->
</plan-template>
