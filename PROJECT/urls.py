from django.contrib import admin
from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('students/', students),
    path('sahifa/', bosh_sahifa),
    path('kitob__gt/', studensts_kiotb__gt0),
    path('students/<int:pk>', student),
    path('kitoblar/', kitoblar),
    path('student_q/', student_qoshish),
    path('mualliflar/<int:pk>', muallif_form),
]
