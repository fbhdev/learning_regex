import csv
import random

from records import Records


class Question:

    def __init__(self, question: str, answer: str) -> None:
        """
        Initialize Question class
        :param question: str
        :param answer:  str
        """
        self._answer = answer
        self._question = question

    def __repr__(self) -> str:
        """
        Return string representation of Question class
        :return: str
        """
        return f"{self.__class__.__name__}"

    @property
    def question(self) -> str:
        """
        Get question
        :return: str
        """
        return self._question

    @question.setter
    def question(self, question: str) -> None:
        """
        Set question
        :param question: str
        :return: None
        """
        self._question = question

    @property
    def answer(self) -> str:
        """
        Get answer
        :return: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer: str) -> None:
        """
        Set answer
        :param answer: str
        :return: None
        """
        self._answer = answer


class HandleUserInput:

    def __init__(self) -> None:
        """
        Initialize HandleUserInput class
        :return: None
        """
        self._prompt = None

    def __repr__(self) -> str:
        """
        Return string representation of HandleUserInput class
        :return: str
        """
        return f"{self.__class__.__name__}({self.__dict__})"

    @property
    def prompt(self) -> str:
        """
        Get prompt
        :return: str
        """
        return self._prompt

    @prompt.setter
    def prompt(self, question) -> None:
        """
        Set prompt
        :param question: str
        :return: None
        """
        self._prompt = input(f"{question}\t")


class Quiz:

    def __init__(self) -> None:
        """
        Instantiates the Quiz class.
        :return: None
        """
        self.csv_file = "questions.csv"
        self.questions = []
        self.open_csv()
        if not self.questions:
            raise FileNotFoundError("Questions file not found.")
        self.score = {"correct": 0, "questions": 0}
        self._length = 0

    def __repr__(self) -> str:
        """
        Returns the string representation of the Quiz class.
        :return: str
        """
        return f"{self.__class__.__name__}({self.__dict__})"

    def open_csv(self) -> None:
        """
        Opens the csv file and reads the questions and answers.
        :return: None
        """
        with open(self.csv_file, "r") as file:
            file = csv.reader(file)
            if not file:
                return None
            for row in file:
                self.questions.append(Question(str(row[0]), str(row[1])))

    def randomize(self) -> None:
        """
        Randomizes the questions.
        :return: None
        """
        random.shuffle(self.questions)

    @property
    def length(self) -> int:
        """
        Returns the length of the quiz.
        :return: int
        """
        return self._length

    @length.setter
    def length(self, length: int) -> None:
        """
        Sets the length of the quiz.
        :param length: int
        :return: None
        """
        if length > len(self.questions):
            self._length = len(self.questions)
        else:
            self._length = length

    def grade(self) -> float:
        """
        Returns the grade.
        :return:
        """
        percentage = self.score["correct"] / self.score["questions"] * 100
        return round(percentage, 2)

    def keep_score(self, mark: float = 1, number: int = 1) -> None:
        """
        Keeps track of the score.
        :param mark: float
        :param number: int
        :return: None
        """
        self.score["correct"] += mark
        self.score["questions"] += number

    def run(self) -> None:
        """
        Runs the quiz.
        :return: None
        """
        while True:
            try:
                print(f"{len(self.questions)} questions available.\n")
                self.length = int(input("How many do you want to answer?\t"))
                print(f"You have chosen to answer {self.length} questions.\n")
                break
            except ValueError:
                continue

        self.randomize()

        while self.score["questions"] < self.length:
            print(self.questions[0].question)
            user_input = HandleUserInput()
            user_input.prompt = "Answer:"
            if self.questions[0].answer.lower() == user_input.prompt.lower():
                self.keep_score()
                print("Correct!")
            else:
                self.keep_score(0)
                print("Incorrect!")
            self.questions.pop(0)
            print()

        Records(self.score["correct"], self.score["questions"], self.grade()).write()
