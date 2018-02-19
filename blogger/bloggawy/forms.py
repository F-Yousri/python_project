from django import forms
from .models import Post
from .models import Comment
from .models import Like
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from  .models import Category
from  .models import Curse
from  .models import Tag


class UserForm(UserCreationForm):
    
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')
        
        
            


class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('post_title','post_content','post_photo','category_id')
		widgets = {
            'post_content': forms.Textarea(attrs={
                'cols': 80,
                'rows': 20, 
                'placeholder': 'Write your post here'
                }),
            }


class CommentForm(forms.ModelForm):
    def CommentSave (self, current_post, current_user):
        comment = self.save(commit=False)
        comment.comment_post = current_post
        comment.comment_user = current_user
        comment.save()  # to save in database

    class Meta:
        model = Comment
        fields = ('comment_content',)
        widgets = {
            'comment_content': forms.Textarea(attrs={
                'class': 'form-control-lg col-sm-2 col-md-6',
                'word-break': 'break-word',
                'placeholder': 'Write a comment',
                'rows':'1',
                'col':'69'

            }),
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

class SignUpForm(UserCreationForm):
   
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CategoryForm(forms.ModelForm):
   
  
    class Meta:
        model = Category
        fields = ('category_name',)

class CurseForm(forms.ModelForm):
   
  
    class Meta:
        model = Curse
        fields = ('curse_content',)


class TagForm(forms.ModelForm):
   
  
    class Meta:
        model = Tag
        fields = ('tag_name',)
