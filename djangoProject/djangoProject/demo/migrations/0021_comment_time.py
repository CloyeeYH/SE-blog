# Generated by Django 3.2.6 on 2021-09-09 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0020_comment_towhich'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]