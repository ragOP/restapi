# Generated by Django 4.0.7 on 2023-07-26 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_company_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='comapny_id',
            new_name='company_id',
        ),
    ]