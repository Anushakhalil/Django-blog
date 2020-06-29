from django import forms

from .models import Blog


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [  # ye model form ban gae ab isay render krengy or view krengy
            'title',
            'content',
            # 'picture',
        ]

 