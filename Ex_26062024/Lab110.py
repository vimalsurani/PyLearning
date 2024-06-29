class Dog:
    name = None
    id = None

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def sleep(self):
        print("Who is Sleeping ->", self.name)


dog1 = Dog("Chow", "101")
dog2 = Dog("Mow", "102")
# dog3 = Dog()  # TypeError: Dog.__init__() missing 2 required positional arguments: 'name' and 'id'


print(f"{dog1.name} has a {dog1.id}")
print(f"{dog2.name} has a {dog2.id}")

dog1.sleep()
dog2.sleep()
