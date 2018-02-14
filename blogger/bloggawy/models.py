from django.db import models


# Edit By Ahmed Helal Ahmed.

class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    user_password = models.CharField(max_length=200)
    user_email = models.EmailField(max_length=254)
    user_blocked = models.BooleanField(default=True)  # False >>blocked user or True >>unblocked user
    user_admin = models.BooleanField(default=False)  # False >>user or True >>admin


class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    cat_users = models.ManyToManyField(User)  # subscribe


class Post(models.Model):
    post_text = models.CharField(max_length=2000)
    post_time = models.TimeField(auto_now_add=True)  # generate time automatic
    # we can make enhancement here
    post_user = models.ForeignKey(User)
    post_categories = models.ManyToManyField(Category)


class Comment(models.Model):
    comment_text = models.CharField(max_length=1000)
    comment_time = models.TimeField(auto_now_add=True)
    # we can make enhancement here
    comment_user = models.ForeignKey(User)
    comment_post = models.ForeignKey(Post)


class Replay(models.Model):
    replay_text = models.CharField(max_length=1000)
    replay_time = models.TimeField(auto_now_add=True)
    # we can make enhancement here
    replay_user = models.ForeignKey(User)
    replay_comments = models.ManyToManyField(Comment)


class Curse(models.Model):
    curse_text = models.CharField(max_length=20)
    curse_comments = models.ManyToManyField(Comment)
    curse_replays = models.ManyToManyField(Replay)


class Like(models.Model):
    like_user = models.ForeignKey(User)
    like_post = models.ForeignKey(Post)


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    tag_posts = models.ManyToManyField(Post)
