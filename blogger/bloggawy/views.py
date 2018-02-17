from django.shortcuts import render
from bloggawy.models import Post
from bloggawy.models import Category
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from time import gmtime, strftime

# Create your views here.
def all_posts(request):
	return render(request,"web/post_page.html",{"all_posts":Post.objects.all()})
def post_details(request, p_id):
	return render (request,"posts/post_page.html",{"post":Post.objects.get(id=p_id)})
def new_post(request):
	form=PostForm()
	if request.method=="POST":
		form=PostForm(request.POST,request.FILES)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.post_user_id = 1
			# return HttpResponse(obj.post_photo)
			# return HttpResponse(str(obj.post_user_id) +' &'+ obj.post_content)
			#obj.post_user_id=request.user.id
			obj.time = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
			obj.save()
			return HttpResponseRedirect('/bloggawy/posts')
	return render(request,"posts/new.html",{"form":form, "all_cats":Category.objects.all()})



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
