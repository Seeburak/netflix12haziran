# Generated by Django 4.2.8 on 2024-01-28 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0009_alter_video_profilsec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='profilsec',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appUser.profile'),
        ),
    ]
