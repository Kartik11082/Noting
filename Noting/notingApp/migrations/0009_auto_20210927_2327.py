# Generated by Django 3.1.6 on 2021-09-27 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notingApp', '0008_auto_20210927_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notingmodel',
            name='title',
            field=models.TextField(null=True),
        ),
    ]
