# Generated by Django 4.2.7 on 2023-11-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_salemodel_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='salemodel',
            name='value_sale',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total'),
        ),
    ]
