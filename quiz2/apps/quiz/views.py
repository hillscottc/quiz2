from django.shortcuts import HttpResponse, render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from quiz2.apps.quiz.models import Quiz, Question, Answer
from quiz2.apps.quiz.forms import QuestionForm, AnswerForm

from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.forms import HiddenInput


def quiz_index(request):
    """List all quizzes."""
    context = {'quiz_list': Quiz.objects.all()}
    return render(request, 'quiz/index.html', context)


def take_quiz(request, quiz_id):
    """List questions for quiz."""
    if request.method == 'POST':
        return HttpResponse("You posted %s" % request.REQUEST)
        #request.POST.get("title", "")
    else:
        quiz = Quiz.objects.get(pk=quiz_id)
        context = {'quiz': quiz,
                   'q_list': Question.objects.filter(quiz=quiz)}
        return render(request, 'quiz/take_quiz.html', context)


def post_answer(request, a_id):
    """Answer a question."""
    answer = Answer.objects.get(pk=a_id)
    if answer.correct:
        response = "<strong>Correct!</strong> Great job."
    else:
        response = "<strong>Sorry,</strong> wrong answer."
    return HttpResponse(response)


@login_required
def manage_quiz(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    QuestionFormSet = modelformset_factory(
        Question, fields=('text',),
        can_delete=True, can_order=True, extra=0)

    if request.method == 'POST':
        formset = QuestionFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            pass
    else:
        formset = QuestionFormSet(
            queryset=Question.objects.filter(quiz=quiz))

    return render(request, 'quiz/manage_quiz.html',
                  {'quiz': quiz, 'formset': formset})


@login_required
def manage_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    quiz = question.quiz
    answers = Answer.objects.filter(question=question)
    if request.method == 'POST':
        if 'delete' in request.POST:
            question.delete()
            return HttpResponseRedirect('/quiz/manage_quiz/%s/' % quiz.id)
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            # return HttpResponse("Thanks for answering. You posted %s" % request.REQUEST)
            return HttpResponseRedirect('/quiz/manage_quiz/%s/' % quiz.id)
    else:
        form = QuestionForm(initial={'quiz': question.quiz,
                                     'text': question.text,
                                     'answers': Answer.objects.filter(question=question)})
        form.fields['quiz'].widget = HiddenInput()

    return render(request, 'quiz/question/manage_question.html',
                  {'form': form,
                   'quiz': quiz,
                   'question_id': question.id,
                   'answers': answers})


@login_required
def manage_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    question = Question.objects.get(answer=answer)
    # quiz = Quiz.objects.get(question=question)
    if request.method == 'POST':
        if 'delete' in request.POST:
            answer.delete()
            return HttpResponseRedirect('/quiz/manage_question/%s/' % question.id)
        # form = AnswerForm(request.POST)
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            # return HttpResponse("Thanks for answering. You posted %s" % request.REQUEST)
            # form = AnswerForm(request.POST, instance=answer)
            form.save()
            return HttpResponseRedirect('/quiz/manage_question/%s/' % question.id)
    else:
        form = AnswerForm(initial={'question': question,
                                   'text': answer.text,
                                   'correct': answer.correct,
                                   'notes': answer.notes})
        form.fields['question'].widget = HiddenInput()

    return render(request, 'quiz/answer/manage_answer.html',
                  {'form': form,
                   'answer_id': answer.id,
                   'question': question})


@login_required
def question_add(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse('manage_quiz',  kwargs={'quiz_id': quiz_id}))
            return HttpResponseRedirect('/quiz/manage_quiz/%s/' % quiz_id)
    else:
        form = QuestionForm(initial={'quiz': quiz,
                                     'user': request.user})
        form.fields['quiz'].widget = HiddenInput()

    return render(request, 'quiz/question/add.html',
                  {'quiz': quiz, 'form': form})



@login_required
def answer_add(request, question_id):
    question = Question.objects.get(pk=question_id)
    # quiz = Quiz.objects.get(question=question)
    if request.method == 'POST':
        form = AnswerForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            # return HttpResponse("Saved! You posted %s" % request.REQUEST)
            return HttpResponseRedirect('/quiz/manage_question/%s/' % question_id)

    else:
        form = AnswerForm(initial={'question': question})
        form.fields['question'].widget = HiddenInput()

    return render(request, 'quiz/answer/add.html',
                  {'question': question,
                   'form': form})

## This works, but not used right now. Uses formset.
# def manage_questions(request, quiz_id):
#     quiz = Quiz.objects.get(pk=quiz_id)
#     QuestionFormSet = modelformset_factory(
#         Question, fields=('text',), can_delete=True,
#         can_order=True, extra=0)
#
#     if request.method == 'POST':
#         formset = QuestionFormSet(request.POST, request.FILES)
#         if formset.is_valid():
#             # do something with the formset.cleaned_data
#             pass
#     else:
#         formset = QuestionFormSet(
#             queryset=Question.objects.filter(quiz=quiz))
#
#     return render(request, 'quiz/question/manage_questions.html',
#                               {'quiz': quiz, 'formset': formset})
#
# def manage_answers(request, question_id):
#     question = Question.objects.get(pk=question_id)
#     AnswerFormSet = modelformset_factory(
#         Answer, fields=('text',), can_delete=True, can_order=True,
#         extra=0)
#
#     if request.method == 'POST':
#         formset = AnswerFormSet(request.POST, request.FILES)
#         if formset.is_valid():
#             # do something with the formset.cleaned_data
#             pass
#     else:
#         formset = AnswerFormSet(queryset=Answer.objects.filter(question=question))
#
#     return render(request, 'quiz/question/manage_answers.html',
#                               {'question': question,
#                                'formset': formset})
