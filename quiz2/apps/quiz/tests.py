from django.utils import unittest
from quiz2.apps.quiz.models import Question, Answer


class SmokeTestCase(unittest.TestCase):
    """Tests for quiz_app"""

    def setUp(self):
        pass

    def test_initial_data(self):
        """Test initial data load."""
        print "DB contains %d questions and %d answers." % (Question.objects.count(),
                                                            Answer.objects.count())
        self.assertGreater(Question.objects.count(), 0)
        self.assertGreater(Answer.objects.count(), 0)

    def test_question(self):
        """Test question model."""
        t = "Hello World"
        print "Create new question", t
        new_question = Question(text=t)
        print new_question
        self.assertEquals(new_question.text, t)

        print "Get question and its related models."
        q = Question.objects.get(pk=5)
        print q
        print q.questionanswer_set.all()
        print q.questiontag_set.all()
        self.assertIsNotNone(q)
        self.assertIsNotNone(q.questionanswer_set.all())
        self.assertIsNotNone(q.questiontag_set.all())