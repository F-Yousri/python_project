
'''from bloggawy.models import Post'''

'''from time import gmtime, strftime'''
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from  .forms import SignUpForm
from  .forms import CategoryForm
from  .forms import PostForm
from  .forms import CurseForm
from  .forms import TagForm
from  .models import Post
from  .models import Category
from  .models import Curse
from  .models import Tag
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from time import gmtime, strftime



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

def addtag(request):
	
	form=TagForm()
	context={"form":form}
	if request.method=="POST":
		ta_form=TagForm(request.POST)
		if ta_form.is_valid():
			ta_form.save()
			return HttpResponseRedirect("/bloggawy/Tags")
	return render(request,"admin/addtag.html",context)







def adminpanel(request):
    
    return render(request,'admin/adminpaneltwo.html')
      
    	


