class Calculator(list):
    def min(self):
        return min(self)

    def max(self):
        return max(self)




p = Calculator()
p.append(12)
p.append(25)
p.append(1123)


print(p.min())
print(p.max())
