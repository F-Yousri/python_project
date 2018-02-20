<<<<<<< HEAD
from django import forms
from .models import Post
from .models import Comment
from .models import Like
from .models import Reply

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

class ReplyForm(forms.ModelForm):
    def ReplySave (self, current_post, current_user,comment):
        reply = self.save(commit=False)
        reply.reply_post = current_post
        reply.reply_user = current_user
        reply.reply_comments = comment
        reply.save()  # to save in database

    class Meta:
        model = Reply
        fields = ('reply_content',)
        widgets = {
            'reply_content': forms.Textarea(attrs={
                'class': 'form-control-lg col-sm-2 col-md-6',
                'word-break': 'break-word',
                'placeholder': 'Write a reply',
                'rows':'1',
                'col':'69'

            }),

        }


=======
# from django import forms
# from .models import Post

# class PostForm(forms.ModelForm):
# 	class Meta:
# 		model=Post
# 		fields=("text")
# 		widgets = {
#             'text': forms.Textarea(attrs={'cols': 80, 'rows': 20})
#         }
	
>>>>>>> fady_branch

# class ModelName(forms.ModelForm):
#     class Meta:
#         model = ModelName  # modify
#         fields = ('fieldname', 'fieldname', 'fieldname', 'fieldname')
#         widgets = {
#             'fieldname': forms.TextInput(attrs={'class': 'form-control'}),
#             'fieldname': forms.TextInput(attrs={'class': 'form-control'}),
#             'fieldname': forms.TextInput(attrs={'class': 'form-control'}),
#         }
