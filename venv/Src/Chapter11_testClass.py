class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.answers = []

    def show_question(self):
        print(self.question)

    def store_answer(self, answer):
        self.answers.append(answer)

    def show_answers(self):
        print("Survey results:")
        for answer in self.answers:
            print("-" + answer)
