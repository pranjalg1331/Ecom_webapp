# Generated by Django 4.2.5 on 2023-10-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_cart_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('expiry_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total_price',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.SmallIntegerField(default=1),
        ),
    ]
