from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('post_title','post_content','post_photo','category_id')
		widgets = {
            'post_content': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        }
	

# class ModelName(forms.ModelForm):
#     class Meta:
#         model = ModelName  # modify
#         fields = ('fieldname', 'fieldname', 'fieldname', 'fieldname')
#         widgets = {
#             'fieldname': forms.TextInput(attrs={'class': 'form-control'}),
#             'fieldname': forms.TextInput(attrs={'class': 'form-control'}),
#             'fieldname': forms.TextInput(attrs={'class': 'form-control'}),
#         }

