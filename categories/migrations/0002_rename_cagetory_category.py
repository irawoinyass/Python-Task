# Generated by Django 4.0.10 on 2023-04-12 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cagetory',
            new_name='Category',
        ),
    ]
