# Generated by Django 4.1.1 on 2022-10-12 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_seccion_options"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="usuario",
            new_name="Autor",
        ),
        migrations.AlterModelOptions(
            name="autor",
            options={"verbose_name_plural": "Autores"},
        ),
    ]