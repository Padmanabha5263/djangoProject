from django.shortcuts import redirect, render
import json
from django.http import  JsonResponse
from django.urls import reverse
from .models import ReachUp
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST['message']
        try:
            ReachUp.objects.create(name=name, email=email, subject=subject, message=message)
            converTime ={
                "name":name,
                "message":"Thank you For your Query kindly we will get back to you"
            }
            return JsonResponse(converTime, status=200)
        except:
            print("error")
    else:
        return render(request, "collegeInfo/index.html")


def department(request):
    return render(request,"collegeInfo/departments.html")

def gallery(request):
    return render(request, "collegeInfo/gallery.html")