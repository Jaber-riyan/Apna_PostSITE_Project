# Generated by Django 4.2.7 on 2024-01-15 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0019_remove_postmodel_like_unlike_postmodel_like_dislike_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likedislikemodel',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='postmodel',
            name='like_dislike',
        ),
        migrations.AddField(
            model_name='likedislikemodel',
            name='post',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.postmodel'),
        ),
    ]
