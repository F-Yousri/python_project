from django.shortcuts import render
from .models import Post
from .models import User
from .models import Comment
from .models import Curse
from .forms import CommentForm
from .forms import ReplyForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from bloggawy.models import Post
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from time import gmtime, strftime
from .models import Like
from .models import Post
from .models import Reply
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout as django_logout
from .models import Category


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
    # ToDo i want to delete the post if the post have greater than 10 likes
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
            a1 = Category.subscribers.through.objects.create(
                category_id=category_id,
                user_id=user_id
            )
        elif (Type == 'UnSubscribe'):
            a1 = Category.subscribers.through.objects.filter(
                category_id=category_id,
                user_id=user_id
            )
            a1.delete()
        return HttpResponse("success")


def index(request):
    return render(request, "web/index.html")


def success(request):
    return render(request, "web/success.html")


def error(request):
    return render(request, "web/error.html")

def pagesuccess(request):
    return render(request, "web/successpage.html")


def pageerror(request):
    return render(request, "web/successerror.html")

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
            return HttpResponseRedirect(""+post_id)
        if reply_form.is_valid():
            comment = Comment.objects.get(id=request.POST.get('numb'))
            reply_form.ReplySave(current_post, current_user, comment)
            return HttpResponseRedirect(""+post_id)

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
        "recentposts":three_recent_posts,
    }

    return render(request, "web/post_page.html", context)
