from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$',
        views.index,
        name='index'
    ),

    url(
        r'^dashboard/$',
        views.dashboard,
        name='dashboard'
    ),

    url(
        r'^documents/$',
        views.documents,
        name='documents'
    ),

    url(
        r'^collaboration/$',
        views.collaboration,
        name='collaboration'
    ),

    url(
        r'^login/$',
        views.login,
        name='login'
    ),

    url(
        r'^session/$',
        views.session,
        name='session'
    ),

    url(
        r'^logout/$',
        views.logout,
        name='logout'
    ),

]
