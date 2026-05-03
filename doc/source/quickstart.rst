Guide de démarrage rapide
=========================

Lancer le serveur local
------------------------

.. code-block:: bash

   source .venv/bin/activate
   python manage.py runserver

Ouvrez ``http://localhost:8000`` dans votre navigateur.

Accéder au panel d'administration
-----------------------------------

.. code-block:: bash

   http://localhost:8000/admin

Connectez-vous avec :

- **Utilisateur** : ``admin``
- **Mot de passe** : ``Abc1234!``

Lancer les tests
-----------------

.. code-block:: bash

   pytest

Vérifier la couverture de test
--------------------------------

.. code-block:: bash

   pytest --cov=. --cov-report=term-missing

Lancer le linting
------------------

.. code-block:: bash

   python -m flake8

Lancer via Docker
------------------

.. code-block:: bash

   docker pull siripo92/oc-lettings:latest
   docker run -p 8000:8000 \
     -e SECRET_KEY='your-secret-key' \
     -e DEBUG=True \
     -e ALLOWED_HOSTS=localhost,127.0.0.1 \
     -e SENTRY_DSN=your-sentry-dsn \
     siripo92/oc-lettings:latest

Ouvrez ``http://localhost:8000`` dans votre navigateur.
