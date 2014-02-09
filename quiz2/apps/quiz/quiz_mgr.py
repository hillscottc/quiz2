from quiz2.apps.quiz.models import RawLog


def log_message(message, taker=None, owner=None):
    RawLog.objects.create(message=message)
