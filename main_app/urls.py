from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    # path('', views.WidgetCreate.as_view(), name='add'),
    path('items/<int:pk>/delete/', views.WidgetDelete.as_view(), name='delete'),
    path('add_widget/', views.add_widget, name='add_widget'),
]