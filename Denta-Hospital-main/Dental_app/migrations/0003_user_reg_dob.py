# Generated by Django 4.1.5 on 2024-05-08 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dental_app', '0002_remove_doctor_reg_address_doctor_reg_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_reg',
            name='dob',
            field=models.CharField(max_length=50, null=True),
        ),
    ]