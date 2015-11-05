from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.web.index, name='index'),

    url(r'^new/$', views.document.new, name='new_document'),
    url(r'^(?P<id>[0-9]+)/delete/$', views.document.delete, name='proc_document_delete'),
    url(r'^create/$', views.document.create, name='document_create'),
    url(r'^(?P<id>[0-9]+)/edit/$', views.document.edit, name='edit'),
    url(r'^(?P<id>[0-9]+)/edit/title/$', views.document.edit_title, name='edit_title'),
    url(r'^(?P<id>[0-9]+)/edit/description/$', views.document.edit_description, name='edit_description'),
    url(r'^(?P<id>[0-9]+)/edit/addcoll/(?P<username>.+)$', views.document.remove_collaborator,
        name='remove_collaborator'),
    url(r'^(?P<id>[0-9]+)/edit/removecoll/$', views.document.add_collaborator, name='add_collaborator'),
    url(r'^(?P<id>[0-9]+)/edit/message/$', views.document.send_message, name='send_message'),

    url(r'^(?P<id>[0-9]+)/sec/create', views.document.create_section, name='section_create'),
    url(r'^(?P<id>[0-9]+)/sec/(?P<section_id>[0-9]+)/delete', views.document.delete_section,
        name='proc_document_section_delete'),

    url(r'^(?P<id>[0-9]+)/sec/(?P<section_id>[0-9]+)/update', views.document.update_section,
        name='section_update'),

    url(r'^(?P<id>[0-9]+)/html/$', views.document.render_html, name='render_html'),
    url(r'^(?P<id>[0-9]+)/raw/', views.document.render_raw, name='render_raw'),

    url(r'^(?P<id>[0-9]+)/sync/start/', views.document.sync_sec_request, name='sync_request'),
    url(r'^(?P<id>[0-9]+)/sync/cancel/', views.document.sync_sec_cancel, name='sync_cancel'),
]
