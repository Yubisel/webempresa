from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def history(request):
    return render(request, "core/history.html")

def visit_us(request):
    return render(request, "core/visit_us.html")

def contact(request):
    return render(request, "core/contact.html")