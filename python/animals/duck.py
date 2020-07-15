from animal import Animal


class Duck(Animal):
  def say_hello(self):
    print("Quack")

  def get_number_of_legs(self):
    print("I have 2 legs")

  def how_do_i_move(self):
    print("I have webbed feet so I paddle and swim smoothly")

  def how_much_do_i_weigh(self):
    print("I weigh 3-4.5 lbs")
