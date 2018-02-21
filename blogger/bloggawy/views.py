from .models import User
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.mail import send_mail
from .forms import SignUpForm
from .forms import CategoryForm
from .forms import PostForm
from .forms import CurseForm
from .forms import UserForm
from .models import Post
from .models import Category
from .models import Curse
from .models import Tag
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import re
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CommentForm
from .forms import ReplyForm
from .forms import TagForm
from .models import Like
from .models import Reply
from django.core.exceptions import ObjectDoesNotExist
import json
from django.db.models import Q
from django.contrib.auth import logout as django_logout


# from django.http import JsonResponse

# just for store the like in the model

def check_super(request):
    # return HttpResponse(request.user.id)
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")


def get_post(request):
    q = request.GET.get('term', '')
    posts = Post.objects.filter(Q(tag_posts=Tag.objects.get(tag_name__icontains=q)) | Q(post_title__icontains=q))
    results = []
    for pl in posts:
        post_json = {}
        post_json['id'] = pl.id;
        post_json['label'] = pl.post_title;
        results.append(post_json)
        data = json.dumps(results)

    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def like(request, post_id):
    current_post = Post.objects.get(id=post_id)
    if request.user.is_authenticated():
        current_user = request.user
    else:
        current_user = None

    try:
        current_like_object = Like.objects.get(like_post=current_post,
                                               like_user=current_user)  # state for the current user
        if current_like_object.like_type == False:
            current_like_object.like_type = True
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
    if request.user.is_authenticated():
        current_user = request.user
    else:
        current_user = None
    try:
        current_like_object = Like.objects.get(like_post=current_post,
                                               like_user=current_user)  # state for the current user
        if current_like_object.like_type == True:
            current_like_object.like_type = False
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
    check_dislikes_counter = Like.objects.filter(like_post=current_post, like_type=False).count()
    if check_dislikes_counter > 10:
        current_post.delete()
    return HttpResponse("Dislike Done");


def home(request):
    all_categories = Category.objects.all()
    p1 = Category.subscribers.through.objects.filter(user_id=request.user.id)
    p2 = []
    try:
        posts = Post.objects.all().order_by('-id')
    except Post.DoesNotExis:
        posts = None

    for i in p1:
        p2.append(i.category_id)
    context = {"allCategories": all_categories,
               'subscribercategory': p2,
               "posts": posts
               }
    return render(request, "web/home2.html", context)


@login_required
def logout(request):
    django_logout(request)
    return HttpResponseRedirect("/bloggawy/home")


