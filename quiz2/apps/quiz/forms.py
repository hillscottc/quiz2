from django.forms import (ModelForm, CharField, PasswordInput, Textarea)
from django.forms.models import modelformset_factory
from django.contrib.auth.models import User
from quiz2.apps.quiz.models import Question, UserProfile, Answer, Quiz


class UserForm(ModelForm):
    password = CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        # fields = ('website', 'picture')
        fields = ('website',)


class AnswerForm(ModelForm):
    class Meta:
        model = Answer


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        exclude = ('created_at', 'updated_at')


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        # exclude = ('created_at', 'updated_at')
        fields = ('text', 'quiz')
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        # self.fields['text'].label = 'Question text:'
        # if not user.is_authenticated():
        #     pass

QuestionFormSet = modelformset_factory(
        Question,
        fields=('text',),
        widgets = {'text': Textarea(attrs={'cols': 80, 'rows': 2}), },
        can_delete=True,
        # can_order=True,
        extra=0)