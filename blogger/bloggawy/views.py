from django.shortcuts import render
from bloggawy.models import Post
from django.contrib.auth.models import User
from bloggawy.models import Category
from bloggawy.models import Tag
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from time import gmtime, strftime
import re


# Create your views here.
def all_posts(request):
    return render(request, "web/post_page.html", {"all_posts": Post.objects.all()})


def post_details(request, p_id):
    return render(request, "posts/post_page.html", {"post": Post.objects.get(id=p_id)})


def new_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post_user = User(1)
            # obj.post_user_id=request.user.id
            obj.time = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
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
                        # return HttpResponse(tag)
                    tag.tag_posts.add(obj)


        return HttpResponseRedirect('/bloggawy/posts')
    return render(request, "posts/new.html", {"form": form, "all_cats": Category.objects.all()})

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
