# Generated by Django 2.2 on 2020-01-01 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo_item',
            new_name='Item',
        ),
        migrations.RenameModel(
            old_name='Todo_list',
            new_name='List',
        ),
    ]
