# Generated by Django 3.0.6 on 2020-05-11 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model_garden', '0010_auto_20200506_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediaasset',
            name='dataset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_assets', to='model_garden.Dataset'),
        ),
    ]