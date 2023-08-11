# Generated by Django 4.2.2 on 2023-08-10 12:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_userfollows'),
        ('authentication', '0006_remove_user_follows'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(through='blog.UserFollows', to=settings.AUTH_USER_MODEL),
        ),
    ]