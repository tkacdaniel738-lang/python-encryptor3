
import random

class Student:
    def __init__(self, name):
        self.name = name
        self.money = 1000
        self.energy = 100
        self.knowledge = 50
        self.happiness = 50
        self.day = 0

    def study(self):
        self.energy -= 15
        self.knowledge += 10
        self.happiness -= 5
        print(f"{self.name} навчається. Знання: {self.knowledge}")

    def work(self):
        self.energy -= 20
        self.money += 500
        self.happiness -= 10
        print(f"{self.name} працює. Гроші: {self.money} грн")

    def rest(self):
        self.energy += 30
        self.money -= 100
        self.happiness += 15
        print(f"{self.name} відпочиває.")

    def live_day(self):
        self.day += 1
        print(f"\n--- День {self.day} ---")

        if self.money < 300:
            self.work()
        elif self.knowledge < 30:
            self.study()
        elif self.energy < 30:
            self.rest()
        else:
            action = random.choice(["study", "work", "rest"])

            if action == "study":
                self.study()
            elif action == "work":
                self.work()
            else:
                self.rest()

        self.energy = max(0, min(100, self.energy))
        self.knowledge = max(0, min(100, self.knowledge))
        self.happiness = max(0, min(100, self.happiness))

    def live_year(self):
        print(f"Студент {self.name} починає навчальний рік!")

        for _ in range(365):
            self.live_day()

        print("\n===== ПІДСУМОК РОКУ =====")
        print("Ім'я:", self.name)
        print("Гроші:", self.money, "грн")
        print("Енергія:", self.energy)
        print("Знання:", self.knowledge)
        print("Щастя:", self.happiness)


student = Student("Данило")
student.live_year()
