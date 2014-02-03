from django.shortcuts import HttpResponse, render
from quiz2.apps.quiz.models import Quiz, Question, Answer
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory, inlineformset_factory


def quiz_index(request):
    """List all quizzes."""
    context = {'quiz_list': Quiz.objects.all()}
    return render(request, 'quiz/index.html', context)


def quiz_questions(request, quiz_id):
    """List questions for quiz."""
    if request.method == 'POST':
        return HttpResponse("You posted %s" % request.REQUEST)
        #request.POST.get("title", "")
    else:
        quiz = Quiz.objects.get(pk=quiz_id)
        context = {'quiz': quiz,
                   'q_list': Question.objects.filter(quiz=quiz)}
        return render(request, 'quiz/question/q_list.html', context)


def post_answer(request, a_id):
    """Answer a question."""
    answer = Answer.objects.get(pk=a_id)
    if answer.correct:
        response = "Correct!"
    else:
        response = "Wrong answer."
    return HttpResponse(response)


# @login_required
# def question_add(request, quiz_id):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             return HttpResponse("Thanks for answering. You posted %s" % request.REQUEST)
#     else:
#         quiz = Quiz.objects.get(pk=quiz_id)
#         form = QuestionForm(initial={"quiz": quiz})
#
#     return render(request, 'quiz/question/add.html', {
#         'form': form,
#     })