from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.db.models import Prefetch

from apps.forum.models import Category, Thread

def DashboardView(request):
    categories = Category.objects.prefetch_related(Prefetch("subcategory", to_attr="prefetched_subcategory"))
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

class SignupView(CreateView):
    form_class=UserCreationForm
    template_name = 'dashboard/register.html'
    success_url= '/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')

        return super().get(request, *args, **kwargs)