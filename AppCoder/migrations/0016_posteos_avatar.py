# Generated by Django 4.0.4 on 2022-06-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0015_posteos_rename_perfil_perfiles_delete_posteo'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteos',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
    ]
