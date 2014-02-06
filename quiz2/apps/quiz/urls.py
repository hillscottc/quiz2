"""Quiz urls."""
from django.conf.urls import patterns, url, include
from quiz2.apps.quiz import views
from quiz2.apps.quiz.admin import quiz_admin_site

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # url(r'^$', views.home, name='home'),
    url(r'^$', views.quiz_index, name='quiz_index'),
    url(r'^quiz/(?P<quiz_id>\d+)/$', views.take_quiz, name='take_quiz'),
    url(r'^post_answer/(?P<a_id>\d+)/$', views.post_answer, name='post_answer'),


    url(r'manage_quiz/(?P<quiz_id>\d+)/$', views.manage_quiz),
    url(r'manage_question/(?P<question_id>\d+)/$', views.manage_question),



    url(r'manage_answer/(?P<answer_id>\d+)/$', views.manage_answer),
    # url(r'manage_answers/(?P<question_id>\d+)/$', views.manage_answers),


    # url(r'question_add/(?P<quiz_id>\d+)/$', views.question_add),

    ## Works, but unused for now
    # url(r'manage_questions/(?P<quiz_id>\d+)/$', views.manage_questions),

    url(r'admin/', include(quiz_admin_site.urls)),
)
