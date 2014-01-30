from django.conf.urls import patterns, include, url
from quiz2.apps.quiz import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quiz2.apps.quiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', views.home, name='home'),
    url(r'questions/$', views.questions_index, name='questions_index'),

    url(r'question/(?P<question_id>\d+)/$', views.question, name='question'),

    url(r'post_answer/(?P<question_id>\d+)/(?P<qa_id>\d+)/$', views.post_answer, name='post_answer'),



)
