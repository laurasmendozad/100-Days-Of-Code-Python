""" Quiz Game Project """
import os
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

os.system('cls')

question_bank = []
for q in question_data:
    question_bank.append(Question(q["question"],q["correct_answer"]))

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
