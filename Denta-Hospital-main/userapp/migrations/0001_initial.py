# Generated by Django 4.1.5 on 2024-05-08 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Dental_app', '0003_user_reg_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generated_at', models.DateField(max_length=100, null=True)),
                ('number', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dental_app.doctor_reg')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dental_app.user_reg')),
            ],
        ),
    ]
