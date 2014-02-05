from django.shortcuts import HttpResponse, render, render_to_response
from quiz2.apps.quiz.models import Quiz, Question, Answer
from quiz2.apps.quiz.forms import QuestionForm, AnswerForm

from django.contrib.auth.decorators import login_required
from django.forms.models import formset_factory, inlineformset_factory, modelformset_factory

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


@login_required
def question_add(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            return HttpResponse("Thanks for answering. You posted %s" % request.REQUEST)
    else:
        form = QuestionForm(request.user,
                            initial={'quiz': quiz})

    return render(request, 'quiz/question/add.html', {
        'quiz': quiz, 'form': form,
    })


def manage_questions(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    QuestionFormSet = modelformset_factory(
        Question, fields=('text',), can_delete=True,
        can_order=True, extra=0)

    if request.method == 'POST':
        formset = QuestionFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            pass
    else:
        formset = QuestionFormSet(
            queryset=Question.objects.filter(quiz=quiz))

    return render_to_response('quiz/question/manage_questions.html',
                              {'quiz': quiz, 'formset': formset})

def manage_answers(request, question_id):
    question = Question.objects.get(pk=question_id)
    AnswerFormSet = modelformset_factory(
        Answer, fields=('text',), can_delete=True, can_order=True,
        extra=0)

    if request.method == 'POST':
        formset = AnswerFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            pass
    else:
        formset = AnswerFormSet(queryset=Answer.objects.filter(question=question))

    return render_to_response('quiz/question/manage_answers.html',
                              {'question': question,
                               'formset': formset})
