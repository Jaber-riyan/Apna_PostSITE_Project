# Generated by Django 4.2.7 on 2024-01-15 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0024_postmodel_post_dislike_postmodel_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