def login_form(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/bloggawy/home")
        else:
            st = 0
            context = {"login": st}
            return render(request, 'web/login_form.html', context)

    return render(request, 'web/login_form.html')


def create(request):
    if request.method == 'GET':
        category_id = request.GET['category']
        user_id = request.GET['user']
        Type = request.GET['type']
        if (Type == 'Subscribe'):

            # p1 = User.objects.create(
            # 		username = subscribers
            # 	)
            # p1.save()
            a1 = Category.subscribers.through.objects.create(
                category_id=category_id,
                user_id=user_id
            )

            subject = "welcome"
            message = "Hello " + request.POST['username'] + " you have subscribed successfully in " + request.GET[
                'category'] + " welcome aboard"
            from_mail = settings.EMAIL_HOST_USER
            to_list = [request.user.email]
            send_mail(subject, message, from_mail, to_list, fail_silently=True)

        # a1.save()
        # a1.subscribers.add(p1)
        # # a1.save()
        elif (Type == 'UnSubscribe'):
            a1 = Category.subscribers.through.objects.filter(
                category_id=category_id,
                user_id=user_id
            )
            a1.delete()
        return HttpResponse("success")


# # Create your views here.
# def home(request):
#     if request.user.is_superuser:
#         pass
#     else:
#         return HttpResponseRedirect("/bloggawy/home")
#     return render(request, "posts/all_p.html", {"home": Post.objects.all()})


# def post_details(request, p_id):
#     return render(request, "posts/post_page.html", {"post": Post.objects.get(id=p_id)})


def new_post(request):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            # obj.post_user = User(1)
            obj.post_user = request.user
            # obj.time = strftime("%a, %d %b %Y %H:%M:%s", gmtime())
            obj.save()
            words = obj.post_content.split()
            for word in words:
                if re.match(r'^#[a-zA-Z0-9]+', word):
                    tag = Tag()
                    if Tag.objects.filter(tag_name=word):
                        tag = Tag.objects.get(tag_name=word)
                    else:
                        tag.tag_name = word
                        tag.save()
                    obj.tag_posts.add(tag)
        return HttpResponseRedirect('/bloggawy/posts')
    return render(request, "posts/new.html", {"form": form, "all_cats": Category.objects.all()})


# view post
def post_page(request, post_id):
    comment_form = CommentForm()
    reply_form = ReplyForm()
    try:
        current_post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        pass
    #     #return render(request, "web/errorpostpage.html")
    if request.user.is_authenticated():
        current_user = request.user
    else:
        current_user = None

    if request.method == "POST":
        reply_form = ReplyForm(request.POST)
        comment_form = CommentForm(request.POST, initial={'comment_post_id': post_id})

        if comment_form.is_valid():
            comment_form.CommentSave(current_post, current_user)
            return HttpResponseRedirect("" + post_id)
        if reply_form.is_valid():
            comment = Comment.objects.get(id=request.POST.get('numb'))
            reply_form.ReplySave(current_post, current_user, comment)
            return HttpResponseRedirect("" + post_id)

    comments_of_post = Comment.objects.filter(comment_post=current_post).order_by('-id')
    try:
        like_status = Like.objects.get(like_post=current_post, like_user=current_user)
    except ObjectDoesNotExist:
        like_status = None
    try:
        all_replies = Reply.objects.all()
    except ObjectDoesNotExist:
        all_replies = None

    like_count = Like.objects.filter(like_type=True, like_post=current_post).count()
    dislike_count = Like.objects.filter(like_type=False, like_post=current_post).count()
    try:
        three_recent_posts = Post.objects.all().order_by('-id')[:3]
    except ObjectDoesNotExist:
        three_recent_posts = None

    context = {
        "current__post": current_post,
        "form": comment_form,
        "formr": reply_form,
        "comments": comments_of_post,
        "replies": all_replies,
        "like": like_status,
        "likes": like_count,
        "dislikes": dislike_count,
        "recentposts": three_recent_posts,
    }

    return render(request, "web/post_page.html", context)


def get_post(request):
    if requst.is_ajax():
        q = request.GET.get('term', '')
        posts = Post.objects.filter(Q(tag_posts=Tag.objects.get(tag_name__icontains=q)) | Q(post_title__icontains=q))
        results = []
        for pl in posts:
            post_json = {}
            post_json['id'] = pl.id;
            post_json['label'] = pl.post_title;
            results.append(post_json)
            data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            checkmail = User.objects.filter(email=request.POST['email'])
            if checkmail.exists():
                return render(request, 'web/registration.html', {"form": form, "errormail": 1})
            save_it = form.save()
            save_it.save()
            subject = "welcome"
            message = "Hello " + request.POST[
                'username'] + " you have subscribed successfully in -category name-  welcome aboard"
            from_mail = settings.EMAIL_HOST_USER
            to_list = [save_it.email]
            send_mail(subject, message, from_mail, to_list, fail_silently=True)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            raw_email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password, email=raw_email)
            login(request, user)
            return HttpResponseRedirect("/bloggawy/home")
        else:
            error = 1

    else:
        form = SignUpForm()
    return render(request, 'web/registration.html', {"form": form})


def allusers(request):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    users = User.objects.all()
    context = {"allusers": users}

    return render(request, 'admin/users.html', context)


def allposts(request):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    posts = Post.objects.all()
    context = {"allposts": posts}

    return render(request, 'admin/posts.html', context)


def allcategories(request):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    categories = Category.objects.all()
    context = {"allcategories": categories}

    return render(request, 'admin/categories.html', context)


def deletecategory(request, st_id):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    category = Category.objects.get(id=st_id)
    category.delete()
    return HttpResponseRedirect("/bloggawy/allcategories")


def editcategory(request, st_id):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    category = Category.objects.get(id=st_id)
    categoryform = CategoryForm(instance=category)
    context = {"form": categoryform}
    if request.method == "POST":
        category_form = CategoryForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            path = "/bloggawy/allcategories"
            return HttpResponseRedirect(path)
    return render(request, "admin/addcategory.html", context)


def addcategory(request):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    form = CategoryForm()
    context = {"form": form}
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect("/bloggawy/allcategories")
    return render(request, "admin/addcategory.html", context)


