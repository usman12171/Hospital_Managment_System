# Generated by Django 4.0.4 on 2022-12-25 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/DoctorProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('education', models.CharField(max_length=20, null=True)),
                ('doctorFee', models.PositiveIntegerField()),
                ('department', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_no', models.PositiveBigIntegerField(null=True)),
                ('lab_test', models.CharField(choices=[('Blood test', 'Blood test'), ('Urine test', 'Urine test'), ('Xray', 'Xray'), ('tumor test', 'tumor test'), ('Biochemstry test', 'Biochemstry test')], default='InPatient', max_length=50)),
                ('amount', models.IntegerField()),
                ('doctorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic/PatientProfilePic/')),
                ('address', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=20)),
                ('symptoms', models.CharField(max_length=100)),
                ('patient_file', models.FileField(upload_to='uploads/file')),
                ('prescription', models.CharField(max_length=100)),
                ('patient_type', models.CharField(choices=[('InPatient', 'InPatient'), ('OutPatient', 'OutPatient')], default='InPatient', max_length=50)),
                ('admitDate', models.DateField(auto_now=True)),
                ('releaseDate', models.DateField()),
                ('status', models.BooleanField(default=False)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salry', models.IntegerField()),
                ('staff_type', models.CharField(choices=[('Doctor', 'Doctor'), ('Nurse', 'Nurse'), ('Ward_boy', 'Ward_boy'), ('Reciptionaciest', 'Reciptionaciest'), ('Data_entry operator', 'Data_entry operator')], default='InPatient', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=100)),
                ('room_type', models.CharField(choices=[('Private_room', 'Private_room'), ('PrivatePlus_room', 'PrivatePlus_room'), ('Executive_room', 'Executive_room')], default='InPatient', max_length=50)),
                ('status', models.BooleanField(default=False)),
                ('room_amount', models.IntegerField()),
                ('patientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientDischargeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daySpent', models.PositiveIntegerField()),
                ('medicineCost', models.PositiveIntegerField()),
                ('OtherCharge', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('Lab_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.lab')),
                ('doctorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
                ('patientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient')),
                ('room_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.room')),
            ],
        ),
        migrations.AddField(
            model_name='lab',
            name='patientId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointmentDate', models.DateField(auto_now=True)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False)),
                ('doctorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
                ('patientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.patient')),
            ],
        ),
    ]