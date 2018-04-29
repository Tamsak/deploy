# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from models import *

def index(request):
    users = {'users' : User.objects.all()}
    return render(request,'user_app/index.html',users)
def show(request, id):
    user = {'users' : User.objects.filter(id=id)}
    return render(request,'user_app/show.html',user)
def edit(request,id):
    user = {'users': User.objects.filter(id=id)}
    return render(request,'user_app/edit.html',user)
def update(request,id):
    edit_user = User.objects.get(id=id)
    edit_user.first_name = request.POST['first_name']
    edit_user.last_name = request.POST['last_name']
    edit_user.email = request.POST['email']
    edit_user.save()
    return redirect('/users/'+id)
def add(request):
    return render(request,'user_app/add.html')
def delete(request,id):
    User.objects.get(id=id).delete()
    return redirect('/users')
def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('users/add')
    else:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['email'])
    return redirect('/users')



