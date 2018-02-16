
'''from bloggawy.models import Post'''

'''from time import gmtime, strftime'''
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from  .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User



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

def adminpanel(request):
    users=User.objects.all()
    context={"allusers":users}
    
    return render(request,'admin/adminpaneltwo.html',context)

      
    	


