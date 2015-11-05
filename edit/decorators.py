import functools
from edit import models
from django.http.response import HttpResponseForbidden


def belongs_to_document(method):
    @functools.wraps(method)
    def wrapper(request, document_id, *args, **kwargs):
        user = request.user
        document = models.Document.objects.filter(id=document_id).get()

        if document.has_user(user):
            return method(request, document_id, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return wrapper


def owner_of_document(method):
    @functools.wraps(method)
    def wrapper(request, document_id, *args, **kwargs):
        user = request.user
        document = models.Document.objects.filter(id=document_id).get()

        if document.owner == user:
            return method(request, document_id, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return wrapper
