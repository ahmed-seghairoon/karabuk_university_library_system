# Generated by Django 4.2.13 on 2024-06-08 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_book_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='uuid',
        ),
    ]
