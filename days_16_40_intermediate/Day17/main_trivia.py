import random
from random import choice, shuffle
from data import questions

TOTAL_QUESTIONS = 15
OPT_DICTIONARY = {
    0: "A)",
    1: "B)",
    2: "C)",
    3: "D)"
}
INV_OPT_DICTIONARY = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3
}


class TriviaQuestion:
    def __init__(self, question, correct_answer, incorrect_answers, category, difficulty):
        self.question = question,
        self.correct_answer = correct_answer,
        self.incorrect_answers = incorrect_answers,
        self.category = category,
        self.difficulty = difficulty

    def get_options(self):
        question_options = self.incorrect_answers[0]

        if len(question_options) == 3:
            question_options.append(self.correct_answer[0])

        shuffle(question_options)
        return question_options


class TriviaGame:
    def __init__(self, question_list):
        self.question_count = 1
        self.score = 0
        self.skip = []
        self.questions = question_list

    @staticmethod
    def greetings():
        print("Welcome to the trivia question game")
        print(f"You will ask for {TOTAL_QUESTIONS} questions")
        print("The game start !! \n")

    def get_next_question(self):
        x = random.randint(0, len(self.questions) - 1)
        while x in self.skip:
            x = (x + 1) % len(self.questions)
        self.skip.append(x)
        return self.questions[x]

    def play(self):
        TriviaGame.greetings()

        while self.question_count <= 15:
            random_question = self.get_next_question()

            next_question = TriviaQuestion(random_question['question'], random_question["correct_answer"],
                                           random_question["incorrect_answers"], random_question["category"],
                                           random_question["difficulty"])

            print(f"\nCategory: {next_question.category[0]} ,  Difficulty: {next_question.difficulty}")
            print(f"Q.{str(self.question_count)}: {next_question.question[0]} ")
            options = next_question.get_options()

            for index, option in enumerate(options):
                print(f"{OPT_DICTIONARY[index]} {option}")

            user_answer = input("What's your answer ? (A/B/C/D) : ").upper()
            while user_answer not in INV_OPT_DICTIONARY:
                print("Please type a valid answer \n")
                user_answer = input("What's your answer ? (A/B/C/D) : ").upper()

            user_answer = options[INV_OPT_DICTIONARY[user_answer]]

            if user_answer == next_question.correct_answer[0]:
                self.score += 1
                print("You got it right!!")

            else:
                print("ohh no, That's wrong :(")
                print(f"The correct answer was {next_question.correct_answer[0]}")

            print(f"Your current score is {self.score}/{self.question_count}")
            self.question_count += 1

        print(f"The game has finish, your final score is {self.score}/{self.question_count}")
        self.reset()

    def reset(self):
        answer = input("Do you want to play again? Type 'y' or  'n' : ")
        if answer == 'y':
            self.question_count = 1
            self.score = 0
            self.skip = []
            self.play()
        else:
            print("Good Bye")


game = TriviaGame(questions)
game.play()
