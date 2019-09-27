from django import forms
from .models import File
from mptt.forms import TreeNodeChoiceField
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

class SignInForm(AuthenticationForm):
   username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
   password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))


class AddFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user',None)
         super(AddFileForm, self).__init__(*args, **kwargs)

         try:
            self.query = File.objects.get(name=self.user).get_descendants(include_self=True)
            self.fields['parent'].queryset = self.query
         except:
             del self.fields['parent']
             self.fields['name'].disabled = True
         
    name = forms.CharField(max_length=75)
    parent = TreeNodeChoiceField(queryset=File.objects.all(), required=False)

    class Meta():
        model = File
        fields = ['name', 'parent']
        
