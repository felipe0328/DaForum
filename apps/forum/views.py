from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect

from .models import Subcategory, Category, Thread, ThreadResponse
from .forms import ThreadForm, ThreadResponseForm


def SubcategoryView(request, name:str):
    categories = Category.objects.all()
    subcategory = Subcategory.objects.get(name=name)
    
    context = {
        "categories": categories,
        "subcategory": subcategory,
    }

    return render(request, "forum/subcategory_detail.html",context)

def ThreadView(request, name:str, pk:int):
    categories = Category.objects.all()
    subcategory = Subcategory.objects.get(name=name)
    thread = Thread.objects.get(pk=pk)
    
    context = {
        "categories": categories,
        "subcategory": subcategory,
        "thread": thread,
    }

    return render(request, "forum/thread_detail.html",context)

class ThreadCreateView(CreateView):
    model=Thread
    form_class = ThreadForm
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        subcategory_name = self.kwargs['name']

        self.object = form.save(commit=False)
        self.object.subcategory = Subcategory.objects.get(name=subcategory_name)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
         return reverse_lazy('forum.subcategory', kwargs={'name': self.kwargs['name']})

class ThreadResponseCreateView(CreateView):
    model= ThreadResponse
    form_class = ThreadResponseForm

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        thread_pk = self.kwargs['pk']

        self.object = form.save(commit=False)
        self.object.thread = Thread.objects.get(pk=thread_pk)
        self.object.save()
        
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
         return reverse_lazy('forum.threadView', kwargs={'name': self.kwargs['name'], 'pk': self.kwargs['pk']})