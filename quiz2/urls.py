"""Top level site urls."""
from django.conf.urls import patterns, include, url
from quiz2 import views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^quiz/', include('quiz2.apps.quiz.urls')),

    url(r'^user/account/$', views.user_account, name='user_account'),

    url(r'^user/password/reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    (r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    (r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect' : '/user/password/done/'}),
    (r'^user/password/done/$',
        'django.contrib.auth.views.password_reset_complete'),

)
