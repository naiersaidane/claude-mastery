# Claude Mastery

**8 skills Claude Code pour passer d'une idée à un produit livré.** La méthode enseignée dans la formation [Claude Mastery](https://laccelerateuria.com) de L'Accélérateur IA, transformée en commandes que ton agent applique tout seul.

![License: MIT](https://img.shields.io/badge/license-MIT-0061FF) ![Installation: skills.sh](https://img.shields.io/badge/install-skills.sh-0061FF) ![Par L'Accélérateur IA](https://img.shields.io/badge/par-L'Acc%C3%A9l%C3%A9rateur%20IA-0F172A)

---

## Installation (30 secondes)

```bash
npx skills add naiersaidane/claude-mastery
```

La commande installe les 8 skills et les rend disponibles pour ton agent (Claude Code et tout agent qui lit les skills). Il te faut juste Node pour exécuter `npx`.

Une fois installés, tu les déclenches par leur commande — `/interroge`, `/cadre`, `/planifie`, `/design`, `/investigue`, `/illustre`, `/branche`, `/livre` — ou par une phrase naturelle (« cadre ce projet », « débugge ça », « fais-moi un diagramme »).

---

## Pourquoi ces Skills

La plupart des frictions avec un agent de code ne viennent pas du modèle. Elles viennent du moment où on lui parle, et de ce qu'on lui demande. Six de ces skills corrigent chacun un de ces moments ; deux de plus — `/branche` et `/livre` — encadrent la livraison Git.

**L'agent code avant d'avoir compris le besoin.** Il devine, part dans une direction, et tu t'en aperçois trop tard. → `/interroge` t'interroge une question à la fois jusqu'à une compréhension partagée, puis `/cadre` fige le besoin dans un PRD.

**Le scope dérive, sans plan livrable.** On empile les tâches, rien n'est jamais « fini ». → `/planifie` découpe le PRD en phases indépendamment livrables, chacune testable de bout en bout.

**Le design est bricolé après coup.** Couleurs et typo choisies au hasard, écran par écran. → `/design` propose un système cohérent et opinioné, documenté et prévisualisable avant la première ligne de CSS.

**Un bug, et c'est la chasse à l'aveugle.** On change trois choses au hasard en espérant que ça passe. → `/investigue` déroule 4 phases validées : localiser, formuler des hypothèses, instrumenter, corriger au minimum.

**Expliquer une idée à l'oral, c'est lent.** Un schéma vaut dix paragraphes. → `/illustre` génère des diagrammes Excalidraw nets en PNG et SVG.

Pris ensemble, ces skills ne sont pas des raccourcis isolés : ils encodent une **méthode de travail**.

---

## Les Skills

| Skill | Ce qu'il fait | Ce qu'il produit |
|-------|---------------|------------------|
| `/interroge` | Te questionne une question à la fois, descend l'arbre de décision, recommande avec justification | Une compréhension partagée |
| `/cadre` | Cadre le projet par questionnement et rédige un PRD en 8 sections | `docs/PRD.md` |
| `/planifie` | Découpe le PRD en phases livrables par tranches verticales (tracer bullets) | `docs/PLAN.md` |
| `/design` | Propose un système de design opinioné (typo, couleurs, layout, motion) | `docs/DESIGN.md` + preview HTML |
| `/investigue` | Investigue un bug en 4 phases validées, sans jamais corriger à la volée | Un fix minimal validé |
| `/illustre` | Crée des diagrammes et visuels Excalidraw (process, schémas, slides) | PNG (2x) + SVG |
| `/branche` | Crée une branche depuis main à jour, avec préfixe conventionnel `feat/` ou `fix/` | Une branche de travail isolée |
| `/livre` | Commit, synchronise avec main distant, push et ouvre une PR (refuse sur main) | Une Pull Request |

---

## La Formation

<p align="center">
  <img src="assets/hero.png" alt="Claude Mastery — L'Accélérateur IA" width="640">
</p>

Ces skills sont la version outillée de ce qu'on enseigne dans **Claude Mastery**, la formation de **L'Accélérateur IA** pour construire avec Claude Code. La même méthode — cadrer, planifier, designer, livrer — appliquée à de vrais projets.

👉 **[Découvrir la formation Claude Mastery](https://laccelerateuria.com)**

