# Generated by Django 5.1.1 on 2024-10-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipos', '0002_tipomaestro_in_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipomaestro',
            name='in_main',
            field=models.BooleanField(default=False, verbose_name='En Main'),
        ),
    ]
