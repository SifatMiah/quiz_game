from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# print(question_bank[0].text)




# just wanted to check the enumerate method like how it works
# for i, dict in enumerate(question_data):
#     n = len(dict)
#     r = (f"Dictionary {i + 1} has {n} keys and values.")
# print(r)