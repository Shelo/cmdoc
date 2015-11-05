import functools
from edit import models
from django.http.response import HttpResponseForbidden


def belongs_to_document(method):
    @functools.wraps(method)
    def wrapper(request, id, *args, **kwargs):
        user = request.user
        document = models.Document.objects.filter(id=id).get()

        if document.has_user(user):
            return method(request, id, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return wrapper


def owner_of_document(method):
    @functools.wraps(method)
    def wrapper(request, id, *args, **kwargs):
        user = request.user
        document = models.Document.objects.filter(id=id).get()

        if document.owner == user:
            return method(request, id, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return wrapper
