# -*- coding:cp1251 -*-

class Soup:

	def __init__(self, ing):
		self.ing = ing

	def show_my_soup(self):
		if(self.ing != ""): print("��� - " + self.ing)
		else: print("������� �������. ")