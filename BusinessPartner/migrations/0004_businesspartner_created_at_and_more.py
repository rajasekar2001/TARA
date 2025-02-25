# Generated by Django 5.1.4 on 2025-02-04 07:08

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BusinessPartner', '0003_rename_aadhar_no_back_businesspartnerkyc_aadhar_back_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='businesspartner',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='businesspartner',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_partners', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='businesspartner',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
