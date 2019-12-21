from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ImageUploaded(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return str(self.user.username)

class Attendance(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.CharField(max_length = 100)
	status = models.BooleanField()
	def __str__(self):
		return str(self.user.username)+' : '+str(self.date)
