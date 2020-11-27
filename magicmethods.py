# TASK4. MAGICMETHODS. ATABEK. HOMEWORK
# 1)
'''Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
элементов начиналась с 1. Например:
x = MyList([1,2,3,4,5])
x[1] → 1'''

# class MyList(list):
#     def things(self, item):
#         num = self.index(item) + 1
#         return num 
    
# obj1 = MyList([1, 2, 3, 4, 5])
# print(obj1[1])

# 2)
'''Напишите класс Student, который описывает студента. У студента есть следующие
аттрибуты: имя, фамилия, класс, и оценки по предметам в следующем виде: {‘history’: 89, history’: 89,
‘history’: 89, math’: 100, ‘history’: 89, literature’: 88}. Сделайте таким образом, чтобы сравнение студентов между
собой производилось по средней оценке студента по предметам.'''

# class Student(dict):
#     def __init__(self, name, last_name, grades, subject_):
#         self.name = name
#         self.last_name = last_name
#         self.grades = grades
#         self.subject_ = subject_

#     def final_score(self, value):
#         score = 0
#         for item in value.values():
#             score += item
#             self.score = score
    
#     def __gt__(self, other):
#         if self.score > other.score:
#             print(f'{self.name} all the grades {self.score} more than {self.other}{self.score}')
#         else:
#             print(f'{self.name} all the grades {self.score} less than {self.other}{self.score}')
    
#     def __lt__(self, other):
#         if self.score < other.score:
#             print(f'{self.name} all the grades {self.score} less than {other.name} {other.score}')
#         else:
#             print(f'{self.name} all the grades {self.score} more than {other.name} {other.score}')

# tilek = Student('Tilek', 'Amanov', {'history': 90, 'math': 85, 'ICT': 80}, 10)
# tilek.final_score(tilek.grades)
# beko = Student('Beko', 'Tilekov', {'history': 95, 'math': 67, 'ICT': 54}, 10)
# beko.final_score(beko.grades)
# tilek < beko
# beko < tilek

# 3)
# class Complex(object):
#     def init(self, real, imaginary):
#         self.real = real
#         self.imaginary = imaginary

#     def __add__(self, no):
#         return Complex(self.real + no.real, self.imaginary + no.imaginary)

#     def __sub__(self, no):
#         return Complex(self.real - no.real, self.imaginary - no.imaginary)

#     def __mul__(self, no):
#         return Complex(self.real * no.real - self.imaginary * no.imaginary,
#                        self.real * no.imaginary + self.imaginary * no.real)

#     def __truediv__(self, no):
#         factor = no.real2 + no.imaginary2
#         return Complex((self.real * no.real + self.imaginary * no.imaginary) / factor,
#                        (self.imaginary * no.real - self.real * no.imaginary) / factor)

#     def __mod__(self):
#         return Complex((self.real2 + self.imaginary2) ** (1 / 2), 0)








