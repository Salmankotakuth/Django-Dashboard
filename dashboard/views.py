from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def tables(request):
    return render(request, 'dashboard/tables.html')

def billing(request):
    return render(request, 'dashboard/billing.html')

def virtual_reality(request):
    return render(request, 'dashboard/virtual_reality.html')

def rtl(request):
    return render(request, 'dashboard/rtl.html')

def notifications(request):
    return render(request, 'dashboard/notifications.html')

def profile(request):
    return render(request, 'dashboard/profile.html')

def sign_in(request):
    return render(request, 'dashboard/sign_in.html')

def sign_up(request):
    return render(request, 'dashboard/sign_up.html')