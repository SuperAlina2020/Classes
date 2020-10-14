from unittests import AnonymousSurvey
from unittest import TestCase

class TestAnonymousSurvey(TestCase):

    def test_single_response(self):
        question = 'Какой это автомобиль?'
        new_poll = AnonymousSurvey(question)
        response = 'Bugatti'
        new_poll.add_answer(response)
        self.assertIn(response,new_poll.responses)

    def test_list_responses(self):
        question = 'Какой чай предпочитаете?'
        responses = ['Elite','Lipton','Akbar','Fuse Tea']
        new_poll = AnonymousSurvey(question)
        for response in responses:
            new_poll.add_answer(response)
        self.assertEqual(len(responses),len(new_poll.responses))


