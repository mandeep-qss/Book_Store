# Generated by Django 3.2.3 on 2021-06-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
