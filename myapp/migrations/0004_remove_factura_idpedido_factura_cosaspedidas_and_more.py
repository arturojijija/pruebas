# Generated by Django 5.0.3 on 2024-05-21 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_pedido_nota_pedido_numeropedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='idPedido',
        ),
        migrations.AddField(
            model_name='factura',
            name='cosasPedidas',
            field=models.CharField(default=2, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='factura',
            name='fecha',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='hora',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
