from django.views.generic import ListView

from apps.forum.models import Category

class DashboardListView(ListView):
    model = Category
    context_object_name = "categories"
    template_name = 'dashboard/dashboard.html'
