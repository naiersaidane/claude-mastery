---
name: investigue
description: "Investiguer méthodiquement un bug en 4 phases validées : localiser/reproduire, 3 hypothèses classées sur la cause racine, logs ciblés, fix minimal. Utilise sur /investigue, ou dès que l'utilisateur décrit un symptôme (\"ça plante quand…\", \"je vois X mais j'attends Y\", \"comportement inattendu\", \"pourquoi ça crash\", \"investigue ce bug\", \"debug ça\", \"analyse le bug\"). Ne propose jamais de fix immédiat — chaque phase s'arrête et attend une validation explicite avant de passer à la suivante."
---

Avant de commencer, vérifie que tu disposes de deux éléments :
- **Le symptôme** : ce qui se passe concrètement (message d'erreur, comportement observé, valeur retournée…)
- **Le comportement attendu** : ce qui devrait se passer à la place

Si l'un ou l'autre manque, demande-le explicitement avant d'aller plus loin.

---

Avant tout fix, déroule ces 4 phases dans l'ordre. Arrête-toi à la fin de chacune et attends ma validation.

## PHASE 1 : Localiser et reproduire.
À partir du symptôme, explore le code (utilise le sous-agent Explore si nécessaire) pour identifier les 2-3 zones les plus susceptibles d'héberger la cause. Liste-les avec une phrase de justification chacune. Puis décris en 3 lignes le scénario minimal qui rejoue ce bug à coup sûr. Si tu ne peux pas le reproduire de manière fiable, dis-le et propose un plan pour y arriver.

## PHASE 2 : 3 hypothèses classées sur la cause racine.
Propose 3 hypothèses sur la cause racine (pas le symptôme), classées de la plus probable à la moins probable. Pour chacune : hypothèse en 1 phrase, puis prédiction falsifiable — « si cette hypothèse est vraie, on observerait <observation précise> ; si on observe l'inverse, on l'élimine ».

## PHASE 3 : Tester l'hypothèse #1.
Ajoute des logs ciblés pour vérifier l'hypothèse #1. Préfixe chaque log par le tag [DEBUG-a4f2] (4 caractères au hasard) pour suppression en bulk plus tard. Ne propose pas de fix à cette phase. Dis-moi ce que je dois observer pour confirmer ou infirmer.

Règle des 3 strikes : si les 3 hypothèses sont fausses, STOP. Ce n'est plus un bug de code, c'est une question d'architecture. On change d'angle.

## PHASE 4 : Fix minimal.
Une fois l'hypothèse confirmée, propose les modifications les plus courtes qui traitent la cause racine. Pas d'optimisation collatérale, pas de refactor opportuniste. Rédige le message de commit en expliquant la cause racine, pas le symptôme.
