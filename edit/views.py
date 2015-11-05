from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from edit import forms, decorators, models
import dashboard.views


@decorators.belongs_to_document
@login_required(login_url=dashboard.views.login)
def index(request, document_id):
    document = get_object_or_404(models.Document, id=document_id)

    return render(request, 'edit/index.html', {
        'document': document,
        'sections': document.section_set.all(),
        'messages': [message for message in document.message_set.all()[:10]][-1::-1],
        'notifications': document.changenotification_set.all()
    })


@login_required(login_url=dashboard.views.login)
def new(request):
    return render(request, 'edit/new.html')


@login_required(login_url=dashboard.views.login)
def create(request):
    document_form = forms.DocumentForm(request.POST)

    if document_form.is_valid():
        document = document_form.save(commit=False)
        document.owner = request.user
        document.save()

        return redirect('edit:index', id=document.id)

    return redirect('dashboard:dashboard')


@decorators.owner_of_document
@login_required(login_url=dashboard.views.login)
def remove(request, document_id):
    document = get_object_or_404(models.Document, id=document_id)
    document.delete()
    return redirect('dashboard:documents')


@decorators.belongs_to_document
@login_required(login_url=dashboard.views.login)
def update_title(request, document_id):
    document = get_object_or_404(models.Document, id=document_id)
    title = request.POST.get('title')

    if title:
        document.title = title
        document.save()

    return redirect('edit:index', document_id=document_id)


@decorators.belongs_to_document
@login_required(login_url=dashboard.views.login)
def update_description(request, document_id):
    document = get_object_or_404(models.Document, id=document_id)
    description = request.POST.get('description')

    if description:
        document.description = description
        document.save()

    return redirect('edit:index', document_id=document_id)


@decorators.belongs_to_document
@login_required(login_url=dashboard.views.login)
def add_collaborator(request, document_id):
    document = get_object_or_404(models.Document, id=document_id)
    username = request.POST.get('username')
    user = models.User.objects.filter(username=username).get()

    if user:
        document.users.add(user)

    return redirect('edit:index', document_id=document_id)


@decorators.belongs_to_document
@login_required(login_url=dashboard.views.login)
def remove_collaborator(request, document_id, username):
    document = get_object_or_404(models.Document, id=document_id)
    user = models.User.objects.filter(username=username).get()

    if user:
        document.users.remove(user)

    return redirect('edit:index', document_id=document_id)


@decorators.belongs_to_document
@login_required(login_url=dashboard.views.login)
def send_message(request, document_id):
    document = get_object_or_404(models.Document, id=document_id)

    message = models.Message(author=request.user, content=request.POST.get('content'), document=document)
    message.save()

    return redirect(reverse('edit:index', kwargs={'document_id': document_id}) + '#fndtn-messages')
