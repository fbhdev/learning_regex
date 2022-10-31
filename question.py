class Question:

    def __init__(self, question, answer):
        self.answer = answer
        self.question = question

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def set_questions(self, question):
        self.question = question

    def get_question(self):
        return self.question

    def set_answer(self, answer):
        self.answer = answer

    def get_answer(self):
        return self.answer
