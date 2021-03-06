# Generated by Django 2.1.2 on 2018-10-08 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TokensDB', '0002_auto_20181002_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='logo_link',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='based_on_blockchain',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='circulating_supply',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='cmc_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='explorer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='max_supply',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='reddit',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='total_supply',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='twitter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='token',
            name='website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
