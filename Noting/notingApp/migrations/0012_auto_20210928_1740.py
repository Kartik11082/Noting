# Generated by Django 3.1.6 on 2021-09-28 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notingApp', '0011_auto_20210928_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notingmodel',
            name='date_posted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]