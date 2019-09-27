from django import forms
from .models import File
from mptt.forms import TreeNodeChoiceField


class AddFileForm(forms.ModelForm):
    name = forms.CharField(max_length=75)
    parent = TreeNodeChoiceField(queryset=File.objects.all())

    class Meta():
        model = File
        fields = ['name', 'parent']
