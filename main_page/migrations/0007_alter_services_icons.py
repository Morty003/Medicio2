# Generated by Django 4.0.5 on 2022-07-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_alter_services_icons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='icons',
            field=models.CharField(choices=[('Cardiology', 'fas fa-heartbeat'), ('Tablets', 'fas fa-pills'), ('Hospital', 'fas fa-hospital-user'), ('DNA-TEST', 'fas fa-dna'), ('Disabled-person', 'fas fa-wheelchair'), ('Appointments', 'fas fa-notes-medical')], default='', max_length=50),
        ),
    ]
