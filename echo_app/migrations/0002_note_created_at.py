# Generated by Django 5.0 on 2023-12-21 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('echo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
