# Generated by Django 4.2.7 on 2023-11-24 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_productmodel_options_salemodel_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salemodel',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordereds', to='core.clientmodel', verbose_name='Cliente'),
        ),
    ]