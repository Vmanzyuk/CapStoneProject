# Generated by Django 2.1.2 on 2018-10-08 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TokensDB', '0003_auto_20181008_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='cmc_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
