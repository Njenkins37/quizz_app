from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.minsize(width=400, height=500)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(bg='white', width=300, height=250)
        self.quiz_text = self.canvas.create_text(150, 125, text='Test', font=FONT, fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_image = PhotoImage(file='/Users/nickjenkins/Downloads/quizzler-app-start/images/true.png')
        wrong_image = PhotoImage(file='/Users/nickjenkins/Downloads/quizzler-app-start/images/false.png')

        self.right_btn = Button(image=right_image, width=100, height=100, highlightthickness=0)
        self.wrong_btn = Button(image=wrong_image, width=100, height=100, highlightthickness=0)
        self.right_btn.grid(row=2, column=0)
        self.wrong_btn.grid(row=2, column=1)

        self.label = Label(text=f"Score:{0}", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)

        self.window.mainloop()
