# Generated by Django 2.2.15 on 2020-08-28 08:14

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizar', '0002_auto_20200828_0221'),
        ('Region', '0002_auto_20200827_0713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Enter Full Name', max_length=50, verbose_name='Your Name')),
                ('photo', models.ImageField(blank=True, upload_to='images/profile', verbose_name='Profile Picture')),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('blood', models.CharField(choices=[('AMNS', 'A -'), ('APLS', 'A +'), ('BMNS', 'B -'), ('BPLS', 'B +'), ('ABMS', 'AB -'), ('ABPS', 'AB +'), ('OMNS', 'O -'), ('OPLS', 'O +')], default='', help_text='Choose Blood Type', max_length=4, verbose_name='Blood Type')),
                ('priv_donate', models.DateField(blank=True, null=True, verbose_name='Donation Date')),
                ('address', models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='Region.Address')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizar.Organization')),
            ],
        ),
    ]
