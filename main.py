class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
       return(f'Имя: {self.name}\nФамилия: {self.surname}\n'
             f'Средняя оценка за домашние задания: {self.average_grade()}\n'
             f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
             f'Завершенные курсы: {", ".join(self.finished_courses)}\n')

    def add_course(self, course_name):
        self.courses_in_progress.append(course_name)

    def complete_course(self, course_name):
        if course_name in self.courses_in_progress:
            self.courses_in_progress.remove(course_name)
            self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        _all_grades = sum(self.grades.values(), [])
        return sum(_all_grades)/len(_all_grades)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student!')
            return
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        return(f'Имя: {self.name}\nФамилия: {self.surname}\n'
             f'Средняя оценка за лекции: {self.average_grade()}\n')

    def average_grade(self):
        _all_grades = sum(self.grades.values(), [])
        return sum(_all_grades)/len(_all_grades)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer!')
            return
        return self.average_grade() < other.average_grade()


class Reviewer(Mentor):
    def __str__(self):
        return(f'Имя: {self.name}\nФамилия: {self.surname}\n')

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def average_grades_for_course(course, individuals):
    _result = {}
    for individual in individuals:
        if isinstance(individual, Lecturer) and course in individual.courses_attached:
            _result[f'{individual.name} {individual.surname}'] = sum(individual.grades[course])/len(individual.grades[course])
    for individual in individuals:
        if isinstance(individual, Student) and course in individual.finished_courses:
            _result[f'{individual.name} {individual.surname}'] = sum(individual.grades[course])/len(individual.grades[course])
    return _result


first_lecturer = Lecturer('Владимир', 'Куликов')
first_lecturer.courses_attached += ['Основы языка программирования Python', 'ООП и работа с API']

second_lecturer = Lecturer('Евдокия', 'Корнеева')
second_lecturer.courses_attached += ['Git — система контроля версий']

first_student = Student('Марк', 'Прокофьев', 'Мужской')
second_student = Student('Полина', 'Семенова', 'Женский')

first_student.add_course('Основы языка программирования Python')
second_student.add_course('Основы языка программирования Python')

first_student.rate_hw(first_lecturer, 'Основы языка программирования Python', 10)
second_student.rate_hw(first_lecturer, 'Основы языка программирования Python', 9)

first_reviewer = Reviewer('Артём', 'Бирюков')
second_reviewer = Reviewer('Арина', 'Павлова')

first_reviewer.rate_hw(first_student, 'Основы языка программирования Python', 8)
first_reviewer.rate_hw(second_student, 'Основы языка программирования Python', 9)

first_student.complete_course('Основы языка программирования Python')
first_student.add_course('Git — система контроля версий')

second_student.complete_course('Основы языка программирования Python')
second_student.add_course('Git — система контроля версий')

first_student.add_course('ООП и работа с API')

first_student.rate_hw(second_lecturer, 'Git — система контроля версий', 7)
second_student.rate_hw(second_lecturer, 'Git — система контроля версий', 9)

second_reviewer.rate_hw(first_student, 'Git — система контроля версий', 10)
second_reviewer.rate_hw(second_student, 'Git — система контроля версий', 9)

first_student.complete_course('Git — система контроля версий')
first_student.add_course('ООП и работа с API')

second_student.complete_course('Git — система контроля версий')
second_student.add_course('ООП и работа с API')

second_reviewer.rate_hw(second_student, 'ООП и работа с API', 10)
second_student.rate_hw(first_lecturer, 'ООП и работа с API', 9)
second_student.complete_course('ООП и работа с API')

print(first_lecturer)
print(second_lecturer)

print(first_lecturer < second_lecturer)

print(first_student)
print(second_student)

print(first_student < second_student)

print(first_reviewer)
print(second_reviewer)

print(average_grades_for_course('Основы языка программирования Python', [first_student, second_student]))
print(average_grades_for_course('Git — система контроля версий', [first_student, second_student]))
print(average_grades_for_course('ООП и работа с API', [first_student, second_student]))

print(average_grades_for_course('Основы языка программирования Python', [first_lecturer, second_lecturer]))
print(average_grades_for_course('Git — система контроля версий', [first_lecturer, second_lecturer]))
print(average_grades_for_course('ООП и работа с API', [first_lecturer, second_lecturer]))

