# Generated by Django 5.0.7 on 2024-10-14 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skinserver', '0009_alter_history_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='image',
        ),
    ]
