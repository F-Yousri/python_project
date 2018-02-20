from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from  .forms import SignUpForm
from  .forms import CategoryForm
from  .forms import PostForm
from  .forms import CurseForm
from  .forms import UserForm
from  .models import Post
from  .models import Category
from  .models import Curse
from  .models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from time import gmtime, strftime
import re
from .models import Comment
from .forms import CommentForm
from .models import Like
from .models import Post
from django.core.exceptions import ObjectDoesNotExist
import json
from django.db.models import Q

# from django.http import JsonResponse

# just for store the like in the model
def listpost(request):

    post_list=Post.objects.all().order_by("-post_time")
    paginator = Paginator(post_list, 5)
    page=request.GET.get('post')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)

    except EmptyPage:
        posts=paginator.page(paginator.num_pages)

    return render(request,"admin/listposts.html",{"posts":posts}) 




def get_post(request):
    
    q = request.GET.get('term','')
    posts = Post.objects.filter(Q(tag_posts = Tag.objects.get(tag_name__icontains=q))|Q(post_title__icontains=q))
    results = []
    for pl in posts:
        post_json = {}
        post_json ['id']=pl.id;
        post_json ['label']=pl.post_title;
        results.append(post_json)
        data = json.dumps(results)
    
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def like(request, post_id):
    current_post = Post.objects.get(id=post_id)
    try:
        current_like_object = Like.objects.get(like_post=current_post)
        if current_like_object.like_type == False:
            current_like_object.like_type=True
            current_like_object.save()
        else:
            current_like_object.delete()
    except ObjectDoesNotExist:
        like_object = Like.objects.create(
            like_user=request.user,
            like_post=current_post,
            like_type=True
        )
        like_object.save()

    return HttpResponse("Like Done")


# just for store the dislike in the model
def dislike(request, post_id):
    current_post = Post.objects.get(id=post_id)
    try:
        current_like_object = Like.objects.get(like_post=current_post)
        if current_like_object.like_type == True:
            current_like_object.like_type=False
            current_like_object.save()
        else:
            current_like_object.delete()
    except ObjectDoesNotExist:
        like_object = Like.objects.create(
            like_user=request.user,
            like_post=current_post,
            like_type=False
        )
        like_object.save()

    return HttpResponse("Dislike Done");

# Create your views here.
def all_posts(request):
    return render(request, "posts/all_p.html", {"all_posts": Post.objects.all()})

def post_details(request, p_id):
    return render(request, "posts/post_page.html", {"post": Post.objects.get(id=p_id)})

def new_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post_user = User(1)
            # obj.post_user = request.user
            # obj.time = strftime("%a, %d %b %Y %H:%M:%s", gmtime())
            obj.save()
            words = obj.post_content.split()
            for word in words:
                if re.match(r'^#[a-zA-Z0-9]+',word):
                    tag=Tag()
                    if Tag.objects.filter(tag_name=word):
                        tag=Tag.objects.get(tag_name=word)
                    else:
                        tag.tag_name=word
                        tag.save()
                    tag.tag_posts.add(obj)
        return HttpResponseRedirect('/bloggawy/posts')
    return render(request, "posts/new.html", {"form": form, "all_cats": Category.objects.all()}) 

def index(request):
    return render(request, "web/index.html")  # http://127.0.0.1:8000/opensource/
def useraddandall(request):
    return render(request,"admin/userallnduseradd.html")


def success(request):
    return render(request, "web/success.html")


def error(request):
    return render(request, "web/error.html")

def registeration(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            raw_email= form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password,email=raw_email)
            login(request, user)
            return redirect('web/home.html')
    else:
    	form = SignUpForm()
    return render(request, 'web/registration.html',{"form": form})

def allusers(request):
    users=User.objects.all()
    context={"allusers":users}
    
    return render(request,'admin/users.html',context)

def allposts(request):
    posts=Post.objects.all()
    context={"allposts":posts}
    
    return render(request,'admin/posts.html',context)


def allcategories(request):
    categories=Category.objects.all()
    context={"allcategories":categories}
    
    return render(request,'admin/categories.html',context)


def deletecategory(request,st_id):
	category=Category.objects.get(id=st_id)
	category.delete()
	return HttpResponseRedirect("/bloggawy/allcategories")


def editcategory(request,st_id):
	category=Category.objects.get(id=st_id)
	categoryform=CategoryForm(instance=category)
	context={"form":categoryform}
	if request.method=="POST":
		category_form=CategoryForm(request.POST,instance=category)
		if category_form.is_valid():
			category_form.save()
			path="/bloggawy/allcategories"
			return HttpResponseRedirect(path)
	return render(request,"admin/addcategory.html",context)

