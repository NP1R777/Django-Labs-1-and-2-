# Generated by Django 5.2 on 2025-04-15 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app1', '0003_authuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_products', models.JSONField(default=list)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app1.user')),
            ],
            options={
                'db_table': 'basket',
            },
        ),
    ]
