# Generated by Django 5.1.4 on 2025-01-10 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mvp', '0005_comment_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='nickname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]