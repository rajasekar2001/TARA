# Generated by Django 5.1.4 on 2025-02-04 09:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_resuser_email_id_alter_resuser_mobile_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resuser',
            name='email_id',
            field=models.EmailField(max_length=254, null=True, unique=True, validators=[django.core.validators.EmailValidator(message='Enter a valid email address.')], verbose_name='Email ID'),
        ),
    ]
