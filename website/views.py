from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    context= {'sir' : "(Most Iconic)"}

    return render(request,"website/home.html", context)

def doors_page_view(request):
    context= {'sir' : "(Most Iconic)"}

    return render(request,"website/doors.html", context)

def dire_page_view(request):
    context= {'sir' : "(Most Iconic)"}

    return render(request,"website/dire.html", context)

