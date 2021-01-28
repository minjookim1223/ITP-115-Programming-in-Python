# Minjoo Kim
# ITP 115, Fall 2019
# Lab 12-1
# minjook@usc.edu

MAX_COURSES = 6


class Student(object):

    def __init__(self, studentName, studentID):
        self.name = studentName
        self.idNumber = studentID
        self.courses = []

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getID(self):
        return self.idNumber

    def setID(self, newID):
        self.idNumber = newID

    def getCourses(self):
        return self.courses

    def getNumberOfCourses(self):
        return len(self.courses)

    def addCourses(self, course):
        courseNumber = self.getNumberOfCourses()
        if courseNumber <= MAX_COURSES:
            self.courses.append(course)
            return True
        else:
            return False

    def __str__(self):
        courses = ""
        for i in range (len(self.courses)):
            courses += ("\t-" + self.courses[i] + "\n")

        s = "Student: " + self.name + ", ID: " + str(self.idNumber) + ", enrolled in " + str(len(self.courses)) + (
            " course(s):\n" + courses)

        return s


def main():
    print("Welcome to the student registration system!\n")

    student1 = Student("Jay", 1)
    student2 = Student("Thomas", 2)
    student3 = Student("Jae", 3)
    student4 = Student("Minjoo", 4)

    key = True
    while key:
        print("Students:")
        print("1) " + student1.name)
        print("2) " + student2.name)
        print("3) " + student3.name)
        print("4) " + student4.name)

        select = input("Select a student from the list (1-4): ")
        course = input("Enter the course the student is registering for: ")

        if int(select) == 1:
            added = student1.addCourses(course)
        elif int(select) == 2:
            added = student2.addCourses(course)
        elif int(select) == 3:
            added = student3.addCourses(course)
        elif int(select) == 4:
            added = student4.addCourses(course)
        else:
            print("Wrong student. Try again.")
            added = False

        if added:
            print("Course registration successful")
        else:
            print("Course registration unsuccessful. You went overboard.")

        askContinue = input("Would you like to continue registering? (y/n): ")
        print("")
        if askContinue == "y":
            key = True
        else:
            key = False
            print(student1, end="")
            print(student2, end="")
            print(student3, end="")
            print(student4, end="")


main()
