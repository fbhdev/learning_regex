import csv
import os.path


class Records:

    def __init__(self, questions: int, score: int, percentage: float) -> None:
        """
        Initialize Records class
        :param questions: int
        :param score:  int
        :param percentage: float
        """
        self.directory = "records/"
        self.csv_file = "logs.csv"
        self.questions = questions
        self.score = score
        self.percentage = percentage

    def __repr__(self) -> str:
        """
        Return string representation of Records class
        :return: str
        """
        return f"{self.__class__.__name__}({self.__dict__})"

    def write(self) -> None:
        """
        Write to csv file
        :return: None
        """
        with open(self.directory + self.csv_file, "a") as file:
            writer = csv.writer(file, delimiter=",")
            if os.path.getsize(self.directory + self.csv_file) == 0:
                writer.writerow(["Number of Questions", "Score", "Percentage"])
            writer.writerow([self.questions, self.score, self.percentage])

    def read(self) -> None:
        """
        Read from csv file
        :return: None
        """
        with open(self.directory + self.csv_file, "r") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                print(row)
