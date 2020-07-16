from dog import Dog
from cat import Cat
from duck import Duck
from bird import Bird
from giraffe import Giraffe
from hippo import Hippo
from monkey import Monkey
from bee import Bee

What_animal = input("What animal do you want us to give information about? ")
if What_animal == "Dog":
    d = Dog(4)
    d.say_hello()
    d.get_number_of_legs()
    d.how_do_i_move()
    d.how_much_do_i_weigh()
    d.am_i_extinct()

if What_animal == "Cat":
    c = Cat(4)
    c.say_hello()
    c.get_number_of_legs()
    c.how_do_i_move()
    c.how_much_do_i_weigh()
    c.am_i_extinct()


if What_animal == "Duck":
    d = Duck(2)
    d.say_hello()
    d.get_number_of_legs()
    d.how_do_i_move()
    d.how_much_do_i_weigh()
    d.am_i_extinct()

if What_animal == "Bird":
    b = Bird(2)
    b.say_hello()
    b.get_number_of_legs()
    b.how_do_i_move()
    b.how_much_do_i_weigh()
    b.am_i_extinct()


if What_animal == "Giraffe":
    g = Giraffe(4)
    g.say_hello()
    g.get_number_of_legs()
    g.how_do_i_move()
    g.how_much_do_i_weigh()
    g.am_i_extinct()


if What_animal == "Hippo":
    h = Hippo(4)
    h.say_hello()
    h.get_number_of_legs()
    h.how_do_i_move()
    h.how_much_do_i_weigh()
    h.am_i_extinct()


if What_animal == "Monkey":
    m = Monkey(2)
    m.say_hello()
    m.get_number_of_legs()
    m.how_do_i_move()
    m.how_much_do_i_weigh()
    m.am_i_extinct()


if What_animal == "Bee":
    be = Bee(0)
    be.say_hello()
    be.get_number_of_legs()
    be.how_do_i_move()
    be.how_much_do_i_weigh()
    be.am_i_extinct()

