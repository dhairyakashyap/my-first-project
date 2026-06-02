class Person:
    def __init__(self, name,):
        self.name = name
    def lifts(self):
        print(f"{self.name} lifts weights")

class Fit(Person):
    def lifts(self):
        print(f"{self.name} is fit and lifts heavy weights")

class Unfit(Person):
    def lifts(self):
        print(f"{self.name} is unfit and struggles to lift weights")

fit_person = Fit("Hulk")
unfit_person = Unfit("Loki")
fit_person.lifts()
unfit_person.lifts()