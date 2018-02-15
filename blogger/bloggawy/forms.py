from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=("text")
		widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        }
		
