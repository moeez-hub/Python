class Student:
    def __init__(self, stu_name, english_marks, math_marks, science_marks):
        self.stu_name = stu_name
        self.english = english_marks
        self.math = math_marks
        self.science = science_marks

    def display(self):
        print(f"Student Name: {self.stu_name}")
        print(f"English Marks: {self.english}")
        print(f"Math Marks: {self.math}")
        print(f"Science Marks: {self.science}")

student1 = Student("Alice", 85, 90, 78)
student1.display()