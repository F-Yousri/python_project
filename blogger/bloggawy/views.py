from django.shortcuts import render
from .models import Post
from .models import User
from .models import Comment
# from .forms import PostForm
from .forms import CommentForm
from .forms import ReplyForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from time import gmtime, strftime
from .models import Like
from .models import Post
from .models import Reply
from django.core.exceptions import ObjectDoesNotExist


# from django.http import JsonResponse

# just for store the like in the model
def like(request, post_id):
    current_post = Post.objects.get(id=post_id)
    try:
        current_like_object = Like.objects.get(like_post=current_post)
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
    try:
        current_like_object = Like.objects.get(like_post=current_post)
        if current_like_object.like_type == True:
            current_like_object.like_type = False
            # ToDo i want to delete the post if the post have 10 likes
            check_dislikes_counter = Like.objects.filter(like_post=current_post, like_type=False)
            if check_dislikes_counter == 1:
                current_post.delete()
            else:
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


def index(request):
    return render(request, "web/index.html")  # http://127.0.0.1:8000/opensource/


def success(request):
    return render(request, "web/success.html")


def error(request):
    return render(request, "web/error.html")


# view post
def comment(request, post_id):
    comment_form = CommentForm()
    reply_form = ReplyForm()
    current_post = Post.objects.get(id=post_id)
    current_user = request.user

    if request.method == "POST":
        reply_form = ReplyForm(request.POST)
        comment_form = CommentForm(request.POST, initial={'comment_post_id': post_id})
        if comment_form.is_valid():
            # comment_form.save()
            # current_user = User.objects.get(id=1)
            comment_form.CommentSave(current_post, current_user)
            return HttpResponseRedirect("success")
        if reply_form.is_valid():
            comment = Comment.objects.get(id=request.POST.get('numb'))
            reply_form.ReplySave(current_post, current_user, comment)
            return HttpResponseRedirect("success")
    # I have fix some problem here to display the recent comment in the top of comments
    comments_of_post = Comment.objects.filter(comment_post=current_post).order_by('-id')
    try:
        like_status = Like.objects.get(like_post=current_post, like_user=current_user)
        all_replys = Reply.objects.all()
    except ObjectDoesNotExist:
        like_status = None
        all_replys = None

    like_count = Like.objects.filter(like_type=True,like_post=current_post).count()
    dislike_count = Like.objects.filter(like_type=False,like_post=current_post).count()
    context = {
        "current__post": current_post,
        "form": comment_form,
        "formr": reply_form,
        "comments": comments_of_post,
        "replys": all_replys,
        "like": like_status,
        "likes": like_count,
        "dislikes": dislike_count,
    }
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
