# Generated by Django 4.0.5 on 2022-07-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0014_pricing_is_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='cross_out_option_1',
            field=models.CharField(choices=[('class="na"', 'Yes'), ('', 'No')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='cross_out_option_2',
            field=models.CharField(choices=[('class="na"', 'Yes'), ('', 'No')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='cross_out_option_3',
            field=models.CharField(choices=[('class="na"', 'Yes'), ('', 'No')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='cross_out_option_4',
            field=models.CharField(choices=[('class="na"', 'Yes'), ('', 'No')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='cross_out_option_5',
            field=models.CharField(choices=[('class="na"', 'Yes'), ('', 'No')], max_length=50),
        ),
    ]
