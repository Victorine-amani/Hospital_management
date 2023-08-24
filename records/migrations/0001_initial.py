# Generated by Django 4.2 on 2023-05-16 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('particulars', models.TextField()),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor')),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
        ),
    ]