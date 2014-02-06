from django import forms
from django.contrib.auth.models import User
from quiz2.apps.quiz.models import Question, UserProfile, Answer
from django.forms.models import inlineformset_factory


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


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ('created_at', 'updated_at')

    ## Init this one with user also. MAybe not needed.
    def __init__(self, user, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        if not user.is_authenticated():
            # self.fields['captcha'] = CaptchaField()
            pass

