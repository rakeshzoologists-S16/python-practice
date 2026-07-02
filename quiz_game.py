questions = {
    "What is the capital of France?": "paris",
    "Which language is used for web apps, Java or JavaScript?": "javascript",
    "What does CPU stand for?": "central processing unit",
    "What is 5 + 7?": "12",
    "Which planet is known as the Red Planet?": "mars"
}

score = 0

print("Welcome to the Quiz Game!")

for question, answer in questions.items():
    user_answer = input(question + " ").strip().lower()
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}.")

print(f"\nYour final score is {score}/{len(questions)}")
