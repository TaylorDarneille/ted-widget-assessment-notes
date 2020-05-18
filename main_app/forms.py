from django.forms import ModelForm
from .models import Widget

# Create the form class.
class WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']