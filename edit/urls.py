from django.conf.urls import url
from edit import views

urlpatterns = [
    url(r'^(?P<id>[0-9]+)$', views.index, name='index'),

    url(r'^new/$', views.new, name='new_document'),
    url(r'^(?P<id>[0-9]+)/delete/$', views.delete, name='proc_document_delete'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<id>[0-9]+)/edit/title/$', views.edit_title, name='edit_title'),
    url(r'^(?P<id>[0-9]+)/edit/description/$', views.edit_description, name='edit_description'),
    url(r'^(?P<id>[0-9]+)/edit/rem_coll/(?P<username>.+)$', views.remove_collaborator,
        name='remove_collaborator'),
    url(r'^(?P<id>[0-9]+)/edit/add_coll/$', views.add_collaborator, name='add_collaborator'),
    url(r'^(?P<id>[0-9]+)/edit/message/$', views.send_message, name='send_message'),

    url(r'^(?P<id>[0-9]+)/sec/create', views.create_section, name='section_create'),
    url(r'^(?P<id>[0-9]+)/sec/(?P<section_id>[0-9]+)/delete', views.delete_section,
        name='proc_document_section_delete'),

    url(r'^(?P<id>[0-9]+)/sec/(?P<section_id>[0-9]+)/update', views.update_section,
        name='section_update'),

    url(r'^(?P<id>[0-9]+)/html/$', views.render_html, name='render_html'),
    url(r'^(?P<id>[0-9]+)/raw/', views.render_raw, name='render_raw'),

    url(r'^(?P<id>[0-9]+)/sync/start/', views.sync_sec_request, name='sync_request'),
    url(r'^(?P<id>[0-9]+)/sync/cancel/', views.sync_sec_cancel, name='sync_cancel'),
]
