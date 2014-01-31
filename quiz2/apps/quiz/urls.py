"""Quiz urls."""
from django.conf.urls import patterns, url, include
from quiz2.apps.quiz import views
from quiz2.apps.quiz.admin import quiz_admin_site

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'questions/(?P<set_id>\d+)/$', views.questions_index, name='questions_index'),

    url(r'sets/$', views.questionsets_index, name='questionsets_index'),

    url(r'post_answer/(?P<qa_id>\d+)/$', views.post_answer, name='post_answer'),

    url(r'admin/', include(quiz_admin_site.urls)),

)
