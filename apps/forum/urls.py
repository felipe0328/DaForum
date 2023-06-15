from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>', views.SubcategoryView, name='forum.subcategory'),
    path('<str:name>/new', views.ThreadCreateView.as_view(),name='forum.createThread'),
    path('<str:name>/thread/<int:pk>', views.ThreadView, name='forum.threadView'),
    path('<str:name>/thread/<int:pk>/new', views.ThreadResponseCreateView.as_view(),name='forum.createThreadResponse'),
]
