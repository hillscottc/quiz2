from django.shortcuts import HttpResponse, render, get_object_or_404
from quiz2.apps.quiz.models import Question, QuestionAnswer


def home(request):
    return HttpResponse("Hello, world.")


def questions_index(request):
    if request.method == 'POST':
        return HttpResponse("Thanks for answering. You posted %s" % request.REQUEST)
        #request.POST.get("title", "")
    else:
        question_list = Question.objects.all()
        context = {'question_list': question_list}
        return render(request, 'questions/index.html', context)


def question(request, question_id):
    if request.method == 'POST':
        return HttpResponse("Thanks for answering question %s" % question_id)
    else:
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'questions/question.html', {'question': question})


def post_answer(request, question_id, qa_id):
    qa = QuestionAnswer.objects.get(pk=qa_id)
    if qa.correct:
        response = "Correct!"
    else:
        response = "Wrong answer."
    return HttpResponse(response)

