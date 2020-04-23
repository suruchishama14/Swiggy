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
            return redirect('open_food')

    except RestaurantModel.DoesNotExist:
        return render(request, "Restaurant/login.html", {"rf": RestroLoginForm(),"error":"Invalid User"})


#def restro_home(request):
   # return render(request,"Restaurant/restro_home.html")
def open_food(request):
    return render(request,'Restaurant/open_Foody.html',{"sf":FoodForm(),"sdata":FoodModel.objects.all()})

def save_food(request):
    sf = FoodForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_food')
    else:
        return render(request,"Restaurant/open_Foody.html",{"sf":sf})


def update_food(request):
    sno = request.GET.get("sno")
    sname = request.GET.get("sname")
    d1 = {"sno":sno,"sname":sname}
    return render(request,"Restaurant/open_Foody.html",{"update_data":d1,"sdata":FoodModel.objects.all()})


def update_food_data(request):
    sno = request.POST.get("s1")
    sname = request.POST.get("s2")
    FoodModel.objects.filter(food_no = sno).update(food_name=sname)
    return redirect('open_food')


def delete_food(request):
    sno = request.GET.get("sno")
    FoodModel.objects.filter(food_no=sno).delete()
    return redirect('open_food')