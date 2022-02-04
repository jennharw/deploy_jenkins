# Generated by Django 3.1.3 on 2022-01-06 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20220106_0240'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='쇼핑몰')),
                ('productOptionGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productoptiongroup')),
            ],
        ),
    ]
