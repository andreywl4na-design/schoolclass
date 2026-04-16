import random


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.avg_mark = random.randint(8, 12)
        self.gladness = 50
        self.progress = 0
        self.money = 100          # стартові гроші
        self.alive = True

    def __str__(self):
        return (f"Name: {self.name}, Age: {self.age}, Mark: {self.avg_mark}, "
                f"Money: {self.money}")

    def to_study(self):
        print("Time to study")
        self.progress += 1
        self.gladness -= 5
        self.money -= 10         # витрати на навчання

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("Time to chill")
        self.gladness += 5
        self.progress -= 0.5
        self.money -= 15         # витрати на відпочинок

    def to_work(self):
        print("Time to work")
        self.money += 30
        self.gladness -= 4
        self.progress -= 0.2

    def check_status(self):
        if self.money <= 0:
            print("No money... Need to work!")
            self.to_work()

        if self.gladness <= 0:
            print("Depression...")
            self.alive = False

        if self.progress >= 365:
            print("Student graduated!")
            self.alive = False

    def end_of_day(self):
        print(f"Progress: {self.progress:.2f}")
        print(f"Gladness: {self.gladness:.2f}")
        print(f"Money: {self.money:.2f}")
        print("-" * 30)

    def live(self, day):
        if not self.alive:
            return

        print(f"Day {day} of {self.name}")

        # Якщо проблеми з навчанням — більше вчиться
        if self.progress < day * 0.5:
            self.to_study()

        # Якщо мало грошей — працює
        elif self.money < 20:
            self.to_work()

        else:
            live_r = random.randint(1, 4)

            if live_r == 1:
                self.to_study()
            elif live_r == 2:
                self.to_sleep()
            elif live_r == 3:
                self.to_chill()
            elif live_r == 4:
                self.to_work()

        self.check_status()
        self.end_of_day()


# запуск симуляції року
nick = Student("Nick", 20)

for day in range(1, 366):
    if nick.alive:
        nick.live(day)
    else:
        break