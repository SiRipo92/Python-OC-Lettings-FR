## Résumé
![CI/CD Pipeline](https://github.com/SiRipo92/Python-OC-Lettings-FR/actions/workflows/ci-cd.yml/badge.svg)

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

## Déploiement

### Fonctionnement général

Le déploiement est entièrement automatisé via un pipeline CI/CD GitHub Actions. Le pipeline fonctionne comme suit :

- **Toutes les branches** : à chaque push, le pipeline exécute le linting (`flake8`) et les tests (`pytest`) avec vérification que la couverture de test est supérieure à 80%.
- **Branche master uniquement** : si les tests passent, une image Docker est construite et poussée sur Docker Hub avec deux tags — le hash du commit et `latest`. Si la conteneurisation réussit, le déploiement sur Render est déclenché automatiquement via un webhook.

### Prérequis pour le déploiement

Vous aurez besoin des comptes et accès suivants :

- **GitHub** : repository avec accès en écriture
- **Docker Hub** : compte avec un repository public `oc-lettings`
- **Render** : compte avec un Web Service configuré pour utiliser l'image Docker Hub
- **Sentry** : projet Django configuré

### Configuration requise

#### GitHub Secrets

Ajoutez ces secrets dans votre repository GitHub (Settings → Secrets and variables → Actions) :

| Secret | Description |
|--------|-------------|
| `SECRET_KEY` | Clé secrète Django |
| `SENTRY_DSN` | DSN de votre projet Sentry |
| `DOCKERHUB_USERNAME` | Votre nom d'utilisateur Docker Hub |
| `DOCKERHUB_TOKEN` | Token d'accès Docker Hub (Read & Write) |
| `RENDER_DEPLOY_HOOK_URL` | URL du deploy hook Render (voir ci-dessous) |

#### Render

1. Créez un compte sur [render.com](https://render.com)
2. Créez un nouveau **Web Service** → **Existing Image**
3. Entrez l'URL de l'image : `docker.io/YOUR_DOCKERHUB_USERNAME/oc-lettings:latest`
4. Ajoutez les variables d'environnement suivantes dans Render :
   - `SECRET_KEY` : votre clé secrète Django
   - `DEBUG` : `False`
   - `ALLOWED_HOSTS` : votre URL Render (ex: `your-app.onrender.com`)
   - `SENTRY_DSN` : votre DSN Sentry
5. **Désactivez le déploiement automatique** dans les paramètres Render — les déploiements sont déclenchés uniquement par GitHub Actions
6. Dans Settings → **Deploy Hook**, copiez l'URL et ajoutez-la comme secret `RENDER_DEPLOY_HOOK_URL` dans GitHub

### Étapes pour déployer

1. Créez une branche feature et faites vos modifications
2. Poussez la branche — le pipeline exécute les tests automatiquement
3. Ouvrez une Pull Request et mergez dans `master`
4. Le pipeline se déclenche automatiquement :
   - Tests et linting
   - Build et push de l'image Docker sur Docker Hub
   - Déclenchement du déploiement sur Render
5. Vérifiez le déploiement sur votre URL Render

### Récupérer et lancer l'image Docker localement

Pour récupérer et lancer l'image depuis Docker Hub sans cloner le repository :

```bash
docker pull YOUR_DOCKERHUB_USERNAME/oc-lettings:latest
docker run -p 8000:8000 \
  -e SECRET_KEY='your-secret-key' \
  -e DEBUG=True \
  -e ALLOWED_HOSTS=localhost,127.0.0.1 \
  -e SENTRY_DSN=your-sentry-dsn \
  YOUR_DOCKERHUB_USERNAME/oc-lettings:latest
```

Puis ouvrez `http://localhost:8000` dans votre navigateur.
