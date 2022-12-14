# Generated by Django 4.1.1 on 2022-10-12 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_rename_usuario_autor_alter_autor_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="autor",
            name="edad",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="autor",
            name="profecion",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="seccion",
            name="fecha_de_creacion",
            field=models.DateField(null=True),
        ),
    ]
