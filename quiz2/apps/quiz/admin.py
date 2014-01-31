from django.contrib import admin
from quiz2.apps.quiz.models import (Question, Answer, QuestionAnswer,
                                    Tag, QuestionTag, UserProfile, QuestionSet)


admin.site.register(QuestionSet)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionAnswer)
admin.site.register(Tag)
admin.site.register(QuestionTag)
admin.site.register(UserProfile)


# from django.contrib.admin.sites import AdminSite
#
# class MyAdminSite(AdminSite):
#     pass
#     #or overwrite some methods for different functionality
#
# quiz_admin_site = MyAdminSite()
#
# quiz_admin_site.register(QuestionSet)
# quiz_admin_site.register(Question)
# quiz_admin_site.register(Answer)
# quiz_admin_site.register(QuestionAnswer)
# quiz_admin_site.register(Tag)
# quiz_admin_site.register(QuestionTag)
# quiz_admin_site.register(UserProfile)


