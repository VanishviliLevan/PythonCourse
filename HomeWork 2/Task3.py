class Animal:
    def __init__(self, name, age, **kwargs):
        self._age = age
        self._name = name

    def info(self):
        return f"Name - {self._name},  Age - {self._age}"


class Dog(Animal):
    def __init__(self, model, color, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.color = color

    def info(self):
        return super().info() + ", " + f"Model - {self.model}, Color - {self.color}"


d1 = Dog(name="Hulk", age=5, model="Pit", color="Black")
print(d1.info())
d2 = Dog(name="Jerry", age=2, model="Husk", color="Gray")
print(d2.info())
