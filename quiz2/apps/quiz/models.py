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


class Quiz(CommonModel):
    """Groups the questions."""
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ("user", "name")

    def __unicode__(self):
        return self.name


class Question(CommonModel):
    quiz = models.ForeignKey(Quiz)
    text = models.CharField(max_length=255, unique=True)

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
    text = models.CharField(max_length=50, unique=True)
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
