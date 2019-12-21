from PIL import Image
import face_recognition
import os
import shutil
def face_extract():
	image = face_recognition.load_image_file("main/camera/camera_snap.jpg")
	face_locations = face_recognition.face_locations(image)
	cam_image = Image.open('main/camera/camera_snap.jpg')

	index = 1
	
	shutil.rmtree('main/extracted_faces')
	os.mkdir('main/extracted_faces')
	
	for face_location in face_locations:
		t,r,b,l = face_location
		img = cam_image.crop((l,t,r,b))
		img.save('main/extracted_faces/unknown'+str(index)+'.jpg')
		index+=1