def addcategory(request):
	form=CategoryForm()
	context={"form":form}
	if request.method=="POST":
		category_form=CategoryForm(request.POST)
		if category_form.is_valid():
			category_form.save()
			return HttpResponseRedirect("/bloggawy/allcategories")
	return render(request,"admin/addcategory.html",context)


def showpost(request,st_id):
	post=Post.objects.get(id=st_id)
	context={"post":post}

	return render (request,"admin/showpost.html",context)



def deletepost(request,st_id):
	post=Post.objects.get(id=st_id)
	post.delete()
	return HttpResponseRedirect("/bloggawy/allposts")



def addpost(request):
	form=PostForm()
	context={"form":form}
	if request.method=="POST":
		post_form=CategoryForm(request.POST)
		if post_form.is_valid():
			
			post_form.save();
			return HttpResponseRedirect("/bloggawy/allposts")
	return render(request,"admin/addposts.html",context)


def editpost(request,st_id):
	post=Post.objects.get(id=st_id)
	postform=PostForm(instance=post)
	context={"form":postform}
	if request.method=="POST":
		post_form=PostForm(request.POST,instance=post)
		if post_form.is_valid():
			post_form.save()
			return HttpResponseRedirect("/bloggawy/allposts")

	return render(request,"admin/addposts.html",context)

def forbiddenwords(request):
	curses=Curse.objects.all()
	context={"allcurses":curses}
	return render(request,'admin/curses.html',context)


def deleteword(request,st_id):
	curse=Curse.objects.get(id=st_id)
	curse.delete()
	return HttpResponseRedirect("/bloggawy/forbiddenwords")




def editword(request,st_id):
	curse=Curse.objects.get(id=st_id)
	curseform=CurseForm(instance=curse)
	context={"form":curseform}
	if request.method=="POST":
		cur_form=CurseForm(request.POST,instance=curse)
		if cur_form.is_valid():
			cur_form.save()
			return HttpResponseRedirect("/bloggawy/forbiddenwords")
	return render(request,"admin/addcurse.html",context)

def addcurse(request):
	
	form=CurseForm()
	context={"form":form}
	if request.method=="POST":
		cur_form=CurseForm(request.POST)
		if cur_form.is_valid():
			cur_form.save()
			return HttpResponseRedirect("/bloggawy/forbiddenwords")
	return render(request,"admin/addcurse.html",context)

def tags(request):
	tags=Tag.objects.all()
	context={"alltags":tags}
	return render(request,'admin/tags.html',context)


def deletetag(request,st_id):
	tag=Tag.objects.get(id=st_id)
	tag.delete()
	return HttpResponseRedirect("/bloggawy/Tags")

def edittag(request,st_id):
	tag=Tag.objects.get(id=st_id)
	tagform=TagForm(instance=tag)
	context={"form":tagform}
	if request.method=="POST":
		t_form=TagForm(request.POST,instance=tag)
		if t_form.is_valid():
			t_form.save()
			return HttpResponseRedirect("/bloggawy/Tags")
	return render(request,"admin/addtag.html",context)



def deleteuser(request,st_id):
    user=User.objects.get(id=st_id)
    user.delete()
    return HttpResponseRedirect("/bloggawy/allusers")


def edituser(request,st_id):
    user=User.objects.get(id=st_id)
    userform=UserForm(instance=post)
    context={"form":userform}
    if request.method=="POST":
        post_form=UserForm(request.POST,instance=user)
        if post_form.is_valid():
            post_form.save()
            path="/bloggawy/allusers"
            return HttpResponseRedirect(path)
    return render(request,"admin/adduser.html",context)

def adduser(request):
    form=UserForm()
    context={"form":form}
    if request.method=="POST":
        post_form=UserForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect("/bloggawy/allusers")
    return render(request,"admin/adduser.html",context)

# view post
def comment(request, post_id):
    comment_form = CommentForm()
    current_post = Post.objects.get(id=post_id)
    current_user = request.user
    if request.method == "POST":
        comment_form = CommentForm(request.POST, initial={'comment_post_id': post_id})
        if comment_form.is_valid():
            # comment_form.save()
            current_user = User.objects.get(id=1)
            comment_form.CommentSave(current_post, current_user)
            return HttpResponseRedirect("success")
        #I have fix some problem here to display the recent comment in the top of comments
    comments_of_post = Comment.objects.filter(comment_post=current_post).order_by('-id')
    try:
        like_status = Like.objects.get(like_post=current_post, like_user=1)
    except ObjectDoesNotExist:
        like_status = None

    like_count = Like.objects.filter(like_type=True).count()
    dislike_count = Like.objects.filter(like_type=False).count()
    context = {
        "form": comment_form,
        "comments": comments_of_post,
        "like": like_status,
        "likes": like_count,
        "dislikes": dislike_count,
    }
    return render(request, "web/post_page.html", context)

def adminpanel(request):
    
    return render(request,'admin/adminpaneltwo.html')
      
    	


