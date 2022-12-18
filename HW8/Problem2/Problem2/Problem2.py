# -*- coding:cp1251 -*-

import random

class Student:
	def __init__(self, name, group):
		self.name = name
		self.group = group
		self.progress = []

	def add_grade(self, grade):
		self.progress.append(grade)

	def get_grades(self):
		return self.progress

	def get_group(self):
		return self.group

	def get_name(self):
		return self.name

	def get_avgrd(self):
		sum_ = 0
		for i in range(len(self.get_grades())):
			sum_ += self.get_grades()[i]
		return (sum_)/(len(self.get_grades()))

class Group:
	def __init__(self, group):
		self.group = group
		self.students = []
		self.num = 0

	def add_student(self, stdt):
		if stdt.get_group() == self.group:
			self.students.append(stdt)
			self.num += 1
			print("Студнет добавлен! (" + stdt.get_name() + ")")
		else: print("Студнет не из этой группы! (" + stdt.get_name() + ")")

	def get_num(self): return self.num

groupone = Group(1)

a1 = Student("Andrey", 1)
a2 = Student("Vasya", 1)
a3 = Student("Artyom", 1)
a4 = Student("Roman", 2)

groupone = Group(1)

groupone.add_student(a1)
groupone.add_student(a2)
groupone.add_student(a3)
groupone.add_student(a4)

print()

for i in range(groupone.get_num()):
	for j in range(random.randint(5, 10)):
		groupone.students[i].add_grade(random.randint(1, 10)) # Не очень хочется каждому студенту отдельно добавлять оценки, поэтому тут генератор, но если поставить максимальный балл 6 вместо 10, то окажется что вся группа учится так себе.

for i in range(groupone.get_num()):
	print("Оценки студента с именем " + groupone.students[i].get_name() + ": ")
	print(groupone.students[i].get_grades())

print()

for i in range(groupone.get_num()):
	if not(groupone.students[i].get_avgrd()>=5):
		print("Студент с именем " + groupone.students[i].get_name() + " учится плохо. ")

print()