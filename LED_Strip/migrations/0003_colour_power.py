# Generated by Django 3.1.2 on 2021-03-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LED_Strip', '0002_colour_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='colour',
            name='power',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
