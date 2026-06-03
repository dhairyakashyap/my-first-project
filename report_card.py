class ReportCard:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

student1 = ReportCard("Alice", 85)
student2 = ReportCard("bob", 35)
print(f"{student1.name} has a grade of {student1.grade()}")
print(f"{student2.name} has a grade of {student2.grade()}")