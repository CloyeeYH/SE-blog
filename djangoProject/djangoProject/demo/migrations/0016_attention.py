# Generated by Django 3.2.6 on 2021-09-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0015_auto_20210904_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liking', models.IntegerField(default=0)),
                ('liked', models.IntegerField(default=0)),
            ],
        ),
    ]