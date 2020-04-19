from django.shortcuts import render,redirect
from Restaurant.forms import *
from django.contrib import messages

from Restaurant.forms import RestaurantForm


def showMain(request):
    return render(request,"Restaurant/main.html")


def registerPage(request):
    return render(request,"Restaurant/register.html",{"rf":RestaurantForm()})


def save_res(request):
    rf = RestaurantForm(request.POST)
    if rf.is_valid():
        db = rf.save(commit=False)
        db.restro_otp = 5475
        db.restro_status = 'pending'
        db.save()
        messages.success(request,"Once the admin approve the Registration you will receive an email and a text Message")
        return redirect('restro')
    else:
        return render(request,"Restaurant/register.html",{"rf":rf})

def restro_login(request):
    return render(request,"Restaurant/login.html",{"rf":RestroLoginForm()})

def restro_login_check(request):
    cno = request.POST.get("contactno")
    upass = request.POST.get("password")
    try:
        res = RestaurantModel.objects.get(restro_contact=cno,restro_password=upass)
        if res.restro_status == "pending":
            message = "Hello Restaurant "+res.restro_name+" Your Registration is still need to Approve"
            return render(request, "Restaurant/login.html", {"rf": RestroLoginForm(), "error": message})
        elif res.restro_status == "cancel":
            message = "Hello Restaurant " + res.restro_name + " Your Registration is Cancel "
            return render(request, "Restaurant/login.html", {"rf": RestroLoginForm(), "error": message})
        else:
            #request.session['status'] = True
            request.session['contact'] = cno
            return redirect('restro_home')

    except RestaurantModel.DoesNotExist:
        return render(request, "Restaurant/login.html", {"rf": RestroLoginForm(),"error":"Invalid User"})


def restro_home(request):
    return render(request,"Restaurant/restro_home.html")
