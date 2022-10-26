"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""
# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a  method  (and a new variable) to get student's overall mark (use average)

class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()


class CFGStudent(Student):

    def add_subject(self, subject, grade):
        self.subjects[subject] = grade

    def remove_subject(self, subject):
        print('**** {} is removed'.format(subject))
        self.subjects.pop(subject)

    def view_subjects(self):
        print('**** {}\'s record is as follows'.format(self.name))
        for subject, grade in self.subjects.items():
            print(subject, grade)

    def get_average(self):
        total = sum(self.subjects.values())
        number_of_subjects = len(self.subjects.values())

        if number_of_subjects: # to avoid zero division error
            print('The overall grade is {} \n'.format(total / number_of_subjects))
        else:
            print('No subject data is available.')

keiko = CFGStudent('Keiko', 38, 1)

# Add subjects:
keiko.add_subject('Homework1', 100)
keiko.add_subject('Homework2', 90)
keiko.add_subject('Homework3', 80)

keiko.view_subjects()

# Remove a subject:
keiko.remove_subject('Homework2')

keiko.view_subjects()

# get student's overall mark
keiko.get_average()

# if there is no grade for a student
emily = CFGStudent('Emily', 20, 2)
emily.view_subjects()
emily.get_average()
