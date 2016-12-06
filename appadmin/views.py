#-*- coding:utf-8 -*-
from django.http import HttpResponse
# from django.template import loader
from .models import Post
from django.template import RequestContext,loader
from django.views.generic import View
from django.shortcuts import render
class MyView(View):
    def get(self, request, *args, **kwargs):
        latest_question_list = Post.objects.order_by('-update')
        template = loader.get_template('appadmin/index.html')
        context = {
            'latest_question_list': latest_question_list,
        }
        return HttpResponse(template.render(context, request))
        # return render(request, template_name='appadmin/index.html', context=context)

def login(self,request):
    return HttpResponse("this is homepage!")
        # return render(request, template_name='appadmin/login.html')



def index(request):
    latest_question_list = Post.objects.order_by('-update')
    template = loader.get_template('appadmin/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def homepage(req):
    return HttpResponse("this is homepage!")


def detail(request, id):
    return HttpResponse("You're looking at id %s." % id)


def results(request, id):
    response = "You're looking at the result of id %s."
    return HttpResponse(response % id)


def vote(request, id):
    return HttpResponse("You're voting on id %s." % id)
