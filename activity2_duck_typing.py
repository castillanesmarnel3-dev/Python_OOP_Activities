class Car:
    def move(self):
        print("The car is driving on the road.")


class Person:
    def move(self):
        print("The person is walking.")


class Robot:
    def move(self):
        print("The robot is moving mechanically.")


def make_it_move(thing):
    thing.move()


objects = [Car(), Person(), Robot()]

for obj in objects:
    make_it_move(obj)
