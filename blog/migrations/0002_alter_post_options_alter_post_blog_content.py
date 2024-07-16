# Generated by Django 4.1.4 on 2024-07-16 08:19

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='post',
            name='blog_content',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
