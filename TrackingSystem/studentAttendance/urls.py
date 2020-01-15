from django.urls import path
from .import views

urlpatterns = [
    path('', views.student_list),
    path('detail/<int:enroll>/',views.student_detail),
    path('create/',views.student_create),
    path('delete/<int:enroll>/',views.student_delete),
    path('update/<int:enroll>/',views.student_update),
    path('map/',views.tag_create),
]