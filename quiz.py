import csv
import random

from question import Question
from records import Records


class Quiz:

    def __init__(self) -> None:
        self.csv_file = "questions.csv"
        self.marks = {"correct": 0, "questions": 0}
        self.num_of_questions = None
        self.questions = []

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def open_csv(self) -> None:
        with open(self.csv_file, "r") as file:
            file = csv.reader(file)
            if file:
                for row in file:
                    self.questions.append(Question(str(row[0]), str(row[1])))

    @staticmethod
    def user_input(question: str) -> str:
        while True:
            user = input(question)
            if len(user) < 1:
                print("Please enter a value")
                continue
            return user

    def get_marks(self) -> int:
        return self.marks["correct"]

    def set_marks(self, marks) -> None:
        self.marks["correct"] = marks

    def grade(self) -> float:
        percentage = self.get_marks() / self.get_num_of_questions() * 100
        return round(percentage, 2)

    def get_all_questions(self) -> list:
        return self.questions

    def shuffle_questions(self) -> None:
        random.shuffle(self.questions)

    def get_next_question(self) -> Question:
        return self.questions[0]

    def remove_question(self) -> None:
        self.questions.pop(0)

    def set_num_of_questions(self) -> None:
        if self.num_of_questions is None:
            self.num_of_questions = len(self.questions)
            self.marks["questions"] = self.num_of_questions

    def get_num_of_questions(self) -> int:
        return self.marks["questions"]

    def check_answer(self, user, answer) -> None:
        if user == answer:
            self.set_marks(self.get_marks() + 1)
            print(f"Correct!")
        else:
            print(f"Incorrect! → Answer: {answer}")

    def performance(self) -> None:
        print(f"Your score is {self.get_marks()} out of {self.get_num_of_questions()}")
        print(f"Your grade is {self.grade()}%")
        print()

    def run(self) -> None:
        self.open_csv()
        self.shuffle_questions()
        self.set_num_of_questions()
        count = 0
        while self.num_of_questions > 0:
            count += 1
            question = self.get_next_question()
            answer = str(self.user_input(f"{count}– {question.get_question()} → "))
            self.check_answer(answer, question.get_answer())
            self.remove_question()
            self.num_of_questions -= 1
            print()
        self.performance()
        Records(self.get_num_of_questions(), self.get_marks(), self.grade()).write()
