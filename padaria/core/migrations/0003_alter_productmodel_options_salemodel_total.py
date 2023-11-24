# Generated by Django 4.2.7 on 2023-11-24 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_salemodel_order_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productmodel',
            options={'ordering': ['id'], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AddField(
            model_name='salemodel',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total'),
        ),
    ]
