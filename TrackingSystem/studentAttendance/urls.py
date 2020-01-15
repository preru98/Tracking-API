from django.urls import path
from .import views

urlpatterns = [
    path('', views.student_list),
    path('detail/<int:enroll>/',views.student_detail),
    path('create/',views.student_create),
]