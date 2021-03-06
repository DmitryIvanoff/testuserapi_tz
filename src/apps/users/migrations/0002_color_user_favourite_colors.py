# Generated by Django 4.0.3 on 2022-04-01 20:39

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, primary_key=True, samples=None, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='favourite_colors',
            field=models.ManyToManyField(blank=True, related_name='users', to='users.color'),
        ),
    ]
