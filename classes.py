class Animal(object):
    def __init__(self, animal_type, leg_count=0):
        self.animal_type = animal_type
        self._leg_count = leg_count

    def speak(self, *args, **kwargs):
        raise NotImplementedError("This animal has not defined how to speak")

    def leg_count(self):
        return self._leg_count


class Dog(Animal):
    def __init__(self, name):
        super().__init__("dog", leg_count=4)
        self.name = name

    def speak(self, *args, **kwargs):
        print(f"I can say these position args: {args}")
        print(f"I can say these keyword args: {kwargs}")


class Cat(Animal):
    def __init__(self, name):
        super().__init__("cat", leg_count=4)
        self.name = name

    def speak(self, *args, **kwargs):
        print("Meow!")


if __name__ == "__main__":
    dog = Dog(name="spot")
    dog.speak("hello", "woof", "im hungry", food="bacon", water="water")
