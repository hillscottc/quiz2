from django.conf.urls import patterns, url
from quiz2.apps.quiz import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'questions/(?P<set_id>\d+)/$', views.questions_index, name='questions_index'),

    url(r'sets/$', views.questionsets_index, name='questionsets_index'),

    url(r'post_answer/(?P<qa_id>\d+)/$', views.post_answer, name='post_answer'),
    url(r'register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)
