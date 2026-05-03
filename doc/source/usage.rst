Guide d'utilisation
====================

Navigation sur le site
-----------------------

Le site est accessible à l'adresse : https://oc-lettings-latest-ww0k.onrender.com

**Page d'accueil** — ``/``

Point d'entrée du site avec des liens vers les sections Locations et Profils.

**Liste des locations** — ``/lettings/``

Affiche toutes les propriétés disponibles à la location.

**Détail d'une location** — ``/lettings/<id>/``

Affiche les informations détaillées d'une propriété : titre et adresse complète.

**Liste des profils** — ``/profiles/``

Affiche tous les profils utilisateurs enregistrés.

**Détail d'un profil** — ``/profiles/<username>/``

Affiche les informations d'un utilisateur : nom d'utilisateur, email, ville favorite.

Panel d'administration
-----------------------

Accessible à ``/admin/`` avec les identifiants administrateur.

Permet de :

- Créer, modifier et supprimer des locations et adresses
- Créer, modifier et supprimer des profils utilisateurs
- Gérer les comptes utilisateurs Django

Vérification de Sentry
-----------------------

Pour vérifier que Sentry capture correctement les erreurs, accédez à une location inexistante :

.. code-block:: bash

   https://oc-lettings-latest-ww0k.onrender.com/lettings/999/

L'erreur 404 doit apparaître dans le dashboard Sentry sous quelques secondes.

Cas d'utilisation typiques
---------------------------

**Consulter les locations disponibles**

1. Ouvrir le site sur ``/``
2. Cliquer sur « Lettings »
3. Sélectionner une propriété pour voir son adresse complète

**Consulter un profil utilisateur**

1. Ouvrir le site sur ``/``
2. Cliquer sur « Profiles »
3. Sélectionner un utilisateur pour voir sa ville favorite

**Ajouter une nouvelle location (administrateur)**

1. Se connecter sur ``/admin/``
2. Aller dans « Lettings » → « Add Letting »
3. Renseigner le titre et créer ou sélectionner une adresse
