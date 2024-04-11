from tkinter import *
from quiz_brain import QuizBrain
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.minsize(width=400, height=500)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(bg='white', width=300, height=250)
        self.quiz_text = self.canvas.create_text(150, 125, text='Test', font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_image = PhotoImage(file='/Users/nickjenkins/Downloads/quizzler-app-start/images/true.png')
        wrong_image = PhotoImage(file='/Users/nickjenkins/Downloads/quizzler-app-start/images/false.png')

        self.right_btn = Button(image=right_image, width=100, height=100, highlightthickness=0,
                                command=self.correct_click)
        self.wrong_btn = Button(image=wrong_image, width=100, height=100, highlightthickness=0,
                                command=self.false_click)
        self.right_btn.grid(row=2, column=0)
        self.wrong_btn.grid(row=2, column=1)

        self.label = Label(text=f"Score:{self.quiz.score}", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text=F'Final Score: {self.quiz.score}/10')

    def false_click(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
        # self.get_next_question()

    def correct_click(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
        # self.get_next_question()

    def turn_white(self):
        self.canvas.config(bg='white')

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, func=self.turn_white)
        self.window.after(1000, func=self.get_next_question)

