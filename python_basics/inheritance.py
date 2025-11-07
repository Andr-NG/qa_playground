class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_info(self):
        return f"{self.name}, age {self.name}"


class Student(Person):

    def __init__(
        self, name: str, age: int, qualifications: list, is_enrolled: bool = False
    ):
        super().__init__(name, age)
        self.qualifications = qualifications
        self.is_enrolled = is_enrolled

    def enroll(self):
        self.is_enrolled = True

    def can_apply_for_advanced_course(self, required_grades):

        if any(
            self.qualifications[ind][1] < val[1]
            for ind, val in enumerate(required_grades)
        ):
            return "NO"
        return "YES"


student_1 = Student(
    "Alice", 18, [("maths", 10), ("physics", 10), ("english", 10), ("chemistry", 9)]
)
student_2 = Student(
    "Bob", 18, [("maths", 7), ("physics", 8), ("english", 7), ("chemistry", 9)]
)
required_grades = [("maths", 7), ("physics", 7), ("english", 7), ("chemistry", 7)]

print(student_2.can_apply_for_advanced_course(required_grades))
