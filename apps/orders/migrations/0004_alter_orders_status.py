# Generated by Django 5.1.5 on 2025-01-18 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_orders_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('WAIT', 'В ожидании'), ('DONE', 'Готово'), ('PAID', 'Оплачено')], default='WAIT'),
        ),
    ]
