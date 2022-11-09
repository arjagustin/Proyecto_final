# Generated by Django 4.1.1 on 2022-11-08 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_autor_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Categorias', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'categorías',
            },
        ),
        migrations.DeleteModel(
            name='seccion',
        ),
        migrations.RenameField(
            model_name='autor',
            old_name='apodo',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='profecion',
        ),
    ]
