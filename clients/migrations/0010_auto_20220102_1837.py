# Generated by Django 3.1.3 on 2022-01-02 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_tbl_clients_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_clients',
            old_name='Username',
            new_name='user',
        ),
    ]