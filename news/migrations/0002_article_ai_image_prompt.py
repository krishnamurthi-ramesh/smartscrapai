# Generated by Django 5.1.7 on 2025-03-30 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='ai_image_prompt',
            field=models.TextField(blank=True, null=True),
        ),
    ]
