# Generated by Django 3.1.6 on 2021-09-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notingApp', '0003_auto_20210927_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notingmodel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='notingmodel',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
