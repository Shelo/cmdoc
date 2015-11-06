from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from edit import decorators
import edit.models
from tokens.forms import TokenForm
import tokens.models


@decorators.belongs_to_document
@login_required(login_url='dashboard:login')
def create(request, document_id):
    document = get_object_or_404(edit.models.Document, id=document_id)

    token_form = TokenForm(request.POST)

    if token_form.is_valid():
        token = token_form.save(commit=False)
        token.document_id = document.id
        token.save()

    return redirect(reverse('edit:index', kwargs={'document_id': document_id}) + "#fndtn-tokens")


@decorators.belongs_to_document
@login_required(login_url='dashboard:login')
def remove(request, document_id, token_key):
    token = get_object_or_404(tokens.models.Token, key=token_key)
    token.delete()

    return redirect(reverse('edit:index', kwargs={'document_id': document_id}) + "#fndtn-tokens")

@decorators.belongs_to_document
@login_required(login_url='dashboard:login')
def update(request):
    return None
