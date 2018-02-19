from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from bloggawy.models import Post
# from .forms import PostForm
from django.http import HttpResponseRedirect
from time import gmtime, strftime
from django.contrib.auth import logout as django_logout
from .models import Category

# Create your views here.


def home(request):
	all_categories = Category.objects.all()
	p1 = Category.subscribers.through.objects.filter(user_id = request.user.id)
	p2=[]
	for i in p1:
		p2.append(i.category_id)






	# data = {'data':p1}
	context = {"allCategories" : all_categories,
				'subscribercategory':p2
	}
	# return HttpResponseRedirect("/user/home.html")
	return render(request,"web/home2.html",context)

@login_required
def logout(request):
    django_logout(request)
    return HttpResponseRedirect("/bloggawy/home")
    

def login_form(request) :

	if request.method == 'POST' :

		name = request.POST['username']
		password = request.POST['password']

		user = authenticate(username = name, password=password)

		if user is not None:
			if user.is_active :
				login(request,user)			
				return HttpResponseRedirect("/bloggawy/home")
		else:
			st = 0
			context = {"login" : st}
			return render(request,'web/login_form.html',context)		

	return render(request,'web/login_form.html')


def create(request):
	if request.method == 'GET':
		category_id = request.GET['category']
		user_id = request.GET['user']
		Type = request.GET['type']
		if(Type == 'Subscribe'):
			
			# p1 = User.objects.create(
			# 		username = subscribers
			# 	)
			# p1.save()
			a1 = Category.subscribers.through.objects.create(
					category_id = category_id,
					user_id = user_id
				)
			# a1.save()
			# a1.subscribers.add(p1)
			# # a1.save()
		elif(Type == 'UnSubscribe'):
			a1 = Category.subscribers.through.objects.filter(
					category_id = category_id,
					user_id = user_id
				)
			a1.delete()			
		return HttpResponse("success")

# @login_required
# def logged_in_only(request):
# 	# if request.user.is_authenticated():
# 	context = {"logged" :1}
# 	return render(request,'web/home2.html',context)


# Create your views here.
def all_posts(request):
	return render(request,"posts/all_p.html",{"all_posts":Post.objects.all()})
def post_details(request, p_id):
	return render (request,"posts/post_page.html",{"post":Post.objects.get(id=p_id)})
def new_post(request):
	form=PostForm()
	if request.method=="POST":
		form=PostForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.user_id = request.user
			obj.time = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
			return HttpResponseRedirect('/bloggawy/posts')
	return render(request,"posts/new.html",{"form":form})



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

