# Generated by Django 2.2.13 on 2022-05-31 03:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]