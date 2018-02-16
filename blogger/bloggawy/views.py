
'''from bloggawy.models import Post'''

'''from time import gmtime, strftime'''
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from  .forms import SignUpForm
from django.shortcuts import render, redirect

# Create your views here.
'''def all_posts(request):
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
	return render(request,"posts/new.html",{"form":form})'''

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
