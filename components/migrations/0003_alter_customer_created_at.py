# Generated by Django 4.1.4 on 2022-12-28 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0002_alter_customer_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
