from django import forms
from django.contrib.auth.models import User
from quiz2.apps.quiz.models import UserProfile, Question, QuestionAnswer
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


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question


class QuestionAnswerForm(forms.ModelForm):
    class Meta:
        model = QuestionAnswer

QuestionAnswerFormSet = inlineformset_factory(Question, QuestionAnswer, extra=1)




