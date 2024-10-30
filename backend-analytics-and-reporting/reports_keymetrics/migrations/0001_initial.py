# Generated by Django 5.1.2 on 2024-10-29 06:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_first_name', models.CharField(max_length=30)),
                ('user_middle_name', models.CharField(blank=True, max_length=30)),
                ('user_last_name', models.CharField(max_length=30)),
                ('user_dob', models.DateField()),
                ('user_phone_number', models.BigIntegerField()),
                ('user_country', models.CharField(max_length=50)),
                ('user_city', models.CharField(max_length=50)),
                ('user_address_line_1', models.CharField(max_length=255)),
                ('user_address_line_2', models.CharField(max_length=255)),
                ('user_pin_code', models.BigIntegerField()),
                ('user_state', models.CharField(max_length=50)),
                ('user_profile_photo', models.CharField(blank=True, max_length=255, null=True)),
                ('user_password', models.CharField(max_length=255)),
                ('user_type', models.CharField(default='customer', max_length=50)),
                ('user_old_password', models.CharField(blank=True, max_length=128, null=True)),
                ('user_joined_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('last_login', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('users_daily_limit', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('users_monthly_limit', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]