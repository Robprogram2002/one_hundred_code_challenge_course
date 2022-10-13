from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, font=("Arial", 14), fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.main_text = self.canvas.create_text(150, 125, text="", font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.update_text()

        correct_img = PhotoImage(file="./images/true.png")
        false_img = PhotoImage(file="./images/false.png")
        self.correct_bt = Button(image=correct_img, highlightthickness=0, command=self.correct_handler)
        self.correct_bt.grid(row=2, column=1)
        self.false_bt = Button(image=false_img, highlightthickness=0, command=self.false_handler)
        self.false_bt.grid(row=2, column=0)

        self.window.mainloop()

    def answer_handler(self, answer):
        color = "green" if self.quiz.check_answer(answer) else "red"
        self.window.after(250, self.update_screen, color)

    def correct_handler(self):
        self.answer_handler("True")

    def false_handler(self):
        self.answer_handler("False")

    def update_text(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score:{self.quiz.score}")
        if self.quiz.question_number < 10:
            self.canvas.itemconfig(self.main_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.main_text,
                                   text=f"Final Score: {self.quiz.score}/{self.quiz.question_number}")
            self.correct_bt.config(state="disabled")
            self.false_bt.config(state="disabled")

    def update_screen(self, color):
        self.canvas.config(bg=color)
        self.window.after(500, self.update_text)