def showpost(request, st_id):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    post = Post.objects.get(id=st_id)
    context = {"post": post}

    return render(request, "admin/showpost.html", context)


def deletepost(request, st_id):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    post = Post.objects.get(id=st_id)
    post.delete()
    return HttpResponseRedirect("/bloggawy/allposts")


def editpost(request, st_id):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    post = Post.objects.get(id=st_id)
    postform = PostForm(instance=post)
    context = {"form": postform}
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            # post.form.post_photo=request.POST['post_photo']
            obj = post_form.save()
            words = obj.post_content.split()
            for word in words:
                if re.match(r'^#[a-zA-Z0-9]+', word):
                    tag = Tag()
                    if Tag.objects.filter(tag_name=word):
                        tag = Tag.objects.get(tag_name=word)
                    else:
                        tag.tag_name = word
                        tag.save()
                    obj.tag_posts.add(tag)

            return HttpResponseRedirect("/bloggawy/allposts")

    return render(request, "admin/addposts.html", context)


def forbiddenwords(request):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    curses = Curse.objects.all()
    context = {"allcurses": curses}
    return render(request, 'admin/curses.html', context)


def deleteword(request, st_id):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    curse = Curse.objects.get(id=st_id)
    curse.delete()
    return HttpResponseRedirect("/bloggawy/forbiddenwords")


def editword(request, st_id):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    curse = Curse.objects.get(id=st_id)
    curseform = CurseForm(instance=curse)
    context = {"form": curseform}
    if request.method == "POST":
        cur_form = CurseForm(request.POST, instance=curse)
        if cur_form.is_valid():
            cur_form.save()
            return HttpResponseRedirect("/bloggawy/forbiddenwords")
    return render(request, "admin/addcurse.html", context)


def addcurse(request):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    form = CurseForm()
    context = {"form": form}
    if request.method == "POST":
        cur_form = CurseForm(request.POST)
        if cur_form.is_valid():
            cur_form.save()
            return HttpResponseRedirect("/bloggawy/forbiddenwords")
    return render(request, "admin/addcurse.html", context)


def tags(request):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    tags = Tag.objects.all()
    context = {"alltags": tags}
    return render(request, 'admin/tags.html', context)


def deletetag(request, st_id):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    tag = Tag.objects.get(id=st_id)
    tag.delete()
    return HttpResponseRedirect("/bloggawy/Tags")


def edittag(request, st_id):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    tag = Tag.objects.get(id=st_id)
    tagform = TagForm(instance=tag)
    context = {"form": tagform}
    if request.method == "POST":
        t_form = TagForm(request.POST, instance=tag)
        if t_form.is_valid():
            t_form.save()
            return HttpResponseRedirect("/bloggawy/Tags")
    return render(request, "admin/addtag.html", context)


def deleteuser(request, st_id):
    user = User.objects.get(id=st_id)
    user.delete()
    return HttpResponseRedirect("/bloggawy/allusers")


def edituser(request, st_id):
    user = User.objects.get(id=st_id)
    userform = UserForm(instance=post)
    context = {"form": userform}
    if request.method == "POST":
        post_form = UserForm(request.POST, instance=user)
        if post_form.is_valid():
            post_form.save()
            path = "/bloggawy/allusers"
            return HttpResponseRedirect(path)
    return render(request, "admin/adduser.html", context)


def adduser(request):
    form = UserForm()
    context = {"form": form}
    if request.method == "POST":
        post_form = UserForm(request.POST)
        if post_form.is_valid() and not User.objects.filter(email=request.POST['email']):
            post_form.save()
            return HttpResponseRedirect("/bloggawy/allusers")
    return render(request, "admin/adduser.html", context)


def adminpanel(request):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    return render(request, 'admin/adminpaneltwo.html')


def promote(request, us_id):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    us = User.objects.get(id=us_id)
    us.is_superuser = 1
    us.is_active = 1
    us.is_staff = 1
    us.save()
    allusers = User.objects.all()
    return HttpResponseRedirect("/bloggawy/allusers", {"allusers": allusers, })


def block(request, us_id):
    if request.user.is_superuser:
        pass
    else:
        return HttpResponseRedirect("/bloggawy/home")
    us = User.objects.get(id=us_id)
    if us.is_active:
        us.is_active = 0
    else:
        us.is_active = 1
    us.save()
    allusers = User.objects.all()
    return HttpResponseRedirect("/bloggawy/allusers", {"allusers": allusers, })
