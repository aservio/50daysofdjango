# Generated by Django 5.1.1 on 2024-11-14 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='pors',
            new_name='post',
        ),
    ]
