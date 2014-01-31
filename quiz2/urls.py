"""Top level site urls."""
from django.conf.urls import patterns, include, url
from quiz2 import views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', 'quiz2.apps.quiz.views.home', name='home'),

    url(r'register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^quiz/', include('quiz2.apps.quiz.urls')),
)
