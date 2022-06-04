# Generated by Django 4.0.4 on 2022-06-03 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_delete_perfil_delete_posteo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('contraseña', models.IntegerField()),
                ('linkDeInteres', models.SlugField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Posteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=150)),
                ('subtitulo', models.CharField(max_length=150)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=150)),
            ],
        ),
    ]
