# Generated by Django 4.2.2 on 2023-10-09 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppKeto', '0006_alter_producto_fotos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fotos',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]
