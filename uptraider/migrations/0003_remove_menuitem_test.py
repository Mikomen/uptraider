# Generated by Django 3.2.24 on 2024-02-09 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uptraider', '0002_menuitem_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='test',
        ),
    ]