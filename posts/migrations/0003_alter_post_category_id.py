# Generated by Django 4.0.10 on 2023-04-15 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_category_id_alter_post_posted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category_id',
            field=models.IntegerField(),
        ),
    ]
