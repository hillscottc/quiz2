from quiz2.apps.quiz.models import RawLog


def log_message(message, taker=None, owner=None):
    if taker:
        message = "%s %s" % (taker, message)

    RawLog.objects.create(message=message)
