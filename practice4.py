class Gym:
    def __init__(self, name):
        self.name = name
    def workout(self):
        print(f"{self.name} is working out at the gym")
    def rest_day(self):
        print(f"{self.name} is taking a rest day and is not working out")
class Bodybuilder(Gym):
    def workout(self):
        print(f"{self.name} is bodybuilding and lifting heavy weights")

class Calisthenics(Gym):
    def workout(self):
        print(f"{self.name} is doing calisthenics and using body weight as the workout")

bodybuilder = Bodybuilder("Arnold")
calisthenics = Calisthenics("Alex")
bodybuilder.workout()
calisthenics.workout()

bodybuilder.rest_day()
calisthenics.rest_day()
class Powerlifter(Gym):
    def __init__(self, name, max_weight):
        super().__init__(name)
        self.max_weight = max_weight
    def workout(self):
            print(f"{self.name} lifts {self.max_weight}kg!")

powerlifter = Powerlifter("Thor", 300)
powerlifter.workout()
powerlifter.rest_day()