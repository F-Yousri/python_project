from django.shortcuts import render
from bloggawy.models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect
from time import gmtime, strftime

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
