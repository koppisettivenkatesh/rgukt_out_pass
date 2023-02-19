from email.policy import default
from django.db import models

class new_out_pass(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    student_id = models.CharField(max_length=500)
    main_reason = models.CharField(max_length=500)
    today_date = models.CharField(max_length=500)
    out_data = models.CharField(max_length=500)
    dis = models.TextField(max_length=3000)
    response = models.CharField(max_length=50, default = 'pending')
    faculty_id = models.CharField(max_length=50, default = 'none')
    Rejected_reason = models.CharField(max_length=50, default = 'none')
    out_pass_id = models.CharField(max_length=500)
    student_out = models.CharField(max_length=500, default = 'none')
    student_in = models.CharField(max_length=500, default = 'none')
    qrcode = models.FileField(null=True)
    qr_image_name = models.CharField(max_length=500, default = 'none')


class Student_images(models.Model):
    student_id= models.CharField(max_length=500)
    student_img = models.FileField( upload_to= "student_profile_images" , null=True ,)
