# Generated by Django 4.2.7 on 2024-01-14 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_postmodel_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='post/media/images/'),
        ),
    ]
