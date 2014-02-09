"""Model data for loading."""
from quiz2.apps.quiz.models import (Question, Answer, Tag, QuestionTag, Quiz)
from django.contrib.auth.models import User
from random import randint


def do_load():

    u, _ = User.objects.get_or_create(pk=1)
    quiz1 = Quiz.objects.create(user=u, name="Demo Quiz %s" % randint(1, 1000))
    print "Created quiz", quiz1

    Tag.objects.get_or_create(text="Science")
    Tag.objects.get_or_create(text="History")
    Tag.objects.get_or_create(text="UnitedStates")
    Tag.objects.get_or_create(text="Math")
    Tag.objects.get_or_create(text="Geography")

    q = Question.objects.create(text="What is the name of the first US president?", quiz=quiz1)
    Answer.objects.create(question=q, text="Washington", correct=True)
    Answer.objects.create(question=q, text="Lincoln")
    Answer.objects.create(question=q, text="Kennedy")
    QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="History"))
    QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="UnitedStates"))

    q = Question.objects.create(text="How many planets are in our solar system?", quiz=quiz1)
    Answer.objects.create(question=q, text="7")
    Answer.objects.create(question=q, text="8", correct=True)
    Answer.objects.create(question=q, text="9")
    QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Science"))
    
    q = Question.objects.create(text="What is the fourth planet from the sun?", quiz=quiz1)
    Answer.objects.create(question=q, text="Neptune")
    Answer.objects.create(question=q, text="Earth")
    Answer.objects.create(question=q, text="Mars", correct=True)
    QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Science"))
    
    q = Question.objects.create(text="How many sides on a triangle?", quiz=quiz1)
    Answer.objects.create(question=q, text="3", correct=True)
    Answer.objects.create(question=q, text="4")
    Answer.objects.create(question=q, text="5")
    QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Math"))

    q = Question.objects.create(text="What is the name of the official national anthem of the USA?", quiz=quiz1)
    Answer.objects.create(question=q, text="The Star-Spangled Banner", correct=True)
    Answer.objects.create(question=q, text="America the Beautiful")
    Answer.objects.create(question=q, text="Stars and Stripes Forever")
    QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="UnitedStates"))
    
    q = Question.objects.create(text="What is the capital city of Afghanistan?", quiz=quiz1)
    Answer.objects.create(question=q, text="Kabul", correct=True)
    Answer.objects.create(question=q, text="Falujah")
    Answer.objects.create(question=q, text="Darfur")
    QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Geography"))
    
    q = Question.objects.create(text="Which two colours are on the flag of Poland?", quiz=quiz1)
    Answer.objects.create(question=q, text="Red and White", correct=True)
    Answer.objects.create(question=q, text="Red and Blue")
    Answer.objects.create(question=q, text="Red and Green")
    QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Geography"))
    
    q = Question.objects.create(text="How many US states begin with the letter 'P'", quiz=quiz1)
    Answer.objects.create(question=q, text="1", correct=True)
    Answer.objects.create(question=q, text="2")
    Answer.objects.create(question=q, text="3")
    QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="UnitedStates"))
    QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Geography"))
    
    q = Question.objects.create(text="Paraguay has borders with Brazil, Bolivia and which other country?", quiz=quiz1)
    Answer.objects.create(question=q, text="Argentina", correct=True)
    Answer.objects.create(question=q, text="Venezuela")
    Answer.objects.create(question=q, text="Belize")
    QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Geography"))
    
    q = Question.objects.create(text="In which country is Mount Everest?", quiz=quiz1)
    Answer.objects.create(question=q, text="Nepal", correct=True)
    Answer.objects.create(question=q, text="China")
    Answer.objects.create(question=q, text="India")
    QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Geography"))
    
    q = Question.objects.create(text="What is the national currency of Egypt?", quiz=quiz1)
    Answer.objects.create(question=q, text="The Pound", correct=True)
    Answer.objects.create(question=q, text="The Lira")
    Answer.objects.create(question=q, text="The Dollar")
    QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Geography"))


