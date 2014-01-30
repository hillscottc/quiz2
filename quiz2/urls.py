from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'quiz2.apps.quiz.views.home', name='home'),
    url(r'^quiz/', include('quiz2.apps.quiz.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
