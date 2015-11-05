from django.conf.urls import url
from section import views

urlpatterns = [
    url(
        r'^(?P<document_id>[0-9]+)/create/',
        views.create,
        name='create'
    ),

    url(
        r'^(?P<document_id>[0-9]+)/remove/(?P<section_id>[0-9]+)/',
        views.remove,
        name='remove'
    ),

    url(
        r'^(?P<document_id>[0-9]+)/update/(?P<section_id>[0-9]+)/',
        views.update,
        name='update'
    ),

    url(
        r'^(?P<document_id>[0-9]+)/acquire/',
        views.acquire,
        name='acquire'
    ),

    url(
        r'^(?P<document_id>[0-9]+)/release/',
        views.release,
        name='release'
    ),
]
