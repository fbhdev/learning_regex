class Question:

    def __init__(self, question: str, answer: str) -> None:
        self.answer = answer
        self.question = question

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"

    def set_questions(self, question: str) -> None:
        self.question = question

    def get_question(self) -> str:
        return self.question

    def set_answer(self, answer: str) -> None:
        self.answer = answer

    def get_answer(self) -> str:
        return self.answer
