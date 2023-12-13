""" Quiz Brain Class """

class QuizBrain():
    """ Quiz Brain Class """
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        """ Ask for the answer of the question """
        current_question = self.question_list[self.question_number]
        user_answer = input(f'Q.{self.question_number+1}: {current_question.text} (True/False)? --> ')
        self.check_answer(user_answer, current_question.answer)
        self.question_number += 1

    def still_has_questions(self):
        """ Return True when there are still some questions, or False otherwise"""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print("That's wrong!")
            print(f'The correct answer was: {correct_answer}')
        
        print(f'Your current score is: {self.score}/{self.question_number+1}\n')
