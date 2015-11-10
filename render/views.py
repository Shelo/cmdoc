import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
import subprocess
from edit import decorators, models
import tempfile


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


@decorators.belongs_to_document
@login_required(login_url='dashboard:login')
def latex(request, document_id):
    document = get_object_or_404(models.Document, id=document_id)
    sections = document.parsed_content()

    content = '\n\n'.join([section.content for section in sections])

    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(content)
    temp.close()

    latex_code = subprocess.check_output(["pandoc", "-f", "markdown", "-t", "latex", temp.name])

    os.remove(temp.name)

    return HttpResponse(latex_code, content_type='text/plain')


@decorators.belongs_to_document
@login_required(login_url='dashboard:login')
def pdf(request, document_id):
    document = get_object_or_404(models.Document, id=document_id)
    sections = document.parsed_content()

    content = '\n\n'.join([section.content for section in sections])

    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(content)
    temp.close()

    output_pdf = os.path.join(settings.STATIC_URL, str(document_id)) + ".pdf"

    subprocess.check_output([
        "pandoc",
        "-f", "markdown",
        "-t", "latex",
        "-o", output_pdf,
        temp.name
    ])

    os.remove(temp.name)

    return HttpResponseRedirect(output_pdf)