# Generated by Django 3.1.3 on 2021-11-27 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20211126_2203'),
        ('core', '0005_auto_20211127_1817'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='tbl_TrxAccounts',
            new_name='tbl_Transactions',
        ),
    ]