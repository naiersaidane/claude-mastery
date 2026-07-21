---
name: livre
description: "Commit les changements, se synchronise avec main distant, push la branche courante et crée une Pull Request. Refuse de tourner directement sur main. Utilise sur /livre, ou quand l'utilisateur veut livrer/expédier son travail : \"commit et push\", \"ouvre une PR\", \"livre ça\", \"ship\", \"envoie la PR\", \"finalise et pousse\". Aval naturel de /branche."
argument-hint: "[message-de-commit]"
---

# /livre

Commit tous les changements, synchronise avec main distant, push, et crée une Pull Request.

## Étapes

### 1. Vérification de sécurité
- Exécute `git branch --show-current` pour obtenir la branche courante
- Si tu es sur `main`, **refuse** et demande à l'utilisateur de créer d'abord une branche de fonctionnalité (propose `/branche`)

### 2. Synchronisation avec main distant
- Récupère la dernière version : `git fetch origin main`
- Vérifie si la branche est en retard : `git log HEAD..origin/main --oneline`
- Si en retard sur origin/main, fusionne : `git merge origin/main`
- En cas de conflits de fusion, montre-les à l'utilisateur et aide à les résoudre avant de continuer

### 3. Staging et commit
- Exécute `git status` pour voir tous les changements (n'utilise jamais le flag `-uall`)
- Exécute `git diff` et `git diff --staged` pour revoir les changements
- Exécute `git log --oneline -5` pour voir le style des commits récents
- Ajoute au staging les fichiers modifiés/nouveaux pertinents (nomme les fichiers précisément, pas `git add -A`)
- N'ajoute PAS au staging les fichiers contenant des secrets (`.env`, identifiants, etc.)
- **Si `$ARGUMENTS` est fourni**, utilise-le comme message de commit
- **Si aucun argument**, rédige un message de commit selon les conventions de CLAUDE.md :
  - Utilise un préfixe de type : `feat:` (nouvelle fonctionnalité) ou `fix:` (correction de bug)
  - Mets l'accent sur le « pourquoi » plutôt que le « quoi »
  - Termine par `Co-Authored-By: Claude`
- Utilise un HEREDOC pour le message de commit afin d'assurer un formatage correct

### 4. Push
- Push avec le suivi de la branche amont : `git push -u origin HEAD`

### 5. Création de la PR
- Utilise `gh pr create` avec :
  - Un titre court (moins de 70 caractères)
  - Un corps contenant `## Résumé` (1 à 3 puces) et `## Plan de test`
  - Utilise un HEREDOC pour le corps
- Retourne l'URL de la PR à l'utilisateur
