# Generated by Django 2.2.1 on 2019-05-16 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_auto_20190516_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='Comment_ID',
        ),
        migrations.RemoveField(
            model_name='movies',
            name='Movie_ID',
        ),
        migrations.AddField(
            model_name='comments',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
