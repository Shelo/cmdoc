from django.conf.urls import url
from tokens import views

urlpatterns = [
    url(
        r'^(?P<document_id>[0-9]+)/create/',
        views.create,
        name='create'
    ),

    url(
        r'^(?P<document_id>[0-9]+)/remove/(?P<token_key>[a-zA-Z_-]+)/',
        views.remove,
        name='remove'
    ),

    url(
        r'^(?P<document_id>[0-9]+)/update/(?P<token_key>[0-9]+)/',
        views.update,
        name='update'
    ),
]
