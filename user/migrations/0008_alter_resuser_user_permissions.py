# Generated by Django 5.1.5 on 2025-03-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0007_rename_delete_resuser_delete_perm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, to='auth.permission'),
        ),
    ]
