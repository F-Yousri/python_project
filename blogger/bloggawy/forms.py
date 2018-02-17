from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from  .models import Category
from  .models import Post

class SignUpForm(UserCreationForm):
   
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CategoryForm(forms.ModelForm):
   
  
    class Meta:
        model = Category
        fields = ('category_name',)



class PostForm(forms.ModelForm):
   
  
    class Meta:
        model = Post
        fields = ('post_content','post_photo','post_title',)



	



