# Generated by Django 5.1.4 on 2025-02-04 08:49

import BusinessPartner.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessPartner', '0005_remove_businesspartner_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesspartner',
            name='alternate_mobile',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, validators=[BusinessPartner.models.validate_mobile_no]),
        ),
        migrations.AlterField(
            model_name='businesspartner',
            name='business_email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='businesspartner',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='businesspartner',
            name='mobile',
            field=models.CharField(max_length=15, unique=True, validators=[BusinessPartner.models.validate_mobile_no], verbose_name='Mobile No'),
        ),
    ]
