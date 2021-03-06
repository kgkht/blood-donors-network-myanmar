# Generated by Django 2.2.15 on 2020-08-25 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Region/Division.', max_length=30, verbose_name='Region/Division')),
            ],
        ),
        migrations.CreateModel(
            name='Township',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter City/Township.', max_length=30, verbose_name='Township')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Region.Division')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Region.Township')),
            ],
        ),
    ]
