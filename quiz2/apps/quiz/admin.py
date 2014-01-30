from django.contrib import admin
from quiz2.apps.quiz.models import Question, Answer, QuestionAnswer, Tag, QuestionTag


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionAnswer)
admin.site.register(Tag)
admin.site.register(QuestionTag)