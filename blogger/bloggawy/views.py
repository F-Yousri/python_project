from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
# Create your views here.

def login_form(request) :

	if request.method == 'POST' :

		name = request.POST['username']
		password = request.POST['password']

		user = authenticate(username = name, password=password)

		if user is not None:
			login(request,user)
			return HttpResponseRedirect("/bloggawy/home")

	return render(request,'login_form.html') 		