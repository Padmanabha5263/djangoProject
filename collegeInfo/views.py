from django.shortcuts import redirect, render
from django.urls import reverse
from .models import ReachUp
# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST["txtName"]
        email = request.POST["txtEmail"]
        subject = request.POST["txtSubject"]
        message = request.POST['txtMessage']
        ReachUp.objects.create(name=name, email=email, subject=subject, message=message)
        print("success")
        return redirect(reverse("collegeInfo:index"))
    else:
        return render(request, "collegeInfo/index.html")


def department(request):
    return render(request,"collegeInfo/departments.html")

def gallery(request):
    return render(request, "collegeInfo/gallery.html")