# Generated by Django 4.1 on 2022-08-09 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_rename_autor_articulo_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='articulo',
            old_name='message',
            new_name='mensaje',
        ),
        migrations.RenameField(
            model_name='articulo',
            old_name='title',
            new_name='titulo',
        ),
    ]