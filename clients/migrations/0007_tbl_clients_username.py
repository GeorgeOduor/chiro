# Generated by Django 3.1.3 on 2021-11-28 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0006_auto_20211128_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_clients',
            name='Username',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
