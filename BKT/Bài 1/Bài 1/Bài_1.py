from tkinter.filedialog import asksaveasfile


class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    def describe(self):
        return f"Name: {self.name}, Year of Birth: {self.yob}"

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        return f"{super().describe()}, Grade: {self.grade}"

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        return f"{super().describe()}, Subject: {self.subject}"

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        return f"{super().describe()}, Specialist: {self.specialist}"

class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def describe(self):
        description = f"Ward Name: {self.name}\n"
        for person in self.people:
            description += person.describe() + "\n"
        return description

    def AddPerson(self, person):
        self.people.append(person)

    def CountDoctor(self):
        cnt = 0
        for person in self.people:
            if isinstance(person, Doctor):
                cnt += 1
        return cnt

    def SortAge(self):
        self.people = sorted(self.people, key = lambda person: person.yob)

    def AveTeacherYearOfBirth(self):
        cnt = 0
        sum = 0
        for person in self.people:
            if isinstance(person, Teacher):
                cnt += 1
                sum += person.yob
        return sum / cnt

ward = Ward("Ward A")
ward.AddPerson(Student("Alice", 2005, "10th Grade"))
ward.AddPerson(Teacher("Mr. Smith", 1980, "Mathematics"))
ward.AddPerson(Doctor("Dr. Brown", 1975, "Cardiology"))
ward.AddPerson(Teacher("Mr. Yellow", 2000, "Biology"))

print(ward.describe())
print("Number of doctor: ", ward.CountDoctor())
ward.SortAge()
print("Age after sort: ")
print(ward.describe())
print("Average of birth: ", ward.AveTeacherYearOfBirth())
