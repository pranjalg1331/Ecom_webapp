# Generated by Django 4.2.3 on 2023-09-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_remove_profile_is_authenticated_remove_profile_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='token',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
