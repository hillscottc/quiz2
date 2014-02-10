"""Quiz urls."""
from django.conf.urls import patterns, url, include
from quiz2.apps.quiz import views
from quiz2.apps.quiz.admin import quiz_admin_site

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='quizapp_home'),
    url(r'^quiz/index/$', views.quiz_index, name='quiz_index'),
    url(r'^quiz/take/(?P<quiz_id>\d+)/$', views.quiz_take, name='quiz_take'),
    url(r'quiz/delete/(?P<quiz_id>\d+)/$', views.quiz_delete, name="quiz_delete"),
    url(r'quiz/add/$', views.quiz_add, name="quiz_add"),
    url(r'quiz/edit/(?P<quiz_id>\d+)/$', views.quiz_edit, name='quiz_edit'),


    url(r'answer/post/(?P<a_id>\d+)/$', views.answer_post, name='answer_post'),
    url(r'answer/manage/(?P<answer_id>\d+)/$', views.answer_manage, name='answer_manage'),
    url(r'answers/edit/(?P<question_id>\d+)/$', views.answers_edit, name='answers_edit'),
    url(r'answer/add/(?P<question_id>\d+)/$', views.answer_add, name='answer_add'),

    url(r'question/manage/(?P<question_id>\d+)/$', views.question_manage, name='question_manage'),


    url(r'question/add/(?P<quiz_id>\d+)/$', views.question_add, name='question_add'),

    url(r'log/$', views.log, name="log"),
    url(r'admin/', include(quiz_admin_site.urls)),
)


## Works, but unused for now
# url(r'manage_questions/(?P<quiz_id>\d+)/$', views.manage_questions),