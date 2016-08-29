from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'apps.views.home', name='home'),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^accounts/', include('django.contrib.auth.urls', namespace="auth")),

    url(r'^TODO_name/', include('TODO_name.urls', namespace='TODO_name')),
    url(r'^$', 'apps.views.home'),
]