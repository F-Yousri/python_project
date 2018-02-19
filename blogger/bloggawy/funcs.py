from django.http import HttpResponseRedirect

def check_super(request):
	if request.user.id:
		return HttpResponse("yeey")
	else:
		return HttpResponseRedirect("/bloggawy/Tags")
