# Generated by Django 3.2.6 on 2021-09-04 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0011_user_avatarurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liking', models.IntegerField()),
                ('liked', models.IntegerField()),
            ],
        ),
    ]