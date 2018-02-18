from django.db import models
from django.contrib.auth.models import User
from django.db.models import ImageField

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    subscribers = models.ManyToManyField(User)  # subscribe
    def __str__(self):
        return  self.category_name

# we need this table Manually
class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_content = models.CharField(max_length=2000)
    post_photo = ImageField(upload_to='uploads/',default="static/bloggawy/images/testphoto.jpg")
    post_time = models.DateTimeField(auto_now_add=True)  # generate time automatic
    # we can make enhancement here
    post_user = models.ForeignKey(User)
    category_id = models.ForeignKey(Category,null=True)
    # we can make enhancement here
    def __str__(self):
        return self.post_title


class Comment(models.Model):
    comment_content = models.CharField(max_length=1000)
    comment_time = models.DateTimeField(auto_now_add=True)
    # we can make enhancement here
    comment_user = models.ForeignKey(User,null=True)
    comment_post = models.ForeignKey(Post,null=True)
    def __str__(self):
        return self.comment_content





class Reply(models.Model):
    reply_content = models.CharField(max_length=1000)
    reply_time = models.DateTimeField(auto_now_add=True)
    # we can make enhancement here
    reply_user = models.ForeignKey(User)
    reply_comments = models.ManyToManyField(Comment)
    def __str__(self):
        return self.reply_content

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

class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    tag_posts = models.ManyToManyField(Post)
    def __str__(self):
        return self.tag_name
