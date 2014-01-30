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


class QuestionSet(CommonModel):
    """Grouped questions."""
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ("user", "name")

    def __unicode__(self):
        return self.name


class Question(CommonModel):
    text = models.CharField(max_length=255, unique=True)
    questionset = models.ForeignKey(QuestionSet)

    class Meta:
        unique_together = ("text", "questionset")

    @property
    def questionanswers(self):
        return self.questionanswer_set.all()

    @property
    def questiontags(self):
        # return self.questiontag_set.all()
        return [qt.tag for qt in self.questiontag_set.all()]

    def __unicode__(self):
        return self.text


class Answer(CommonModel):
    text = models.CharField(max_length=50, unique=True)
    notes = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.text


class QuestionAnswer(CommonModel):
    question = models.ForeignKey(Question)
    answer = models.ForeignKey(Answer)
    correct = models.BooleanField(default=False)

    def __unicode__(self):
        return "{}...{}...{}".format(self.question.text[:50], self.answer.text[:30], self.correct)


class Tag(CommonModel):
    text = models.CharField(max_length=25, unique=True)

    def __unicode__(self):
        return self.text


class QuestionTag(CommonModel):
    question = models.ForeignKey(Question)
    tag = models.ForeignKey(Tag)

    def __unicode__(self):
        return "{}...{}".format(self.question.text[:30], self.tag.text)
