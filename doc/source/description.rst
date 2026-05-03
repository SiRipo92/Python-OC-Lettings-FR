Description du projet
=====================

OC Lettings est une application web développée avec le framework Django pour la startup américaine **Orange County Lettings**, spécialisée dans la location de biens immobiliers.

La version 2.0 constitue une refonte complète de l'architecture de la version originale. L'application monolithique a été décomposée en une architecture modulaire, accompagnée d'un pipeline CI/CD, d'une surveillance des erreurs via Sentry, et d'un déploiement automatisé sur Render.

Objectifs de la version 2.0
-----------------------------

- Refonte de l'architecture modulaire (séparation en applications distinctes)
- Réduction de la dette technique (linting, tests, docstrings, gestion des erreurs)
- Surveillance de l'application et suivi des erreurs via Sentry
- Mise en place d'un pipeline CI/CD avec déploiement automatisé
- Création de cette documentation technique

Applications
------------

L'application est composée de trois modules Django :

- **oc_lettings_site** : point d'entrée du projet, gère la page d'accueil et les erreurs globales (404, 500)
- **lettings** : gestion des propriétés à louer et de leurs adresses
- **profiles** : gestion des profils utilisateurs
