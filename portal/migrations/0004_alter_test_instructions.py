# Generated by Django 5.0.1 on 2024-01-16 19:16

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_excelfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='instructions',
            field=tinymce.models.HTMLField(default=''),
        ),
    ]
