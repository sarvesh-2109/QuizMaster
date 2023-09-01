from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for info in question_data:
    question = info["question"]
    answer = info["correct_answer"]
    data = Question(question, answer)
    question_bank.append(data)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_que()

print("You have completed the quiz!")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")

