import csv
import random

from question import Question


class Quiz:

    def __init__(self):
        self.csv_file = "questions.csv"
        self.marks = None
        self.num_of_questions = None
        self.questions = []

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def open_csv(self):
        with open(self.csv_file, "r") as file:
            file = csv.reader(file)
            if file:
                for row in file:
                    self.questions.append(Question(row[0], row[1]))

    @staticmethod
    def user_input(question: str):
        return input(question)

    def get_marks(self):
        return self.marks

    def set_marks(self, marks):
        self.marks = marks

    def get_all_questions(self):
        return self.questions

    def shuffle_questions(self):
        random.shuffle(self.questions)

    def get_next_question(self):
        return self.questions[0]

    def remove_question(self):
        self.questions.pop(0)

    def set_num_of_questions(self):
        if self.num_of_questions is None:
            self.num_of_questions = len(self.questions)

    def run(self):
        self.open_csv()
        self.shuffle_questions()
        self.set_num_of_questions()
        self.set_marks(0)
        while self.num_of_questions > 0:
            question = self.get_next_question()
            answer = self.user_input(f"{question.get_question()} → ")
            if answer == question.get_answer():
                self.set_marks(self.get_marks() + 1)
            self.remove_question()
        print(f"You got {self.get_marks()} out of {self.num_of_questions} correct")
