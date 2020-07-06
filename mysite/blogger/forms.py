from .models import Blogger
from django import forms

class CreateBloggerForm(forms.ModelForm):
    class Meta:
        model = Blogger
        fields = [ 'username','pic']


