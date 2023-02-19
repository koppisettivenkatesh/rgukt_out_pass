from django.shortcuts import render,redirect
import cv2
import pyqrcode
from pyqrcode import QRCode
from datetime import date
from django.contrib import messages
from student_access.models import  *


# Create your views here.
def index(request):
    return render(request, 'index.html')

def security(request):
    return render(request, 'security.html')


def scan(request):
        camera_id = 0
        delay = 1
        window_name = 'OpenCV QR Code'
        qcd = cv2.QRCodeDetector()
        cap = cv2.VideoCapture(camera_id)
        current_date = date.today()
        current_date_format = current_date.strftime("%d/%m/%Y")
        scanned_code = None
        student_id_scanned = None
        while True:
                ret, frame = cap.read()

                if ret:
                        verify = None
                        ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
                        if ret_qr:
                                for s, p in zip(decoded_info, points):
                                        if s:   
                                                image_name = s.split("-")
                                                scanned_code = s
                                                student_id_scanned = image_name[0]
                                                try:
                                                    if new_out_pass.objects.filter(student_id = image_name[0] , student_out= current_date_format , response= "approve" , out_pass_id= s ).exists():
                                                        verify = 'already scanned'
                                                        break
                                                    elif new_out_pass.objects.filter(student_id = image_name[0] ,student_out= "none", response= "approve" , out_pass_id= s ).exists():
                                                        verify = "approved"
                                                        new_out_pass.objects.filter(student_id = image_name[0] ,student_out= "none", response= "approve" , out_pass_id= s ).update(student_out= current_date_format)
                                                        break
                                                    elif new_out_pass.objects.filter(student_id = image_name[0] ,student_out= "none", response= "reject" , out_pass_id= s ).exists():
                                                        verify = 'reject'
                                                        break
                                                    elif new_out_pass.objects.filter(student_id = image_name[0] ,student_out= "none", response= "pending" , out_pass_id= s ).exists():
                                                        verify = 'pending'
                                                        break
                                                    else:
                                                        verify = "not found"
                                                        break
                                                except:
                                                        verify = None
                                                
                                        else:
                                                color = (0, 0, 255)
                                        frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
                        if verify is None :
                                cv2.imshow(window_name, frame)
                        else:
                                break
                        
                                                        
                if cv2.waitKey(delay) & 0xFF == ord('q'):
                        break

        cv2.destroyWindow(window_name)
        response = new_out_pass.objects.filter(student_id=student_id_scanned , out_pass_id=scanned_code)
        profile = Student_images.objects.filter(student_id= student_id_scanned)
        if verify == 'approved' :
                messages.success(request,"Out Pass approved")
                return render(request, 'security.html ', {'data' : response , 'profile' : profile})
        elif verify == 'already scanned' :
                messages.success(request, " Out Pass already scanned ")
                return render(request, 'security.html ', {'data' : response , 'profile' : profile})
        elif verify == 'not found' :
                messages.error(request, "No data found")
                return render(request, 'security.html ', {'data' : response , 'profile' : profile})
        elif verify == None:
                messages.error(request, "Please Scan Again")
                return render(request, 'security.html')
        else:
                pass