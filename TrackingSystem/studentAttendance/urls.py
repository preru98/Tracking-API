from django.urls import path
from .import views

urlpatterns = [
    path('', views.student_list),
    path('detail/<int:enroll>/',views.student_detail),      #get details by roll number
    path('create/',views.student_create),                   #register student
    path('delete/<int:enroll>/',views.student_delete),      #delete student
    path('update/<int:enroll>/',views.student_update),      #update
    path('map/',views.tag_create),                          #wrong
    path('mapTag/',views.map_tag),                          #map tag with existing student
    path('viewTags/',views.tag_list),                       #view all tags
    path('TapTime/',views.tap_tag),                         #Tap card       
    path('Log/<int:enroll>/',views.student_attendance_log), #attendance log of every student
    path('studentLogin/',views.student_login),              #student login
]

# { "tag":"ABC",
#    "studentRollNumber":"3" 
# }