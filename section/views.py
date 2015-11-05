from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from edit import decorators
from section import forms, utils, models
import edit.models


@decorators.belongs_to_document
@login_required(login_url='dashboard:login')
def create(request, document_id):
    section_form = forms.SectionForm(request.POST)

    if section_form.is_valid():
        section = section_form.save(commit=False)
        section.owner = request.user
        section.document_id = document_id
        section.modifier = request.user

        if section.position == -1:
            last = models.Section.objects.filter(
                document_id=section.document_id
            ).last()

            if last is None:
                section.position = 0
            else:
                section.position = last.position + 1

        models.Section.objects.filter(
            document_id=section.document_id,
            position__gte=section.position
        ).update(position=F('position') + 1)

        section.save()

    return redirect('edit:index', document_id=document_id)


@decorators.belongs_to_document
@login_required(login_url='dashboard:login')
def remove(request, document_id, section_id):
    section = get_object_or_404(models.Section, id=section_id)
    position = section.position

    models.Section.objects.filter(document_id=section.document_id,
                                  position__gte=position + 1).update(position=F('position') - 1)

    section.delete()
    return redirect('edit:index', document_id=document_id)


@decorators.belongs_to_document
@login_required(login_url='dashboard:login')
def update(request, document_id, section_id):
    section = get_object_or_404(models.Section, id=section_id)
    section.content = request.POST.get('content')
    section.modifier = request.user
    section.message = request.POST.get('message')
    section.save()

    utils.release_section(section_id)

    return redirect('edit:index', document_id=document_id)


@decorators.belongs_to_document
@login_required(login_url='dashboard:login')
def acquire(request, document_id):
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
        'current': section.editing.username,
        'content': section.content,
    })


@decorators.belongs_to_document
@login_required(login_url='dashboard:login')
def release(request, document_id):
    section_id = request.POST.get('sectionId')
    utils.release_section(section_id)

    return JsonResponse({
        'status': True
    })
