class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        self.area_info = self.width * self.length
        return self.area

    def perimeter(self):
        self.perimeter_info = (self.width+self.length) * 2
        return self.perimeter_info

    def print_info(self):
        print(f"The length is - {self.length} , The Width is - {self.width} , Area - {self.area_info} , Perimeter - {self.perimeter_info}")


# თუ Area და Perimeter  მეთოდები არ გამოაცხადე ისე print_info არ დაიბეჭდება , შემეძლო სხვანაირადაც ჩამეწერა მაგრამ იდეა მესმის და ასე დავტოვე