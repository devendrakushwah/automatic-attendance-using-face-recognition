from django.urls import path
from .views import *
app_name = 'main'
urlpatterns = [
    path('',my_attendance, name='home'),
    path('upload_image_html/', upload_image_html, name="upload_image_html"),
    path('upload_image_logic/', upload_image_logic, name="upload_image_logic"),
    path('feed_attendance_html/', feed_attendance_html, name="feed_attendance_html"),
    path('feed_attendance_logic/', feed_attendance_logic, name="feed_attendance_logic"),
    path('my_attendance/',my_attendance,name='my_attendance'),
]
