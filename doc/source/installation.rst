Installation
============

Prérequis
---------

- Python 3.11 ou supérieur
- Git
- SQLite3
- Docker (optionnel, pour lancer via image)

Cloner le repository
--------------------

.. code-block:: bash

   git clone https://github.com/SiRipo92/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR

Créer et activer l'environnement virtuel
-----------------------------------------

.. code-block:: bash

   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # ou
   .venv\Scripts\Activate.ps1  # Windows

Installer les dépendances
--------------------------

.. code-block:: bash

   pip install -r requirements.txt

Configurer les variables d'environnement
-----------------------------------------

Créez un fichier ``.env`` à la racine du projet :

.. code-block:: bash

   SECRET_KEY='your-secret-key'
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   SENTRY_DSN=your-sentry-dsn

Pour générer une clé secrète Django :

.. code-block:: bash

   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Appliquer les migrations
-------------------------

.. code-block:: bash

   python manage.py migrate
