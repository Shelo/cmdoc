from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^doc/', include('edit.urls', namespace='edit')),
    url(r'^', include('dashboard.urls', namespace='dashboard')),
]
