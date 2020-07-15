from dog import Dog
from cat import Cat
from duck import Duck
from bird import Bird

What_animal = input("What animal do you want us to give information about? ")
if What_animal == "Dog":
    d = Dog(4)
    d.say_hello()
    d.get_number_of_legs()
    d.how_do_i_move()
    d.how_much_do_i_weigh()

if What_animal == "Cat":
    c = Cat(4)
    c.say_hello()
    c.get_number_of_legs()
    c.how_do_i_move()
    c.how_much_do_i_weigh()

if What_animal == "Duck":
    d = Duck(2)
    d.say_hello()
    d.get_number_of_legs()
    d.how_do_i_move()
    d.how_much_do_i_weigh()

if What_animal == "Bird":
    b = Bird(2)
    b.say_hello()
    b.get_number_of_legs()
    b.how_do_i_move()
    b.how_much_do_i_weigh()
