class QuizBrain:

    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        player_answer = input(f"Q. {self.question_number}: {current_question.text} (True / False)?")
        return player_answer

    def check_answer(self, player_answer):
        if player_answer.lower() == self.questions_list[self.question_number - 1].answer.lower():
            print("You got it right!")
            return True
        else:
            print("That's not correct.")
            return False

    def display_score(self):
        print(f"Your score is {self.score}/{self.question_number}.\n")

    def increase_score(self):
        self.score += 1

    def still_has_questions(self):
        return self.question_number != len(self.questions_list)


