from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.screen = self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.canvas = Canvas(height=250, width=300, bg="white")

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", fill=THEME_COLOR, width=280,
                                                     font=("Ariel", 15, "italic"))
        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, background=THEME_COLOR,
                                  command=self.true_answer)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=self.false_image, highlightthickness=0, background=THEME_COLOR,
                                   command=self.false_answer)
        self.false_button.grid(column=1, row=2)
        self.score = Label(text="Score: 0", background=THEME_COLOR, font=("Ariel", 10, "normal"), fg="white")
        self.score.grid(column=1, row=0)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):

        if is_right is True:
            self.canvas.config(bg="green")
        elif is_right is False:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)

