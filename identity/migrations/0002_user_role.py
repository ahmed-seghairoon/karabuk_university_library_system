# Generated by Django 5.0.6 on 2024-06-08 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('student', 'student'), ('admin', 'admin')], max_length=256, null=True),
        ),
    ]
