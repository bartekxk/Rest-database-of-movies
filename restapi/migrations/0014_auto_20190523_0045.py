# Generated by Django 2.2.1 on 2019-05-23 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0013_auto_20190523_0042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='ID',
            new_name='id',
        ),
    ]
