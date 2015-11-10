from django.conf.urls import url
from render import views

urlpatterns = [
    url(
        r'^(?P<document_id>[0-9]+)/html/$',
        views.html,
        name='html'
    ),

    url(
        r'^(?P<document_id>[0-9]+)/raw/',
        views.raw,
        name='raw'
    ),

    url(
        r'^(?P<document_id>[0-9]+)/latex/',
        views.latex,
        name='latex'
    ),

    url(
        r'^(?P<document_id>[0-9]+)/pdf/',
        views.pdf,
        name='pdf'
    ),
]
