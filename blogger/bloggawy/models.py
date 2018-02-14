from django.db import models

# Create your models here.
class User(models.Model):
	user_name = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	blocked = models.BooleanField(default=1) # 0 >>blocked user or 1 >>unblocked user
	is_admin = models.BooleanField(default=0) # 0 >>user or 1 >>admin



class Category(models.Model):
	cat_name = models.CharField(max_length = 200)



class Post(models.Model):
	post_text = models.CharField(max_length = 2000)
	time = models.TimeField(auto_now_add=True) #generate time automatic
	user_id = models.ForeignKey(User)
	cat_id = models.ForeignKey(Category)


class Comment(models.Model):
	comment_text = models.CharField(max_length =1000)
	time = models.TimeField()
	user_id = models.ForeignKey(User)
	post_id = models.ForeignKey(Post)
	reply_text = models.CharField(max_length = 1000) #weak entity

class Curses(models.Model):
	curses_text = models.CharField(max_length =500)


class Like(models.Model):
	number_likes = models.IntegerField()
	user_id = models.ForeignKey(User)
	post_id = models.ForeignKey(Post)



class Tag(models.Model):
	tag_name =models.CharField(max_length = 100)


class UserCat(models.Model):
	user_id = models.ForeignKey(User)
	cat_id = models.ForeignKey(Category)


class CommentCurses(models.Model):
	comment_id = models.ForeignKey(Comment)
	curses_id = models.ForeignKey(Curses)


class PostTag(models.Model):
	tag_id =models.ForeignKey(Tag)
	post_id =models.ForeignKey(Post)
