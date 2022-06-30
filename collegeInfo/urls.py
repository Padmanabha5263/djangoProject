from django.urls import path
from . import views

app_name = "collegeInfo"

urlpatterns = [
    path("", views.index, name="index"),
    path("departments/", views.department, name="departments"),
    path("gallery/", views.gallery, name="gallery"),
]
