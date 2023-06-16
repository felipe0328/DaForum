from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

from apps.forum.models import Category, Thread

def DashboardView(request):
    categories = Category.objects.all()
    threads = Thread.objects.all().order_by('-created')[:10]
    
    context = {
        "categories": categories,
        "threads": threads
    }

    return render(request, "dashboard/dashboard.html", context)

class LoginInterfaceView(LoginView):
    template_name='dashboard/login.html'

class LogoutInterfaceView(LogoutView):
    template_name='dashboard/logout.html'