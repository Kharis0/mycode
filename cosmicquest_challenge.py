#!/usr/bin/env python3
"""Kharis Research | KharisZ.Inc
    Conditionals - Cosmic Quest Challenge guessing game using a while true loop."""

def multiple_choice_game():
    questions = [
        {
            "question": "In which galaxy is our solor system located?",
            "options": ["A. Andromeda", "B. Milky Way", "C. Triangulum", "D. Sombrero"],
            "correct_answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"],
            "correct_answer": "C"
        },
        {
            "question": "What is the term for a sudden and intense increase in the brightness of a star, often outshining an entire galaxy temporarily?",
            "options": ["A. Supernova", "B. Nova", "C. Hypernova", "D. Quasar"],
            "correct_answer": "A"
        },
        {
            "question": "Which exoplanet is often referred to as Earth's twin due to its similar size and potential habitability?",
            "options": ["A. Kepler-22b", "B. Proxima Centauri b", "C. TRAPPIST-1e", "D. Gliese 581g"],
            "correct_answer": "A"
        },
        {
            "question": "What is the phenomenon where light is bent as it passes through a gravitational field?",
            "options": ["A. Refraction", "B. Diffraction", "C. Gravitational lensing", "D. Polarization"],
            "correct_answer": "C"
        },
        {
            "question": "What is the name of the largest moon in our solar system, which orbits Jupiter?",
            "options": ["A. Europa", "B. Ganymede", "C. Io", "D. Callisto"],
            "correct_answer": "B"
        }
    ]

    score = 0
    incorrect_answers = 0
    question_number = 0

    print("WELCOME TO COSMIC QUEST CHALLENGE GAME!")

    while question_number < len(questions) and incorrect_answers < 3:
        current_question = questions[question_number]

        print(f"\nQuestion {question_number + 1}: {current_question['question']}")
        for option in current_question['options']:
            print(option)

        user_answer = input("Enter the letter of your answer (A, B, C, or D): ").upper()

        if user_answer == current_question['correct_answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {current_question['correct_answer']}.\n")
            incorrect_answers += 1

        question_number += 1

    if incorrect_answers == 3:
        print("Sorry, you failed the gmae. Better luck next time!")
    else:
        print(f"Congratulations! You answered all questions correctly. Your final score is {score}/{len(questions)}.")

# Run the game
multiple_choice_game()
