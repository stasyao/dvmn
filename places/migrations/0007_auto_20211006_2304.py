# Generated by Django 3.2.7 on 2021-10-06 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_image_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('priority',)},
        ),
        migrations.AlterField(
            model_name='image',
            name='priority',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
