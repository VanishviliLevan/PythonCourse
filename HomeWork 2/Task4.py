class CallMixin:
    def call(self):
        return f"Calling to {self.fname} {self.lname} , On number {self.number}"


class Person(CallMixin):
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number

    def info(self):
        return f"{self.fname} {self.lname} , Number - {self.number}"


p1 = Person("jane", "Smith", 11111111)
print(p1.call())
p2 = Person("Tom", "Jones", 122222222)
print(p2.call())