# Generated by Django 4.1.3 on 2023-01-05 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='print',
            new_name='price',
        ),
    ]
