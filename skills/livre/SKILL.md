---
name: livre
description: "Vérifie le changement (via /verifie), commit, se synchronise avec main distant, push la branche courante et crée une Pull Request avec les preuves de vérification. Refuse de tourner directement sur main. Utilise sur /livre, ou quand l'utilisateur veut livrer/expédier son travail : \"commit et push\", \"ouvre une PR\", \"livre ça\", \"ship\", \"envoie la PR\", \"finalise et pousse\". Aval naturel de /branche et /verifie."
argument-hint: "[message-de-commit]"
---

# /livre

Vérifie, commit, synchronise avec main distant, push, et crée une Pull Request avec les preuves.

## Étapes

### 1. Vérification de sécurité
- Exécute `git branch --show-current` pour obtenir la branche courante
- Si tu es sur `main`, **refuse** et demande à l'utilisateur de créer d'abord une branche de fonctionnalité (propose `/branche`)

### 2. Synchronisation avec main distant
- Récupère la dernière version : `git fetch origin main`
- Vérifie si la branche est en retard : `git log HEAD..origin/main --oneline`
- Si en retard sur origin/main, fusionne : `git merge origin/main`
- En cas de conflits de fusion, montre-les à l'utilisateur et aide à les résoudre avant de continuer

La synchronisation passe **avant** la vérification : on vérifie le code tel qu'il sera livré, fusion comprise.

### 3. Vérification

Rien ne part sans preuve. Déroule dans l'ordre :

1. **Pas de `docs/VERIFICATION.md`** : annonce *« Ce projet n'a pas encore de vérification. J'installe `/verifie`, je vérifie, puis je livre. »* et applique le skill `/verifie` (installation puis exécution).
2. **Tampon valide** : si `.claude/verifie.json` existe, recalcule l'empreinte de l'état du code avec la commande du skill `/verifie` (section B4). Si elle est identique au champ `empreinte` et que `resultat` vaut `vert`, réutilise ce rapport sans relancer.
3. **Sinon** : applique le skill `/verifie` (exécution).

Ensuite :
- **Rouge** (échec après 3 tours) : **STOP**. Montre le rapport, propose `/investigue`. Ne commit pas.
- **Vert avec corrections** : si `/verifie` a modifié du code pendant ses tours de correction, montre le diff de ces corrections et **attends la validation explicite** de l'utilisateur avant de continuer. On ne commit pas du code que personne n'a vu.
- **Vert** : continue.

**Porte de sortie** : à tout moment de cette étape, l'utilisateur peut dire « livre sans vérifier ». Exige une raison en une phrase (ex. « correction de typo dans le README »), puis continue en la traçant dans le commit et la PR. N'en propose jamais l'usage toi-même.

### 4. Staging et commit
- Exécute `git status` pour voir tous les changements (n'utilise jamais le flag `-uall`)
- Exécute `git diff` et `git diff --staged` pour revoir les changements
- Exécute `git log --oneline -5` pour voir le style des commits récents
- Ajoute au staging les fichiers modifiés/nouveaux pertinents (nomme les fichiers précisément, pas `git add -A`), y compris les tests E2E écrits par `/verifie` et `docs/VERIFICATION.md`
- N'ajoute PAS au staging les fichiers contenant des secrets (`.env`, identifiants, etc.)
- **Si `$ARGUMENTS` est fourni**, utilise-le comme message de commit
- **Si aucun argument**, rédige un message de commit selon les conventions de CLAUDE.md :
  - Utilise un préfixe de type : `feat:` (nouvelle fonctionnalité) ou `fix:` (correction de bug)
  - Mets l'accent sur le « pourquoi » plutôt que le « quoi »
- Avant les lignes de co-auteur, ajoute une ligne de vérification :
  - `Vérifié: oui (arbre <7 premiers caractères de l'empreinte>)`
  - ou `Vérifié: non (<raison de la porte de sortie>)`
- Termine par `Co-Authored-By: Claude`
- Utilise un HEREDOC pour le message de commit afin d'assurer un formatage correct
- Après le commit, compare `git rev-parse HEAD^{tree}` à l'empreinte vérifiée. Si elles diffèrent (des fichiers vérifiés n'ont pas été commités), liste ces fichiers à l'utilisateur et demande s'il faut les ajouter ou revérifier l'état commité avant de pousser.

### 5. Push
- Push avec le suivi de la branche amont : `git push -u origin HEAD`

### 6. Création de la PR
- Utilise `gh pr create` avec :
  - Un titre court (moins de 70 caractères)
  - Un corps contenant :
    - `## Résumé` (1 à 3 puces)
    - `## Preuves de vérification` : le rapport de `/verifie` (bloc de code), la liste des critères du PLAN couverts par cette PR, et les remarques ⚠ de la passe exploratoire à trancher par le relecteur. En cas de porte de sortie : *« Non vérifié : <raison> »*.
  - Utilise un HEREDOC pour le corps
- Les captures de la passe exploratoire restent locales : cite leurs chemins, ne les commit pas
- Retourne l'URL de la PR à l'utilisateur
