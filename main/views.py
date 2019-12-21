from django.shortcuts import render
from .models import ImageUploaded, Attendance
from django.core.files.storage import FileSystemStorage
from .face_extractor import face_extract as fe
from .face_recognizer import face_recognize as fr
import os
import shutil
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
import datetime
import pytz
import smtplib 

# Create your views here.
@login_required
def upload_image_html(request):
	qSet = ImageUploaded.objects.filter(user=request.user)
	if len(qSet) == 0:
		return render(request,'main/upload_image_html.html',{})
	qSet = Attendance.objects.filter(user=request.user)
	return render(request,'main/my_attendance.html',{'data':qSet})
	
@login_required
def upload_image_logic(request):
	image = request.FILES['image']
	fs = FileSystemStorage()
	filename = fs.save('main/known_faces/'+str(request.user.username)+'.jpg', image)
	obj = ImageUploaded(user=request.user)
	obj.save()
	qSet = Attendance.objects.filter(user=request.user)
	return render(request,'main/my_attendance.html',{'data':qSet})

@login_required
def my_attendance(request):
	qSet = ImageUploaded.objects.filter(user=request.user)
	if len(qSet) == 0:
		return render(request,'main/upload_image_html.html',{})
	qSet = Attendance.objects.filter(user=request.user)
	return render(request,'main/my_attendance.html',{'data':qSet})

@staff_member_required
def feed_attendance_html(request):
	if request.user.is_superuser:
		return render(request,'main/feed_attendance_html.html',{})
	qSet = Attendance.objects.filter(user=request.user)
	return render(request,'main/my_attendance.html',{'data':qSet})
	
@staff_member_required
def feed_attendance_logic(request):
	if request.user.is_superuser:
		image = request.FILES['image']
		fs = FileSystemStorage()
		shutil.rmtree('main/camera')
		os.mkdir('main/camera')
		filename = fs.save('main/camera/camera_snap.jpg', image)
		fe()
		usernames = fr()
		qSet = User.objects.all()
		now = datetime.datetime.now()
		tz = pytz.timezone('Asia/Kolkata')
		now = now.astimezone(tz)
		date_string = now.strftime("%d/%m/%Y %H:%M:%S")
 
		for user in qSet:
			print('sending emails.....')
			if user.username in usernames:
				obj = Attendance(user=user,date=date_string,status=True)
				obj.save()
				message = "\nHello, "+user.username+" Attendace marked as present on "+date_string
				print(message)
				s = smtplib.SMTP('smtp.gmail.com', 587) 
				s.starttls() 
				s.login("vaishnavmajor@gmail.com", "csec2020") 
				s.sendmail("vaishnavmajor@gmail.com", user.email, message) 
				s.quit()
			else:
				obj = Attendance(user=user,date=date_string,status=False)
				obj.save()
				message = "\nHello, "+user.username+" Attendace marked as absent on "+date_string
				print(message)
				s = smtplib.SMTP('smtp.gmail.com', 587) 
				s.starttls() 
				s.login("vaishnavmajor@gmail.com", "csec2020") 
				s.sendmail("vaishnavmajor@gmail.com", user.email, message) 
				s.quit()
			
	qSet = Attendance.objects.filter(user=request.user)
	return render(request,'main/my_attendance.html',{'data':qSet})
	s
