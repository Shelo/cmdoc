from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^document/', include('edit.urls', namespace='edit')),
    url(r'^section/', include('section.urls', namespace='section')),
    url(r'^render/', include('render.urls', namespace='render')),
    url(r'^tokens/', include('tokens.urls', namespace='tokens')),
    url(r'^', include('dashboard.urls', namespace='dashboard')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
