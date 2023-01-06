from django import forms
from .models import *
  
class StudentForm(forms.ModelForm):
  
    class Meta:
        model = Student_images
        fields = ['student_img']