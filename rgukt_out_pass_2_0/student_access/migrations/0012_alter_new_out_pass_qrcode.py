# Generated by Django 4.1.2 on 2023-01-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_access', '0011_alter_new_out_pass_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_out_pass',
            name='qrcode',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]