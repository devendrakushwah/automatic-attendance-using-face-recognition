import face_recognition
import os
import shutil
def face_recognize():
	''' To calculate known face encodings '''
	known_faces_encodings = []
	list_of_known_faces = os.listdir('main/known_faces')

	for item in list_of_known_faces:
		known_picture = face_recognition.load_image_file('main/known_faces/'+item)
		known_faces_encodings.append(face_recognition.face_encodings(known_picture)[0])

	''' To calculate unknown face encodings '''
	extracted_faces_encodings = []
	list_of_extracted_faces = os.listdir('main/extracted_faces')

	for item in list_of_extracted_faces:
		extracted_picture = face_recognition.load_image_file('main/extracted_faces/'+item)
		extracted_faces_encodings.append(face_recognition.face_encodings(extracted_picture)[0])

	present_students = []

	index = 0
	ans = []
	for student in extracted_faces_encodings:
		results = face_recognition.compare_faces(known_faces_encodings, student) 
		for i in range(len(results)):
			if results[i]:
				ans.append(list_of_known_faces[i][:-4])
	return ans
