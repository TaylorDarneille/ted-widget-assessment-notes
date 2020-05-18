from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
from django.views.generic.edit import CreateView, DeleteView

# Create your views here.
def home(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'index.html', {'widgets': widgets, 'form': widget_form})

# You don't actually use this view since you use a ModelForm instead
# this Class Based View will work if you want to have the add widget form on a separate page
# class WidgetCreate(CreateView):
#     model = Widget
#     fields = '__all__'
#     success_url = '/'

def add_widget(request):
    print("is this thing on?")
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('home')

class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'