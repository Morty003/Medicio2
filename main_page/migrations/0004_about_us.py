# Generated by Django 4.0.5 on 2022-06-30 16:51

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_doctors_facebook_doctors_instagram_doctors_linkedin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(blank=True, max_length=200)),
                ('photo', models.ImageField(upload_to=main_page.models.About_Us.get_file_name3)),
                ('small_desc', models.CharField(blank=True, max_length=200)),
                ('option_1', models.CharField(max_length=200)),
                ('option_2', models.CharField(max_length=200)),
                ('option_3', models.CharField(max_length=200)),
                ('big_desc', models.TextField(max_length=500)),
            ],
        ),
    ]
