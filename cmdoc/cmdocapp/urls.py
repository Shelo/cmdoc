from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.web.index, name='index'),
    url(r'^documents/$', views.web.documents, name='documents'),
    url(r'^collaboration/$', views.web.collaboration, name='collaboration'),
    url(r'^dashboard/$', views.web.dashboard, name='dashboard'),

    url(r'^doc/new/$', views.document.new, name='new_document'),
    url(r'^doc/(?P<id>[0-9]+)/delete/$', views.document.delete, name='proc_document_delete'),
    url(r'^doc/new/send/$', views.document.send_new, name='proc_new_document'),
    url(r'^doc/(?P<id>[0-9]+)/edit/$', views.document.edit, name='edit'),
    url(r'^doc/(?P<id>[0-9]+)/edit/title/$', views.document.edit_title, name='edit_title'),
    url(r'^doc/(?P<id>[0-9]+)/edit/description/$', views.document.edit_description, name='edit_description'),
    url(r'^doc/(?P<id>[0-9]+)/edit/addcoll/(?P<username>.+)$', views.document.remove_collaborator,
        name='remove_collaborator'),
    url(r'^doc/(?P<id>[0-9]+)/edit/removecoll/$', views.document.add_collaborator, name='add_collaborator'),
    url(r'^doc/(?P<id>[0-9]+)/edit/message/$', views.document.send_message, name='send_message'),

    url(r'^doc/(?P<id>[0-9]+)/sec/new/send$', views.document.send_new_section, name='proc_document_section_new'),
    url(r'^doc/(?P<id>[0-9]+)/sec/(?P<section_id>[0-9]+)/delete', views.document.delete_section,
        name='proc_document_section_delete'),
    url(r'^doc/(?P<id>[0-9]+)/sec/(?P<section_id>[0-9]+)/edit', views.document.edit_section,
        name='proc_document_section_edit'),

    url(r'^doc/(?P<id>[0-9]+)/html/$', views.document.render_html, name='render_html'),
    url(r'^doc/(?P<id>[0-9]+)/raw/', views.document.render_raw, name='render_raw'),

    url(r'doc/(?P<id>[0-9]+)/sync/start/', views.document.sync_sec_request, name='sync_request'),
    url(r'doc/(?P<id>[0-9]+)/sync/cancel/', views.document.sync_sec_cancel, name='sync_cancel'),

    url(r'^login/$', views.web.login, name='login'),
    url(r'^login/send/$', views.web.send_login, name='process_login'),
    url(r'^logout/$', views.web.send_logout, name='process_logout'),
]
