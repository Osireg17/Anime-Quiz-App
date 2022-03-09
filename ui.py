from cgitb import text
from tkinter import *

from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Anime Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR, font=('Arial', 24,'bold'))
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=400, height=300, bg='White')   #this creates the width of the canvavs
        self.question_text = self.canvas.create_text(
            200, 
            150, 
            width=300,
            text='Question', 
            fill=THEME_COLOR, 
            font=('Arial', 20, 'italic')
            )  #this just sets up the text, literally just says question above it
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)  #this sets up the grid of the canvas
        self.Tick = PhotoImage(file='true.png')
        self.cross = PhotoImage(file='false.png')

        self.true_buttton = Button(image=self.Tick, command=self.is_true)
        self.true_buttton.grid(row=3, column=1, pady=10)
        self.wrong_button = Button(image=self.cross, command=self.is_false)
        self.wrong_button.grid(row=3, column=0, pady=10, padx=30)
        
        self.get_next_question()

        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_text) #This has changed the text which was previously made, using the attribute itemconfig
        else:
            self.canvas.itemconfig(self.question_text, text=f'You have ended the Quiz')
            self.is_true.config(state='disabled')
            self.is_false.config(state='disabled')
    def is_true(self):
        self.give_feeback(self.quiz.check_answer('True'))
    def is_false(self):
        self.give_feeback(self.quiz.check_answer('False'))
    def give_feeback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg='red')
            self.window.after(1000, self.get_next_question)