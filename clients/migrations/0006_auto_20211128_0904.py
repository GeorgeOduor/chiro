# Generated by Django 3.1.3 on 2021-11-28 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_tbl_clients_amounteligible'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_clients',
            name='BusinessName',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='tbl_clients',
            name='ClientType',
            field=models.CharField(choices=[('C', 'Client'), ('L', 'Lender'), ('S', 'Service provider')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]