# Generated by Django 3.1.6 on 2021-09-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notingApp', '0013_auto_20210928_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notingmodel',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]