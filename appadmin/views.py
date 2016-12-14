#-*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from django.template import RequestContext,loader
from django.views.generic import View
from appadmin import forms
from django.shortcuts import render_to_response
from django.shortcuts import render,render_to_response,HttpResponse
from home.Helper import Checkcode
from io import StringIO

class MyView(View):
    def get(self, request, *args, **kwargs):
        latest_question_list = Post.objects.order_by('-update')
        template = loader.get_template('appadmin/index.html')
        context = {
            'latest_question_list': latest_question_list,
        }
        return HttpResponse(template.render(context, request))

def blog_form(request):
    template = loader.get_template('appadmin/blog_form.html')
    form = forms.BlogForm()
    if request.method == 'POST':
        form = forms.BlogForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        if 'id' not in data:
            post = Post(title = data['title'],body = data['body'], status = data['status'])
            post.save()
            return HttpResponseRedirect('/appadmin/login')
        else:
            post = Post.objects.get(id=data.id)
            post.title = data['title']
            post.author = data['author']
            post.body = data['body']
            post.save()
            return HttpResponse("this is homepage!")
            # return HttpResponseRedirect('/appadmin/login')
    else:
        form = forms.BlogForm()
        context = {'form':form}
        return HttpResponse(template.render(context, request))

def blog_index(request):
    template = loader.get_template('appadmin/blog_form.html')
    form = forms.BlogForm()
    context = {'form':form,}
    return HttpResponse(template.render(context, request))


def vote(request, id):
    latest_question_list = Post.objects.get(id="%s" % id)
    context = {'latest_question_list':latest_question_list,}
    template = loader.get_template('appadmin/bolg_article.html')
    return HttpResponse(template.render(context, request))
    # return HttpResponse("You're voting on id %s." % id)

def admin_login(request):
    template = loader.get_template('appadmin/blog_login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def CheckCode(request):
    mstream = StringIO()
    validate_code = Checkcode.create_validate_code()
    img = validate_code[0]
    img.save(mstream, "GIF")

    #将验证码保存到session
    request.session["CheckCode"] = validate_code[1]
    return HttpResponse(mstream.getvalue())

# def index(request):
#     latest_question_list = Post.objects.order_by('-update')
#     template = loader.get_template('appadmin/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
#
#
# def homepage(req):
#     return HttpResponse("this is homepage!")
#
#
# def detail(request, id):
#     return HttpResponse("You're looking at id %s." % id)
#
#
# def results(request, id):
#     response = "You're looking at the result of id %s."
#     return HttpResponse(response % id)
#
#
