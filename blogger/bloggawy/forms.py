from django import forms
from .models import Post
from .models import Comment


# class PostForm(forms.ModelForm):
# 	class Meta:
# 		model=Post
# 		fields=("text")
# 		widgets = {
#             'text': forms.Textarea(attrs={'cols': 80, 'rows': 20})
#         }

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
