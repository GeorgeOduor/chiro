# Generated by Django 3.1.3 on 2021-11-24 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_TrxAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccountID', models.CharField(max_length=12)),
                ('TransactionType', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], max_length=10)),
                ('TrxDate', models.DateTimeField(auto_now_add=True)),
                ('TrxNarration', models.TextField(max_length=5000)),
                ('Amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('TrxTypeID', models.CharField(choices=[('TC', 'TC'), ('TD', 'TD'), ('CC', 'CC')], max_length=2)),
                ('ClientType', models.CharField(choices=[('C', 'Client'), ('L', 'Lender'), ('S', 'Service provider')], max_length=2)),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
    ]