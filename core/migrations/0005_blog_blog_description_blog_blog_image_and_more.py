# Generated by Django 4.0.4 on 2022-12-28 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_doctor_otp_patient_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_pic/blogPic/'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_image',
            field=models.ImageField(blank=True, null=True, upload_to='room_pic/roomPic/'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('Private_room', 'Private_room'), ('PrivatePlus_room', 'PrivatePlus_room'), ('Executive_room', 'Executive_room')], default='Private_room', max_length=50),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_type',
            field=models.CharField(choices=[('Doctor', 'Doctor'), ('Nurse', 'Nurse'), ('Ward_boy', 'Ward_boy'), ('Reciptionaciest', 'Reciptionaciest'), ('Data_entry operator', 'Data_entry operator')], default='Doctor', max_length=50),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('rate', models.IntegerField(default=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', related_query_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.comment'),
        ),
    ]