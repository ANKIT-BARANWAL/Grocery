# Generated by Django 2.2.19 on 2021-02-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0002_auto_20210223_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='grocery',
            name='item_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
