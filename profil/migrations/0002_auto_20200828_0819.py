# Generated by Django 2.2.15 on 2020-08-28 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profil',
            old_name='priv_donate',
            new_name='last_donation',
        ),
    ]
