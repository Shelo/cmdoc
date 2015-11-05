from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from edit import models
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user


def index(request):
    if request.user.is_authenticated():
        return redirect('dashboard:dashboard')

    return render(request, 'dashboard/index.html')


def login(request):
    return render(request, 'dashboard/login.html')


@login_required(login_url=login)
def dashboard(request):
    documents = request.user.document_owner.get_queryset() | request.user.document_set.get_queryset()
    documents = documents.distinct().order_by('-last_modified')[:5]

    notifications = QuerySet(model=models.ChangeNotification)
    for document in documents:
        notifications |= document.changenotification_set.get_queryset()[:5]

    return render(request, 'dashboard/dashboard.html', {
        'documents': documents,
        'notifications': notifications.order_by('-modify_time').all()
    })


@login_required(login_url=login)
def documents(request):
    return render(request, 'dashboard/documents.html', {
        'documents': request.user.document_owner.order_by('-last_modified').all()
    })


@login_required(login_url=login)
def collaboration(request):
    return render(request, 'dashboard/documents.html', {
        'documents': request.user.document_set.order_by('-last_modified').all()
    })


def session(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login_user(request, user)
            return redirect('dashboard:dashboard')

    return redirect(login)


@login_required(login_url=login)
def logout(request):
    logout_user(request)
    return redirect('dashboard:index')
