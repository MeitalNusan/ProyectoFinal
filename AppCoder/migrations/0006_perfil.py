# Generated by Django 4.0.4 on 2022-06-02 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_delete_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('contraseña', models.IntegerField()),
                ('link', models.SlugField(max_length=150)),
                ('descripcion', models.CharField(max_length=150)),
            ],
        ),
    ]