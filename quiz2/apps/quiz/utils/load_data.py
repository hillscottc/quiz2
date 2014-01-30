"""Model data for loading."""
from quiz2.apps.quiz.models import (Question, Answer, QuestionAnswer, Tag,
                                    QuestionTag, QuestionSet)
from django.contrib.auth.models import User

u = User.objects.get(pk=1)
qs = QuestionSet.objects.create(user=u, name="Test Set 1")


for i in range(0, 10):
    Answer.objects.create(text=str(i))


Tag.objects.create(text="Science")
Tag.objects.create(text="History")
Tag.objects.create(text="UnitedStates")
Tag.objects.create(text="Math")
Tag.objects.create(text="Geography")

q = Question.objects.create(text="How many planets are in our solar system?")
QuestionAnswer.objects.create(question=q, answer=Answer.objects.get(text="7"))
QuestionAnswer.objects.create(question=q, answer=Answer.objects.get(text="8"), correct=True)
QuestionAnswer.objects.create(question=q, answer=Answer.objects.get(text="9"))
QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Science"))

q = Question.objects.create(text="What is the fourth planet from the sun?")
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Neptune"))
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Earth"))
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Mars"), correct=True)
QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Science"))

q = Question.objects.create(text="How many sides on a triangle?")
QuestionAnswer.objects.create(question=q, answer=Answer.objects.get(text="3"), correct=True)
QuestionAnswer.objects.create(question=q, answer=Answer.objects.get(text="4"))
QuestionAnswer.objects.create(question=q, answer=Answer.objects.get(text="5"))
QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Math"))

q = Question.objects.create(text="What is the name of the first US president?")
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Washington"), correct=True)
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Lincoln"))
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Kennedy"))
QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="History"))
QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="UnitedStates"))

q = Question.objects.create(text="What is the name of the official national anthem of the USA?")
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="The Star-Spangled Banner"), correct=True)
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="America the Beautiful"))
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Stars and Stripes Forever"))
QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="UnitedStates"))

q = Question.objects.create(text="What is the capital city of Afghanistan?")
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Kabul"), correct=True)
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Falujah"))
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Darfur"))
QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Geography"))

q = Question.objects.create(text="Which two colours are on the flag of Poland?")
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Red and White"), correct=True)
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Red and Blue"))
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Red and Green"))
QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Geography"))

q = Question.objects.create(text="How many US states begin with the letter 'P'")
QuestionAnswer.objects.create(question=q, answer=Answer.objects.get(text="1"), correct=True)
QuestionAnswer.objects.create(question=q, answer=Answer.objects.get(text="2"))
QuestionAnswer.objects.create(question=q, answer=Answer.objects.get(text="3"))
QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="UnitedStates"))
QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Geography"))

q = Question.objects.create(text="Paraguay has borders with Brazil, Bolivia and which other country?")
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Argentina"), correct=True)
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Venezuela"))
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Belize"))
QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Geography"))

q = Question.objects.create(text="In which country is Mount Everest?")
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="Nepal"), correct=True)
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="China"))
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="India"))
QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Geography"))

q = Question.objects.create(text="What is the national currency of Egypt?")
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="The Pound"), correct=True)
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="The Lira"))
QuestionAnswer.objects.create(question=q, answer=Answer.objects.create(text="The Dollar"))
QuestionTag.objects.create(question=q, tag=Tag.objects.get(text="Geography"))


