---
name: branche
description: "Crée une nouvelle branche Git à partir de la dernière version de main, avec un préfixe conventionnel feat/ (nouvelle fonctionnalité) ou fix/ (correction de bug). Utilise sur /branche, ou quand l'utilisateur veut démarrer un nouveau travail sur une branche dédiée : \"nouvelle branche\", \"crée une branche\", \"je commence une feature\", \"pars de main à jour\", avant d'attaquer un développement isolé. Amont naturel de /livre."
argument-hint: "[nom-de-branche]"
---

# /branche

Crée une nouvelle branche à partir de la dernière version de main.

## Étapes

1. Bascule sur main et récupère la dernière version :
   ```bash
   git checkout main && git pull origin main
   ```

2. **Si `$ARGUMENTS` est fourni** (ex. `/branche feat/algorithme-churn`) :
   - Utilise l'argument directement comme nom de branche
   - Crée et bascule sur la branche : `git checkout -b <nom-de-branche>`

3. **Si aucun argument n'est fourni :**
   - Demande à l'utilisateur le nom de la branche ou une description du travail
   - Propose un nom avec un préfixe conventionnel : `feat/` ou `fix/`
   - Une fois confirmé, crée la branche : `git checkout -b <nom-de-branche>`

4. Confirme la création de la branche en exécutant `git branch --show-current`

## Conventions de nommage des branches

Utilise ces préfixes :
- `feat/` — Nouvelle fonctionnalité
- `fix/` — Correction de bug

Si l'utilisateur fournit un nom sans préfixe, propose d'en ajouter un.
