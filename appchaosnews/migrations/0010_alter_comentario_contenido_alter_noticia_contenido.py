# Generated by Django 5.0.6 on 2024-06-07 23:04

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appchaosnews', '0009_alter_comentario_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='contenido',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='contenido',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]
