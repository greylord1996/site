# Generated by Django 2.0.4 on 2018-05-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_good_add_from_administration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='add_from_administration',
            field=models.BooleanField(db_index=True, default=False, verbose_name='Из админки'),
        ),
    ]
