''' UI DESIGN '''
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    ''' Quiz UI Interface Class '''
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0",
                                 font=("Arial", 15),
                                 bg=THEME_COLOR,
                                 fg= "white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                    text="Quizzler",
                                                    width=250,
                                                    fill=THEME_COLOR,
                                                    font=("Arial", 18, "italic"),
                                                    justify= CENTER)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_img = PhotoImage(file=r"Day 034\images\true.png")
        self.true_button = Button(image=self.true_img,
                                  highlightthickness=0,
                                  command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        self.false_img = PhotoImage(file=r"Day 034\images\false.png")
        self.false_button = Button(image=self.false_img,
                                   highlightthickness=0,
                                   command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        ''' Generate Next Question '''
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, fill="black")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text= "You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        ''' Select the true answer button '''
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        ''' Select the false answer button '''
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        ''' Give feedback to the user '''
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_next_question)
