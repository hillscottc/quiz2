from django.shortcuts import HttpResponse, render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from quiz2.apps.quiz.models import Quiz, Question, Answer, RawLog
from quiz2.apps.quiz.forms import QuestionForm, AnswerForm, QuizForm
from quiz2.apps.quiz.quiz_mgr import log_message

from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.forms import HiddenInput, Textarea
from django.contrib import messages


def home(request):
    return render(request, 'quizapp/home.html', {})


def log(request):
    """The log page."""
    log_list = RawLog.objects.all().order_by('-created_at')[:50]
    return render(request, 'quizapp/log.html', {'log_list': log_list})


def quiz_index(request):
    """List all quizzes."""
    context = {'quiz_list': Quiz.objects.all()}
    return render(request, 'quizapp/quiz/index.html', context)


def quiz_add(request):
    if request.method == 'POST':
        form = QuizForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('quizapp:quiz_index'))
    else:
        form = QuizForm(initial={'user': request.user})
        form.fields['user'].widget = HiddenInput()

    return render(request, 'quizapp/quiz/add.html', {'form': form})


def quiz_take(request, quiz_id):
    """List questions for quiz."""
    if request.method == 'POST':
        return HttpResponse("You posted %s" % request.REQUEST)
        #request.POST.get("title", "")
    else:
        log_message(message="started a quiz", taker=request.user)
        quiz = Quiz.objects.get(pk=quiz_id)
        context = {'quiz': quiz,
                   'back_to_url': reverse('quizapp:quiz_index'),
                   'q_list': Question.objects.filter(quiz=quiz)}
        return render(request, 'quizapp/quiz/take.html', context)


@login_required
def quiz_delete(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    quiz.delete()
    return HttpResponseRedirect(reverse('quiz_index'))


@login_required
def question_manage(request, question_id):
    question = Question.objects.get(pk=question_id)
    quiz = question.quiz
    answers = Answer.objects.filter(question=question)
    if request.method == 'POST':
        if 'delete' in request.POST:
            question.delete()
            return HttpResponseRedirect(reverse('quiz_manage', args=(quiz.id,)))
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('quiz_manage', args=(quiz.id,)))
    else:
        form = QuestionForm(initial={'quiz': question.quiz,
                                     'text': question.text,
                                     'answers': Answer.objects.filter(question=question)})
        form.fields['quiz'].widget = HiddenInput()

    return render(request, 'quizapp/question/manage.html',
                  {'form': form,
                   'quiz': quiz,
                   'question_id': question.id,
                   'answers': answers})


def answer_post(request, a_id):
    """Answer a question."""
    answer = Answer.objects.get(pk=a_id)
    if answer.correct:
        response = "<strong>Correct!</strong> Great job."
    else:
        response = "<strong>Sorry,</strong> wrong answer."
    return HttpResponse(response)


@login_required
def answer_manage(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    question = Question.objects.get(answer=answer)
    if request.method == 'POST':
        if 'delete' in request.POST:
            answer.delete()
            return HttpResponseRedirect(reverse('question_manage', args=(question.id,)))
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('question_manage', args=(question.id,)))

    else:
        form = AnswerForm(initial={'question': question,
                                   'text': answer.text,
                                   'correct': answer.correct,
                                   'notes': answer.notes})
        form.fields['question'].widget = HiddenInput()

    return render(request, 'quizapp/answer/manage.html',
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
            return HttpResponseRedirect(reverse('quizapp:quiz_manage', args=(quiz_id,)))
    else:
        form = QuestionForm(initial={'quiz': quiz,
                                     'user': request.user})
        # form.fields['quiz'].widget = HiddenInput()

    return render(request, 'quizapp/question/add.html',
                  {'quiz': quiz, 'form': form})


@login_required
def answer_add(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('quizapp:question_manage', args=(question_id,)))

    else:
        form = AnswerForm(initial={'question': question})
        form.fields['question'].widget = HiddenInput()

    return render(request, 'quizapp/answer/add.html',
                  {'question': question,
                   'form': form})


def quiz_edit(request, quiz_id):
    """Manage set of answers"""
    quiz = Quiz.objects.get(pk=quiz_id)
    QuestionFormSet = modelformset_factory(
        Question,
        fields=('text',),
        widgets = {'text': Textarea(attrs={'cols': 80, 'rows': 2}), },
        can_delete=True,
        # can_order=True,
        extra=0)

    if request.method == 'POST':
        formset = QuestionFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data?
            formset.save()
            messages.success(request, 'Questions updated.')
            # return HttpResponseRedirect(reverse('quizapp:questions_manage', args=(quiz_id,)))
    else:
        formset = QuestionFormSet(
            queryset=Question.objects.filter(quiz=quiz))

    return render(request, 'quizapp/quiz/edit.html',
                  {'quiz': quiz,
                   'back_to_url': reverse('quizapp:quiz_index'),
                   'add_url': reverse('quizapp:question_add', args=[quiz_id]),
                   'formset': formset})


def answers_edit(request, question_id):
    """Manage set of answers"""
    question = Question.objects.get(pk=question_id)
    AnswerFormSet = modelformset_factory(
        Answer, fields=('text', 'correct'),
        can_delete=True,
        # can_order=True,
        extra=0)

    if request.method == 'POST':
        formset = AnswerFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            pass
    else:
        formset = AnswerFormSet(queryset=Answer.objects.filter(question=question))

    return render(request, 'quizapp/answer/edit.html',
                  {'question': question,
                   'back_to_url': reverse('quizapp:quiz_edit', args=[question.quiz.id]),
                   'add_url': reverse('quizapp:answer_add', args=[question_id]),
                   'formset': formset})
