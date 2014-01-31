from django.shortcuts import HttpResponse, render
from quiz2.apps.quiz.models import Question, QuestionAnswer, QuestionSet


def home(request):
    return render(request, 'index.html', {})


def questionsets_index(request):
    questionset_list = QuestionSet.objects.all()
    context = {'questionset_list': questionset_list}
    return render(request, 'quiz/questions/sets_list.html', context)


def questions_index(request, set_id):
    if request.method == 'POST':
        return HttpResponse("Thanks for answering. You posted %s" % request.REQUEST)
        #request.POST.get("title", "")
    else:
        questionset = QuestionSet.objects.get(pk=set_id)
        question_list = Question.objects.filter(questionset=questionset)
        context = {'questionset': questionset, 'question_list': question_list}
        return render(request, 'quiz/questions/questions_list.html', context)


def post_answer(request, qa_id):
    qa = QuestionAnswer.objects.get(pk=qa_id)
    if qa.correct:
        response = "Correct!"
    else:
        response = "Wrong answer."
    return HttpResponse(response)



