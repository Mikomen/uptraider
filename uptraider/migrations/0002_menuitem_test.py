# Generated by Django 3.2.24 on 2024-02-09 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uptraider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='test',
            field=models.ManyToManyField(blank=True, null=True, related_name='_uptraider_menuitem_test_+', to='uptraider.MenuItem'),
        ),
    ]
