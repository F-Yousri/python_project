from django.shortcuts import render
from .models import Post
from .models import User
from .models import Comment
# from .forms import PostForm
from .forms import CommentForm
from django.http import HttpResponseRedirect
from time import gmtime, strftime


# Create your views here.
def all_posts(request):
    return render(request, "posts/all_p.html", {"all_posts": Post.objects.all()})


def post_details(request, p_id):
    return render(request, "posts/post_page.html", {"post": Post.objects.get(id=p_id)})


# def new_post(request):
# 	form=PostForm()
# 	if request.method=="POST":
# 		form=PostForm(request.POST)
# 		if form.is_valid():
# 			obj = form.save(commit=False)
# 		    obj.user_id = request.user
# 		    obj.time = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
# 			return HttpResponseRedirect('/bloggawy/posts')
# 	return render(request,"posts/new.html",{"form":form})

def index(request):
    return render(request, "web/index.html")#http://127.0.0.1:8000/opensource/
def success(request):
    return render(request, "web/success.html")
def error(request):
    return render(request, "web/error.html")
def comment(request, post_id):
    comment_form = CommentForm()
    current_post = Post.objects.get(id=post_id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST,initial={'comment_post_id': post_id})
        if comment_form.is_valid():
            #comment_form.save()
            #current_user = User.objects.get(id=1)
            current_user = request.user
            comment_form.CommentSave(current_post,current_user)
            return HttpResponseRedirect("success")
    comments_of_post = Comment.objects.filter(comment_post=current_post).order_by('-comment_time')
    context = {"form": comment_form,"comments":comments_of_post}
    return render(request, "web/post_page.html", context)

# To send variables implecitly
# form = CreateASomething(request.POST)
# if form.is_valid():
#     obj = form.save(commit=False)
#     obj.field1 = request.user
#     obj.save()


# To check for Authentication
# if request.user.is_authenticated:
#     ... # Do something for logged-in users.
# else:
#     ... # Do something for anonymous users.
