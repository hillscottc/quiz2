from django import forms
from django.contrib.auth.models import User
from quiz2.apps.quiz.models import Question, UserProfile, Answer, Quiz


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        # fields = ('website', 'picture')
        fields = ('website',)


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        exclude = ('created_at', 'updated_at')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        # exclude = ('created_at', 'updated_at')
        fields = ('text', )
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        # self.fields['text'].label = 'Question text:'
        # if not user.is_authenticated():
        #     pass

