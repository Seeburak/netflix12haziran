# Generated by Django 4.2 on 2024-01-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0003_profile_isnew'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='islogin',
            field=models.BooleanField(default=False, verbose_name='Girişli Profil'),
        ),
    ]
