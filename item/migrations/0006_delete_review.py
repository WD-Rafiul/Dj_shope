# Generated by Django 4.2.6 on 2024-01-22 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_alter_review_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]