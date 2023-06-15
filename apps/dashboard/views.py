from apps.forum.views import CategoryListView
from django.shortcuts import render

from apps.forum.models import Category, Thread

class DashboardTemplateView(CategoryListView):
    template_name="dashboard/dashboard.html"


def DashboardView(request):
    categories = Category.objects.all()
    threads = Thread.objects.all()[:10]
    
    context = {
        "categories": categories,
        "threads": threads
    }

    return render(request, "dashboard/dashboard.html", context)