# Generated by Django 5.0.6 on 2024-06-17 15:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('dateOfBirth', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phoneNumber', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='El número de celular solo debe contener dígitos.', regex='^\\d+$')])),
            ],
        ),
    ]
