# Generated by Django 4.0 on 2022-02-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0003_auto_20220123_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]