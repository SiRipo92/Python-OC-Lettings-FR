Interfaces de programmation
============================

L'application expose des URLs qui mappent vers des vues Django retournant des pages HTML.

URLs — ``oc_lettings_site``
----------------------------

Point d'entrée racine (``ROOT_URLCONF``).

.. list-table::
   :header-rows: 1

   * - URL
     - Vue
     - Nom
     - Description
   * - ``/``
     - ``oc_lettings_site.views.index``
     - ``index``
     - Page d'accueil
   * - ``/lettings/``
     - inclus depuis ``lettings.urls``
     - —
     - URLs de l'application lettings
   * - ``/profiles/``
     - inclus depuis ``profiles.urls``
     - —
     - URLs de l'application profiles
   * - ``/admin/``
     - Django Admin
     - —
     - Interface d'administration

URLs — ``lettings``
--------------------

Namespace : ``lettings``

.. list-table::
   :header-rows: 1

   * - URL
     - Vue
     - Nom
     - Description
   * - ``/lettings/``
     - ``lettings.views.index``
     - ``lettings:index``
     - Liste de toutes les locations
   * - ``/lettings/<id>/``
     - ``lettings.views.letting``
     - ``lettings:letting``
     - Détail d'une location

URLs — ``profiles``
--------------------

Namespace : ``profiles``

.. list-table::
   :header-rows: 1

   * - URL
     - Vue
     - Nom
     - Description
   * - ``/profiles/``
     - ``profiles.views.index``
     - ``profiles:index``
     - Liste de tous les profils
   * - ``/profiles/<username>/``
     - ``profiles.views.profile``
     - ``profiles:profile``
     - Détail d'un profil

Gestion des erreurs
--------------------

.. list-table::
   :header-rows: 1

   * - Erreur
     - Vue
     - Template
   * - 404 — Page introuvable
     - ``oc_lettings_site.views.error_404``
     - ``404.html``
   * - 500 — Erreur serveur
     - ``oc_lettings_site.views.error_500``
     - ``500.html``
