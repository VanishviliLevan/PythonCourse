class TestClass:
    def reset(self):
        self.x = 0
        self.y = 0

    def add(self, x, y):
        self.x = x
        self.y = y

    def calc(self, second):
        sum = []
        sum.append(self.x + second.x)
        sum.append(self.y + second.y)
        return sum


new = TestClass()
new.add(2, 3)
new2 = TestClass()
new2.reset()

print(new.calc(new2))
