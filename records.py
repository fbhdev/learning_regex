import csv
import os.path


class Records:

    def __init__(self, questions: int, score: int, percentage: float) -> None:
        self.directory = "records/"
        self.csv_file = "logs.csv"
        self.questions = questions
        self.score = score
        self.percentage = percentage

    def __repr__(self):
        pass

    def write(self):
        with open(self.directory + self.csv_file, "a") as file:
            writer = csv.writer(file, delimiter=",")
            if os.path.getsize(self.directory + self.csv_file) == 0:
                writer.writerow(["Number of Questions", "Score", "Percentage"])
            writer.writerow([self.questions, self.score, self.percentage])

    def read(self):
        with open(self.directory + self.csv_file, "r") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                print(row)
