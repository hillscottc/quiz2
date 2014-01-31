"""Top level Admin."""
from django.contrib import admin
from quiz2.apps.quiz.models import (Question, Answer, QuestionAnswer,
                                    Tag, QuestionTag, QuestionSet, UserProfile)

admin.site.register(QuestionSet)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionAnswer)
admin.site.register(Tag)
admin.site.register(QuestionTag)

## Not sure why this isn't working. But be careful trying to move it to a top model.
admin.site.register(UserProfile)

