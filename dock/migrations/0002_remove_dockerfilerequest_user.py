# Generated by Django 4.2.19 on 2025-06-09 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dock', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dockerfilerequest',
            name='user',
        ),
    ]
