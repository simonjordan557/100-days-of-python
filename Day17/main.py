from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_list = []

for entry in question_data:
    question_list.append(Question(entry["question"], entry["correct_answer"]))

quiz = QuizBrain(question_list)

while quiz.still_has_questions():
    player_answer = quiz.next_question()
    if quiz.check_answer(player_answer):
        quiz.increase_score()
    quiz.display_score()

print(f"You've completed the quiz! Your final score was {quiz.score}/{quiz.question_number}.")
