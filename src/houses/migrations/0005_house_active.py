# Generated by Django 4.0.4 on 2022-05-13 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0004_house_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Активен'),
        ),
    ]