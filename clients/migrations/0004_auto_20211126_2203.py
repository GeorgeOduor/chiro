# Generated by Django 3.1.3 on 2021-11-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20211126_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_clients',
            name='AccountNumber',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
