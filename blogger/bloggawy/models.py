from django.db import models
from django.contrib.auth.models import User
from django.db.models import ImageField
from django.db.models import DateTimeField



class Category(models.Model):
    category_name = models.CharField(max_length=200)
    subscribers = models.ManyToManyField(User)  # subscribe

    def __str__(self):
        return  self.category_name

class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    '''tag_posts = models.ManyToManyField(Post)'''
    def __str__(self):
        return self.tag_name
# we need this table Manually
class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_content = models.CharField(max_length=2000)
    post_photo = ImageField(upload_to='uploads/',default="static/bloggawy/images/testphoto.jpg")
    post_time = models.DateTimeField(auto_now_add=True)  # generate time automatic
    # we can make enhancement here
    post_user = models.ForeignKey(User)
    post_category = models.ForeignKey(Category, null=True)
    tag_posts = models.ManyToManyField(Tag)
    def __str__(self):
        return self.post_title


def findindex(L, obj):
    try:
        return L.index(obj)
    except ValueError:
        return -1

class Comment(models.Model):
    comment_content = models.CharField(max_length=1000)
    comment_time = models.DateTimeField(auto_now_add=True)
    # we can make enhancement here
    comment_user = models.ForeignKey(User, null=True)
    comment_post = models.ForeignKey(Post, null=True)

    def replacecurse(self):
        words = self.comment_content.split()
        all_bad_words = Curse.objects.all()
        bads = []
        new_words=[]
        for bad in all_bad_words:
            bads.append(bad.curse_content)
        for word in words:
            if findindex(bads, word) != -1:
                stars = '*' * len(word)
                word = stars
                new_words.append(word)
            else :
                new_words.append(word)
        self.comment_content=" ".join(new_words)

class ReplyForm(forms.ModelForm):
    def ReplySave (self, current_post, current_user,comment):
        reply = self.save(commit=False)
        reply.reply_post = current_post
        reply.reply_user = current_user
        reply.reply_comments = comment
        reply.replacecurse()
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


class Curse(models.Model):
    curse_content = models.CharField(max_length=20)
    def __str__(self):
        return self.curse_content


# we need this table Manually
# we handle error of the count like by code
# we will prevent user from make more than one like at a time
class Like(models.Model):
    like_user = models.ForeignKey(User)
    like_post = models.ForeignKey(Post)
    like_type = models.BooleanField(default=None)  # False >>dislike or True >>like
    def __str__(self):
        return self.like_post
