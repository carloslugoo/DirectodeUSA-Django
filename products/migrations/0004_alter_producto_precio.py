# Generated by Django 4.2.1 on 2024-02-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_actualizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.CharField(default='0', max_length=8),
        ),
    ]
