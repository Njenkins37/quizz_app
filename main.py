from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []

for item in question_data:
    question = Question(item["text"], item["answer"])
    question_bank.append(question)

quiz = Quiz(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{len(question_bank)}")