from django.db import migrations

class Migration(migrations.Migration):

    initial = False

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
        ('lettings', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(name='Letting'),
        migrations.DeleteModel(name='Address'),
        migrations.DeleteModel(name='Profile'),
    ]
