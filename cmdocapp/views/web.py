from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.db.models.query import QuerySet
from cmdocapp import models

def index(request):
    if request.user.is_authenticated():
        return redirect(dashboard)

    return render(request, 'cmdocapp/index.html')


def login(request):
    return render(request, 'cmdocapp/login.html')


@login_required(login_url=login)
def dashboard(request):
    documents = request.user.document_owner.get_queryset() | request.user.document_set.get_queryset()
    documents = documents.distinct().order_by('-last_modified')[:5]

    notifications = QuerySet(model=models.ChangeNotification)
    for document in documents:
        notifications |= document.changenotification_set.get_queryset()[:5]

    return render(request, 'cmdocapp/dashboard.html', {
        'documents': documents,
        'notifications': notifications.order_by('-modify_time').all()
    })


@login_required(login_url=login)
def documents(request):
    return render(request, 'cmdocapp/documents.html', {
        'documents': request.user.document_owner.order_by('-last_modified').all()
    })


@login_required(login_url=login)
def collaboration(request):
    return render(request, 'cmdocapp/documents.html', {
        'documents': request.user.document_set.order_by('-last_modified').all()
    })


def send_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login_user(request, user)
            return redirect(documents)

    return redirect(login)


@login_required(login_url=login)
def send_logout(request):
    logout_user(request)
    return redirect(index)
