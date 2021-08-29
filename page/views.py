from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

from .task import test_func
# Create your views here.


def call_task_anywhere(r):
	test_func.delay(username=r.user.username)

def page_view(request):
	if request.user.is_authenticated:

		call_task_anywhere(request)

		user = request.user
		request.session["user_pk"] = user.pk

	return TemplateResponse(request,'page/index.html',{})


def page_view2(request):
	s = request.session.get("user_pk",None)
	if s is None:
		print("None")
	else:
		print(s)
	return TemplateResponse(request,'page/about.html',{})