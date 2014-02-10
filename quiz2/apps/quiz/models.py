from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes.
    website = models.URLField(blank=True)
    # picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Organization(CommonModel):
    """i.e. Mirman. To group the quizzes."""
    name = models.CharField(max_length=150, unique=True)

    def __unicode__(self):
        return self.name


class Quiz(CommonModel):
    """Groups the questions."""
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, blank=True, null=True)

    # version = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("user", "name")

    def __unicode__(self):
        return self.name


class QuizLog(CommonModel):
    """Log with foreign keys"""
    quiz = models.ForeignKey(Quiz)
    taker = models.ForeignKey(User, null=True)
    MESSAGE_CHOICES = (('STARTED', 'STARTED'), ('COMPLETED', 'COMPLETED'))
    message = models.CharField(max_length=10, choices=MESSAGE_CHOICES)


class RawLog(CommonModel):
    """Log without foreign keys"""
    message = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%s %s" % (self.created_at.strftime('%c'),
                           self.message)


class Question(CommonModel):
    quiz = models.ForeignKey(Quiz)
    text = models.CharField(max_length=255,
                            verbose_name='question text',)

    class Meta:
        unique_together = ("text", "quiz")

    @property
    def answers(self):
        return self.answer_set.all()

    @property
    def tags(self):
        # return self.questiontag_set.all()
        return [qt.tag for qt in self.questiontag_set.all()]

    def __unicode__(self):
        return self.text


class Answer(CommonModel):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=50)
    correct = models.BooleanField(default=False)
    notes = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.text

    class Meta:
        unique_together = ("question", "text")


class Tag(CommonModel):
    text = models.CharField(max_length=25, unique=True)

    def __unicode__(self):
        return self.text


class QuestionTag(CommonModel):
    question = models.ForeignKey(Question)
    tag = models.ForeignKey(Tag)

    def __unicode__(self):
        return "{}...{}".format(self.question.text[:30], self.tag.text)

    class Meta:
        unique_together = ("question", "tag")


