# Generated by Django 2.2.15 on 2020-08-28 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='id',
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Region.Address'),
        ),
    ]
