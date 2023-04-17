# Generated by Django 4.1.7 on 2023-04-17 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_post_updated_at_alter_post_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="file_upload",
            field=models.FileField(blank=True, upload_to="blog/files/%Y/%m/%d"),
        ),
        migrations.AddField(
            model_name="post",
            name="head_image",
            field=models.ImageField(blank=True, upload_to="blog/images/%Y/%m/%d"),
        ),
        migrations.AddField(
            model_name="post",
            name="hook_text",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
