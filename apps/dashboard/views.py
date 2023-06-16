from django.shortcuts import render

from apps.forum.models import Category, Thread

def DashboardView(request):
    categories = Category.objects.all()
    threads = Thread.objects.all().order_by('-created')[:10]
    
    context = {
        "categories": categories,
        "threads": threads
    }

    return render(request, "dashboard/dashboard.html", context)