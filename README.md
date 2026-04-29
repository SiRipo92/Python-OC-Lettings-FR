## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv .venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source .venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source .venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source .venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source .venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  oc_lettings_site_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Variables d'environnement

L'application utilise des variables d'environnement pour les données sensibles. Créez un fichier `.env` à la racine du projet avec les variables suivantes :

```
SECRET_KEY='your-secret-key'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
SENTRY_DSN=your-sentry-dsn
```

- `SECRET_KEY` : clé secrète Django. Générez-en une avec `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`
- `DEBUG` : `True` en développement, `False` en production
- `ALLOWED_HOSTS` : liste des hôtes autorisés, séparés par des virgules
- `SENTRY_DSN` : DSN fourni par votre projet Sentry (voir section ci-dessous)

Ne commitez jamais le fichier `.env` — il est listé dans `.gitignore`.

## Surveillance et suivi des erreurs (Sentry)

L'application utilise [Sentry](https://sentry.io) pour la surveillance des erreurs et la journalisation.

### Configuration

1. Créez un compte sur [sentry.io](https://sentry.io) et créez un nouveau projet en choisissant **Django** comme plateforme
2. Copiez le DSN fourni par Sentry
3. Ajoutez-le à votre fichier `.env` : `SENTRY_DSN=your-dsn-here`
4. Sentry est initialisé automatiquement au démarrage via `settings.py`

### Journalisation

Les logs sont configurés dans `settings.py` et s'affichent dans la console. Les événements suivants sont enregistrés :

- Accès aux pages de détail d'une location (`INFO`)
- Accès aux pages de détail d'un profil (`INFO`)
- Erreurs 404 (`WARNING`)
- Erreurs 500 (`ERROR`)
- Ressources introuvables dans la base de données (`ERROR`)

### Vérification

Pour vérifier que Sentry capture bien les erreurs, provoquez une erreur délibérée en accédant à une location inexistante :

```
http://localhost:8000/lettings/999/
```

L'erreur doit apparaître dans votre dashboard Sentry sous quelques secondes.
