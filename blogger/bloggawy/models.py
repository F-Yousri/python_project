from django.db import models
from django.contrib.auth.models import User
from django.db.models import ImageField


class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    subscribers = models.ManyToManyField(User)  # subscribe

# we need this table Manually
class Post(models.Model):
    post_title = models.CharField(max_length=50)
    post_content = models.CharField(max_length=2000)
    post_photo = ImageField(upload_to='static/bloggawy/images', height_field=None, width_field=None, max_length=100)
    post_time = models.TimeField(auto_now_add=True)  # generate time automatic
    # we can make enhancement here
    post_user = models.ForeignKey(User)
    post_categories = models.ManyToManyField(Category)

class Comment(models.Model):
    comment_content = models.CharField(max_length=1000)
    comment_time = models.TimeField(auto_now_add=True)
    # we can make enhancement here
    comment_user = models.ForeignKey(User)
    comment_post = models.ForeignKey(Post)


class Reply(models.Model):
    reply_content = models.CharField(max_length=1000)
    reply_time = models.TimeField(auto_now_add=True)
    # we can make enhancement here
    reply_user = models.ForeignKey(User)
    reply_comments = models.ManyToManyField(Comment)


class Curse(models.Model):
    curse_content = models.CharField(max_length=20)


# we need this table Manually
# we handle error of the count like by code
# we will prevent user from make more than one like at a time
class Like(models.Model):
    like_user = models.ForeignKey(User)
    like_post = models.ForeignKey(Post)
    like_type = models.BooleanField()  # False >>dislike or True >>like

class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    tag_posts = models.ManyToManyField(Post)
