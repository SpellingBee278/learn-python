# variables
chicks = "Do you have chick?"
animal = input("What animal do you like? ")
animal_array = ["Chicks", "chicks"]
chicks_array = ["Yes", "yes"]
other_animals = [""]
yes_answer = ["Yes", "yes"]
# if statements
print(animal)

if animal in chicks_array:
    print("Me too!")
    print(chicks + input(" "))

else:
    print("Ok")


if chicks == yes_answer:
    chick_name = input("What is your chick's name? ")
    chicks_age = input("What is your chick's age? ")


else:
    print("Ended")



