# Generated by Django 5.1.4 on 2025-02-02 15:02

import BusinessPartner.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessPartner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businesspartnerkyc',
            name='aadhar_no_2',
        ),
        migrations.AddField(
            model_name='businesspartnerkyc',
            name='aadhar_no_back',
            field=models.ImageField(blank=True, null=True, upload_to='kyc/aadhar/'),
        ),
        migrations.AddField(
            model_name='businesspartnerkyc',
            name='aadhar_no_front',
            field=models.ImageField(blank=True, null=True, upload_to='kyc/aadhar/'),
        ),
        migrations.AlterField(
            model_name='businesspartner',
            name='alternate_mobile',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[BusinessPartner.models.validate_mobile_no]),
        ),
        migrations.AlterField(
            model_name='businesspartner',
            name='mobile',
            field=models.CharField(max_length=15, validators=[BusinessPartner.models.validate_mobile_no], verbose_name='Mobile No'),
        ),
        migrations.AlterField(
            model_name='businesspartnerkyc',
            name='gst_no',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[BusinessPartner.models.validate_gst_number]),
        ),
        migrations.AlterField(
            model_name='businesspartnerkyc',
            name='pan_no',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[BusinessPartner.models.validate_pan_number]),
        ),
    ]
