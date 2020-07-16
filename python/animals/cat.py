from animal import Animal


class Cat(Animal):
  def say_hello(self):
    print("Meow")

  def get_number_of_legs(self):
    print("This animal has 4 legs")

  def how_do_i_move(self):
    print("When I am spooked, I run away, I also walk when I am regular and just like dogs when "
          "I see something tasty I munch it.")

  def how_much_do_i_weigh(self):
    print("I weigh as much as 5-10-25 lbs")

  def am_i_extinct(self):
    print("I am not extinct")
