from django.conf.urls import url
from edit import views

urlpatterns = [
    url(
        r'^(?P<document_id>[0-9]+)$',
        views.index,
        name='index'
    ),

    url(
        r'^new/$',
        views.new,
        name='new'
    ),

    url(
        r'^(?P<document_id>[0-9]+)/remove/$',
        views.remove,
        name='remove'
    ),

    url(
        r'^create/$',
        views.create,
        name='create'
    ),

    url(
        r'^(?P<document_id>[0-9]+)/update/title/$',
        views.update_title,
        name='update_title'
    ),

    url(
        r'^(?P<document_id>[0-9]+)/update/description/$',
        views.update_description,
        name='update_description'
    ),

    url(
        r'^(?P<document_id>[0-9]+)/rem/coll/(?P<username>.+)$',
        views.remove_collaborator,
        name='remove_collaborator'
    ),

    url(
        r'^(?P<document_id>[0-9]+)/add/coll/$',
        views.add_collaborator,
        name='add_collaborator'
    ),

    url(
        r'^(?P<document_id>[0-9]+)/message/$',
        views.send_message,
        name='send_message'
    ),
]
