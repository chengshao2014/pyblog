#-*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from django.template import RequestContext,loader
from django.views.generic import View
from appadmin import forms
from django.shortcuts import render_to_response
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
            post = Post(title = data['title'],author = data['author'], body = data['body'])
            post.save(using='first')
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
# def vote(request, id):
#     return HttpResponse("You're voting on id %s." % id)
