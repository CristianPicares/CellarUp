# Generated by Django 4.1 on 2022-12-13 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='ubicacion',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='marcaProducto',
            field=models.CharField(max_length=10),
        ),
    ]
