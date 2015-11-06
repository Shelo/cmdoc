from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from edit import decorators, models


@decorators.belongs_to_document
@login_required(login_url='dashboard:login')
def raw(request, document_id):
    document = get_object_or_404(models.Document, id=document_id)
    sections = document.parsed_content()

    content = '\n\n'.join([section.content for section in sections])

    return HttpResponse(content, content_type='text/plain')


@decorators.belongs_to_document
@login_required(login_url='dashboard:login')
def html(request, document_id):
    document = get_object_or_404(models.Document, id=document_id)

    return render(request, 'render/render.html', {
        'document': document,
        'sections': document.parsed_content()
    })
