Déploiement et gestion
=======================

Fonctionnement général
-----------------------

Le déploiement est entièrement automatisé via un pipeline CI/CD GitHub Actions :

- **Toutes les branches** : linting (``flake8``) + tests (``pytest``) avec couverture ≥ 80%
- **Branche master uniquement** : build et push de l'image Docker sur Docker Hub, puis déploiement sur Render via webhook

Pipeline CI/CD
--------------

.. code-block:: yaml

   test  →  docker  →  deploy
   (all)    (master)   (master)

Configuration requise
---------------------

**GitHub Secrets**

.. list-table::
   :header-rows: 1

   * - Secret
     - Description
   * - ``SECRET_KEY``
     - Clé secrète Django
   * - ``SENTRY_DSN``
     - DSN du projet Sentry
   * - ``DOCKERHUB_USERNAME``
     - Nom d'utilisateur Docker Hub
   * - ``DOCKERHUB_TOKEN``
     - Token d'accès Docker Hub (Read & Write)
   * - ``RENDER_DEPLOY_HOOK_URL``
     - URL du deploy hook Render

**Variables d'environnement Render**

.. list-table::
   :header-rows: 1

   * - Variable
     - Valeur
   * - ``SECRET_KEY``
     - Clé secrète Django
   * - ``DEBUG``
     - ``False``
   * - ``ALLOWED_HOSTS``
     - ``your-app.onrender.com``
   * - ``SENTRY_DSN``
     - DSN Sentry

Étapes pour déployer
---------------------

1. Créer une branche feature et effectuer les modifications
2. Pousser la branche — le pipeline exécute les tests automatiquement
3. Ouvrir une Pull Request et merger dans ``master``
4. Le pipeline se déclenche :

   - Tests et linting
   - Build et push de l'image Docker (tags : commit SHA + ``latest``)
   - Déclenchement du déploiement sur Render

5. Vérifier le déploiement sur l'URL Render

Récupérer et lancer l'image Docker localement
----------------------------------------------

.. code-block:: bash

   docker pull siripo92/oc-lettings:latest
   docker run -p 8000:8000 \
     -e SECRET_KEY='your-secret-key' \
     -e DEBUG=True \
     -e ALLOWED_HOSTS=localhost,127.0.0.1 \
     -e SENTRY_DSN=your-sentry-dsn \
     siripo92/oc-lettings:latest

Ouvrez ``http://localhost:8000``.

Surveillance des erreurs
-------------------------

Les erreurs sont capturées automatiquement par Sentry. Consultez le dashboard sur
`sentry.io <https://sentry.io>`_ pour visualiser les erreurs et les logs de l'application.
