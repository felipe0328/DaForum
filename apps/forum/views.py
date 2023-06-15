from django.shortcuts import render

from .models import Subcategory, Category


def SubcategoryView(request, name:str):
    categories = Category.objects.all()
    subcategory = Subcategory.objects.get(name=name)
    
    context = {
        "categories": categories,
        "subcategory":subcategory
    }

    return render(request, "forum/subcategory_detail.html",context)
