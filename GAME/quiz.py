import tkinter as tk
import random

from click import command
from pygame.examples.video import answer

#Sample flashcards (you can add more)
flashcards = [
    {"question":"what is the capital of France?","answer":"Paris"},
    {"question":"what is  5 + 7?","answer":"12"},
    {"question":"what is the color of the sky?","answer":"Blue"},
    {"question":"who wrote 'Harry Potter'?","answer":"J.K.Rowling"},
    {"question":"what is the largest planet?","answer":"Jupiter"},
]
class FlashcardApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Flashcard Quiz")
        self.root.geometry("400x300")
        self.root.config(bg="white")

        self.question_label = tk.Label(root,text="",font=("Arial",16),wraplength=350,bg="white")
        self.question_label.pack(pady=40)

        self.question_label = tk.Label(root, text="", font=("Arial", 14,"italic"), fg="green",bg="white")
        self.question_label.pack(pady=10)

        self.show_answer_btn =  tk.Label(root, text="Show Answer", command=self.show_answer)
        self.show_answer_btn.pack(pady=5)

        self.next_flashcard() #show first flashcard
    def next_flashcard(self):
        self.current = random.choice(flashcards)
        self.question_label.config(text=self.current["question"])
        self.answer_label



