from django.shortcuts import render, redirect
from .models import UserProfile
def page1(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname = request.POST['lname']
        ph_no = request.POST['ph_no']
        email = request.POST['email']
        gender = request.POST['gender']
        profile=UserProfile(f_name=fname,l_name=lname,ph_no=ph_no,email=email,gender=gender)
        profile.save()
        return redirect('page1')
    else:
        return render(request,'Page1.html')
def page2(request):
    if request.method=="POST":
        email=request.POST['email']
        try:
            profile=UserProfile.objects.get(email=email)
            return render(request,"Page3.html",{'profile':profile,'message':'Found User'})
        except UserProfile.DoesNotExist:
            return render(request,"Page3.html",{'message':"No user found"})
    else:
        return render(request,"Page2.html")

# Create your views here.
