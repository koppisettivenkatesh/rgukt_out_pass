# Generated by Django 4.1.2 on 2023-01-03 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_access', '0009_new_out_pass_qr_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_images',
            name='student_img',
            field=models.FileField(null=True, upload_to='student_profile_images'),
        ),
    ]
