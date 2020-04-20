from exercise import Exercise
from student import Student
from cohort import Cohort
from instructor import Instructor

kennel = Exercise("Pet Kennel", "React")
studentExercises = Exercise("Student Exercises", "Python")
nutshell = Exercise("Nutshell", "JavaScript")
celebTribute = Exercise("Celebrity Tribute", "HTML + CSS")

c38 = Cohort("C38")
c37 = Cohort("C37")
c39 = Cohort("C39")

landon = Student("Landon", "Morgan", "@landon")
mike = Student("Mike", "Prince", "@mike")
michael = Student("Michael", "Clark", "@michael")
cody = Student("Cody", "Murdock", "@cody")
dingo = Student("Dingo", "LastName", "@dingo")

c38.add_person(landon)
c38.add_person(mike)
c37.add_person(michael)
c39.add_person(cody)
c39.add_person(dingo)

kristen = Instructor("Kristen", "Norris", "@kristen")
jisie = Instructor("Jisie", "David", "@jisie")
chase = Instructor("Chase", "Fite", "@chase")

c37.add_person(kristen)
c38.add_person(jisie)
c39.add_person(chase)

kristen.assign(michael, kennel)
kristen.assign(michael, studentExercises)

jisie.assign(mike, nutshell)
jisie.assign(mike, studentExercises)
jisie.assign(landon, kennel)
jisie.assign(landon, studentExercises)

chase.assign(cody, studentExercises)
chase.assign(cody, celebTribute)

students = list()
cohorts = list()

students.append(landon)
students.append(mike)
students.append(michael)
students.append(cody)
students.append(dingo)

cohorts.append(c37)
cohorts.append(c38)
cohorts.append(c39)

for cohort in cohorts:
    print(f'{cohort.name}')
    print(f'-------------')
    for student in students:
        if student.cohort == cohort.name:
            sentence = f'{student.first_name} is working on '
            if len(student.exercises) > 1:
                last_item = student.exercises[-1]
                del student.exercises[-1]
                for exercise in student.exercises:
                    sentence += f'{exercise.name}, '
                else:
                    sentence += f'and {last_item.name}.'
            elif len(student.exercises) == 1:
                sentence += f'{last_item.name}.'
                last_item = "."
            else:
                sentence += f'zero exercises currently.'
            print(f'{sentence}')
    print(f'')

print(f'-------------------')
print(dingo.exercises)