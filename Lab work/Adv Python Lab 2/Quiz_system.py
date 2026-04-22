"""Quiz System

Features:
- Load questions from file
- Ask user
- Score calculation
- Handle invalid input
"""


def load_questions(file_name="questions.txt"):
    questions = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            parts = [p.strip() for p in line.strip().split("|")]
            if len(parts) != 6:
                continue
            questions.append(parts)
    return questions


def run_quiz():
    questions = load_questions()
    score = 0

    for index, q in enumerate(questions, start=1):
        question, op1, op2, op3, op4, answer = q
        print(f"\nQ{index}: {question}")
        print("1.", op1)
        print("2.", op2)
        print("3.", op3)
        print("4.", op4)

        try:
            user_choice = int(input("Your answer (1-4): "))
            if user_choice not in (1, 2, 3, 4):
                raise ValueError("Choice must be 1 to 4")

            if str(user_choice) == answer:
                score += 1
        except ValueError as exc:
            print("Invalid input:", exc)

    print(f"\nFinal Score: {score}/{len(questions)}")


if __name__ == "__main__":
    run_quiz()
