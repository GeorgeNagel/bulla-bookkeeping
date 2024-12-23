# Generated by Django 5.1.4 on 2024-12-23 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_add_top_level_accounts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ledger.account'),
        ),
    ]