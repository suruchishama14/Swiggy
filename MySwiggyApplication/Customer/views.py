from django.shortcuts import render

# Create your views here.
def offermenu(request):
    return render(request, 'main/offermenu.html')
