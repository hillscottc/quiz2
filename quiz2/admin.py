"""Top level Admin."""
from django.contrib import admin
from quiz2.apps.quiz.models import (Quiz, Question, Answer,
                                    Tag, QuestionTag, UserProfile)

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(QuestionTag)

## Not sure why this isn't working. But be careful trying to move it to a top model.
admin.site.register(UserProfile)

