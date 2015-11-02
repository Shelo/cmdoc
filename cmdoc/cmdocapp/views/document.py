from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from cmdocapp import models, forms
from cmdocapp.views import web
from cmdocapp import decorators
from cmdocapp import utils


@decorators.belongs_to_document
@login_required(login_url=web.login)
def edit(request, id):
    document = get_object_or_404(models.Document, id=id)
    return render(request, 'cmdocapp/edit.html', {
        'document': document,
        'sections': document.section_set.all(),
        'messages': [message for message in document.message_set.all()[:10]][-1::-1]
    })


@login_required(login_url=web.login)
def new(request):
    return render(request, 'cmdocapp/new_document.html')


@login_required(login_url=web.login)
def send_new(request):
    document_form = forms.DocumentForm(request.POST)

    if document_form.is_valid():
        document = document_form.save(commit=False)
        document.owner = request.user
        document.save()

        return redirect(edit, id=document.id)

    return redirect(web.dashboard)


@decorators.owner_of_document
@login_required(login_url=web.login)
def delete(request, id):
    document = get_object_or_404(models.Document, id=id)
    document.delete()
    return redirect(web.documents)


@decorators.belongs_to_document
@login_required(login_url=web.login)
def send_new_section(request, id):
    section_form = forms.SectionForm(request.POST)

    if section_form.is_valid():
        section = section_form.save(commit=False)
        section.owner = request.user
        section.document_id = id
        section.modifier = request.user

        position = section.position
        models.Section.objects.filter(document_id=section.document_id,
                                      position__gte=position).update(position=F('position') + 1)

        section.save()

    return redirect(edit, id=id)


@decorators.belongs_to_document
@login_required(login_url=web.login)
def delete_section(request, id, section_id):
    section = get_object_or_404(models.Section, id=section_id)
    position = section.position

    models.Section.objects.filter(document_id=section.document_id,
                                  position__gte=position + 1).update(position=F('position') - 1)

    section.delete()
    return redirect(edit, id=id)


@decorators.belongs_to_document
@login_required(login_url=web.login)
def edit_section(request, id, section_id):
    section = get_object_or_404(models.Section, id=section_id)
    section.content = request.POST.get('content')
    section.modifier = request.user
    section.message = request.POST.get('message')
    section.save()

    utils.sync_sec_cancel(section_id)

    return redirect(edit, id=id)


@decorators.belongs_to_document
@login_required(login_url=web.login)
def render_raw(request, id):
    document = get_object_or_404(models.Document, id=id)
    sections = document.section_set.all()

    content = '\n\n'.join([section.content for section in sections])
    return HttpResponse(content, content_type='text/plain')


@decorators.belongs_to_document
@login_required(login_url=web.login)
def render_html(request, id):
    document = get_object_or_404(models.Document, id=id)
    return render(request, 'cmdocapp/render.html', {
        'document': document
    })


@decorators.belongs_to_document
@login_required(login_url=web.login)
def edit_title(request, id):
    document = get_object_or_404(models.Document, id=id)
    title = request.POST.get('title')

    if title:
        document.title = title
        document.save()

    return redirect(edit, id=id)


@decorators.belongs_to_document
@login_required(login_url=web.login)
def edit_description(request, id):
    document = get_object_or_404(models.Document, id=id)
    description = request.POST.get('description')

    if description:
        document.description = description
        document.save()

    return redirect(edit, id=id)


@decorators.belongs_to_document
@login_required(login_url=web.login)
def add_collaborator(request, id):
    document = get_object_or_404(models.Document, id=id)
    username = request.POST.get('username')
    user = models.User.objects.filter(username=username).get()

    if user:
        document.users.add(user)

    return redirect(edit, id=id)


@decorators.belongs_to_document
@login_required(login_url=web.login)
def remove_collaborator(request, id, username):
    document = get_object_or_404(models.Document, id=id)
    user = models.User.objects.filter(username=username).get()

    if user:
        document.users.remove(user)

    return redirect(edit, id=id)


@decorators.belongs_to_document
@login_required(login_url=web.login)
def send_message(request, id):
    document = get_object_or_404(models.Document, id=id)

    message = models.Message(author=request.user, content=request.POST.get('content'), document=document)
    message.save()

    return redirect(edit, id=id)


@decorators.belongs_to_document
@login_required(login_url=web.login)
def sync_sec_request(request, id):
    section_id = request.POST.get('sectionId')
    section = get_object_or_404(models.Section, id=section_id)

    response = False

    # allow editing if no one is editing or you are editing (just for bugs though...)
    if section.editing is None or section.editing.username == request.user.username:
        response = True

        section.editing = request.user
        section.save_no_notification()

    return JsonResponse({
        'status': response,
        'current': section.editing.username
    })


@decorators.belongs_to_document
@login_required(login_url=web.login)
def sync_sec_cancel(request, id):
    section_id = request.POST.get('sectionId')
    utils.sync_sec_cancel(section_id)

    return JsonResponse({
        'status': True
    })
