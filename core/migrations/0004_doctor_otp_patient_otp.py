# Generated by Django 4.0.4 on 2022-12-26 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_patient_doctor_alter_doctor_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='otp',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='otp',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
