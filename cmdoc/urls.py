from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^document/', include('edit.urls', namespace='edit')),
    url(r'^section/', include('section.urls', namespace='section')),
    url(r'^', include('dashboard.urls', namespace='dashboard')),
]
