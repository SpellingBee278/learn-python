from random import randint


class MathQuiz:
  def whole_math_quiz(self):
    num1 = randint(2, 9)
    num2 = randint(3, 10)
    product = num1 * num2

    ans = int(input(f"What is {num1} X {num2}? "))
    if ans == product:
        print("Well done! You have got the answer right!")
        restart_question = input("Do you want to restart the math quiz? ")
        if restart_question == 'Yes':
            self.whole_math_quiz()

    else:
        print("You have got it wrong!")
        restart_question = input("Do you want to restart the math quiz? ")
        if restart_question == 'Yes':
            self.whole_math_quiz()
        else:
            print("Math Quiz Ended")
