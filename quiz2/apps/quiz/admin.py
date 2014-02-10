"""Quiz section admin."""
from quiz2.apps.quiz.models import Quiz, Question, Answer, Tag, QuestionTag, Organization
from django.contrib.admin.sites import AdminSite


class QuizAdminSite(AdminSite):
    pass

quiz_admin_site = QuizAdminSite('apps.quiz')

quiz_admin_site.register(Quiz)
quiz_admin_site.register(Question)
quiz_admin_site.register(Answer)
quiz_admin_site.register(Tag)
quiz_admin_site.register(QuestionTag)
quiz_admin_site.register(Organization)

# quiz_admin_site.register(UserProfile)


