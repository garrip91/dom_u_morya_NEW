# Generated by Django 4.0.4 on 2022-05-06 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_alter_house_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='houses/photos', verbose_name='Фотография'),
        ),
    ]