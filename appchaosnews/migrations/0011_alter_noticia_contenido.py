# Generated by Django 5.0.6 on 2024-06-08 00:07

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appchaosnews', '0010_alter_comentario_contenido_alter_noticia_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='contenido',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='contenido'),
        ),
    ]
