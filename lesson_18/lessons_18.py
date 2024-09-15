class Human:
    def __init__(self, age, name, height, weight):
        self.age = age
        self.name = name
        self.height = height
        self.weight = weight

    def say_hllo(self):
        print('Hello!')
        print('I am a human.')

    def say_good_bye(self):
        print('See you!')

    def tell_about_yourself(self):
        print('Hello, may name is', self.name)
        print('I am', self.age, 'years old')

    def happy_birthaday(self):
        print('Today is my birthday!')
        self.age += 1


x = Human(5, 'Joe', 160, 56)
list_hum = [x, Human(10, 'Vika', 160, 156), ]

for i in range(list_hum.__len__()):
    print(list_hum[i].age)
