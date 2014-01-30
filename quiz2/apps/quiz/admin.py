from django.contrib import admin
from quiz2.apps.quiz.models import (Question, Answer, QuestionAnswer,
                                    Tag, QuestionTag, UserProfile, QuestionSet)


# class QuestionSetAdmin(admin.ModelAdmin):
#     fields = ('name',)
#
#     def save_model(self, request, obj, form, change):
#         obj.user = request.user
#         obj.save()


# admin.site.register(QuestionSet, QuestionSetAdmin)
admin.site.register(QuestionSet)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionAnswer)
admin.site.register(Tag)
admin.site.register(QuestionTag)
admin.site.register(UserProfile)




