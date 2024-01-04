""" Quiz Brain Class """
import html
class QuizBrain():
    """ Quiz Brain Class """
    def __init__(self, question_list):
        self.question_list = question_list
        self.current_question = None
        self.question_number = 0
        self.score = 0

    def next_question(self):
        """ Ask for the answer of the question """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f'Q.{self.question_number}: {q_text}'

    def still_has_questions(self):
        """ Return True when there are still some questions, or False otherwise"""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer):
        """ Check if the answer is correct """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
