#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
import random

class CosmicQuestGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Cosmic Quest Challenge")
        self.geometry("600x400")

        self.questions = [
            {
                "question": "In which galaxy is our solar system located?",
                "options": ["A. Andromeda", "B. Milky Way", "C. Triangulum", "D. Sombrero"],
                "correct_answer": "B"
            },
            # ... (other questions)
        ]

        self.score = 0
        self.incorrect_answers = 0
        self.question_number = 0

        self.label_question = tk.Label(self, text="", font=("Arial", 12))
        self.label_question.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(self, text="", variable=self.radio_var, value="", command=self.check_answer)
            self.radio_buttons.append(radio_button)
            radio_button.pack()

        self.next_button = tk.Button(self, text="Next", command=self.next_question)
        self.next_button.pack(pady=10)

        # Shuffle questions
        random.shuffle(self.questions)

        # Start the game
        self.next_question()

    def next_question(self):
        if self.question_number < len(self.questions) and self.incorrect_answers < 3:
            current_question = self.questions[self.question_number]

            self.label_question.config(text=f"Question {self.question_number + 1}: {current_question['question']}")

            # Shuffle options
            random.shuffle(current_question['options'])

            for i, option in enumerate(current_question['options']):
                self.radio_buttons[i].config(text=option, value=option)

            self.radio_var.set("")
        else:
            self.show_result()

    def check_answer(self):
        user_answer = self.radio_var.get()
        current_question = self.questions[self.question_number]

        if user_answer == current_question['correct_answer']:
            messagebox.showinfo("Correct!", "Correct answer!")
            self.score += 1
        else:
            messagebox.showerror("Incorrect!", f"Wrong! The correct answer is {current_question['correct_answer']}.")
            self.incorrect_answers += 1

        self.question_number += 1
        self.next_question()

    def show_result(self):
        if self.incorrect_answers == 3:
            messagebox.showinfo("Game Over", "Sorry, you failed the game. Better luck next time!")
        else:
            messagebox.showinfo("Congratulations!", f"You answered all questions correctly. Your final score is {self.score}/{len(self.questions)}.")

if __name__ == "__main__":
    app = CosmicQuestGame()
    app.mainloop()

