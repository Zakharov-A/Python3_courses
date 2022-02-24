class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name=None, age=20, isHappy="a little bit"):
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name = None, age = None, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, "age: ", self.age, ". Happy: ", self.isHappy)


cat1 = Cat("dartBarsik", 2, "Yes" )



cat2 = Cat("dartHrosick", 3, False)


