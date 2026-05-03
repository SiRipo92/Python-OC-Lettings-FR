Structure de la base de données
================================

L'application utilise SQLite3 avec l'ORM Django. Les modèles sont répartis dans deux applications.

Application ``lettings``
------------------------

**Address**

Représente une adresse physique associée à une location.

.. list-table::
   :header-rows: 1

   * - Champ
     - Type
     - Contraintes
   * - ``number``
     - PositiveIntegerField
     - max 9999
   * - ``street``
     - CharField
     - max 64 caractères
   * - ``city``
     - CharField
     - max 64 caractères
   * - ``state``
     - CharField
     - exactement 2 caractères
   * - ``zip_code``
     - PositiveIntegerField
     - max 99999
   * - ``country_iso_code``
     - CharField
     - exactement 3 caractères

**Letting**

Représente une propriété à louer.

.. list-table::
   :header-rows: 1

   * - Champ
     - Type
     - Contraintes
   * - ``title``
     - CharField
     - max 256 caractères
   * - ``address``
     - OneToOneField → Address
     - CASCADE

Application ``profiles``
------------------------

**Profile**

Représente le profil étendu d'un utilisateur Django.

.. list-table::
   :header-rows: 1

   * - Champ
     - Type
     - Contraintes
   * - ``user``
     - OneToOneField → User
     - CASCADE
   * - ``favorite_city``
     - CharField
     - max 64 caractères, optionnel

Relations
---------

- Chaque ``Letting`` est lié à exactement une ``Address`` (OneToOne)
- Chaque ``Profile`` est lié à exactement un ``User`` Django (OneToOne)

Ajouter des données via le shell Django
----------------------------------------

.. code-block:: bash

   python manage.py shell

.. code-block:: python

   from lettings.models import Address, Letting

   address = Address.objects.create(
       number=123, street='Rue de la Paix', city='Paris',
       state='IL', zip_code=75001, country_iso_code='FRA'
   )
   Letting.objects.create(title='Parisian Studio', address=address)

.. code-block:: python

   from django.contrib.auth.models import User
   from profiles.models import Profile

   user = User.objects.create_user(username='newuser', password='Pass123!')
   Profile.objects.create(user=user, favorite_city='Lyon')
