# Generated by Django 3.1.6 on 2021-09-28 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notingApp', '0010_auto_20210928_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notingmodel',
            old_name='id',
            new_name='noteID',
        ),
    ]
