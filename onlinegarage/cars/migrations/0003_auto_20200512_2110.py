# Generated by Django 3.0.6 on 2020-05-13 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20200512_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='pub_date',
            field=models.DateField(auto_now_add=True, verbose_name='Published'),
        ),
    ]
