# Prject 18 - Quizz App
# QUestion Api Link: https://opentdb.com/api_config.php

from day_017.data import question_data2
from day_017.question_model import Question
from day_017.quiz_brain import QuizBrain

question_bank = []
for question in question_data2:
    question_text = question['question']
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_no}")
