import sqlite3
from sqlite3 import connect
import os


class People:
	def __init__(self, fam, name, sur_name, birthday, phone):
		self.fam = fam
		self.name = name
		self.sur_name = sur_name
		self.birthday = birthday
		self.phone = phone

	def get_fam(self):
		return self.fam

	def set_fam(self, new_fam):
		self.fam = new_fam

	def get_name(self):
		return self.name

	def set_name(self, new_name):
		if len(new_name) > 0:
			self.name = new_name

	def get_sur_name(self):
		return self.sur_name

	def set_sur_name(self, new_sur_name):
		self.sur_name = new_sur_name

	def get_birthday(self):
		return self.birthday

	def set_birthday(self, new_birthday):
		self.birthday = new_birthday

	def get_phone(self):
		return self.phone

	def set_phone(self, new_phone):
		new_phone = str(new_phone)
		if len(new_phone) != 12:
			result = 'Error: количество символов не соответствует формату'
		else:
			if new_phone[0] != '+':
				result = 'Error: первый символ должен быть: +'
			else:
				self.phone = new_phone
				result = None
		return result


class Employees(People):
	def __init__(self, fam, name, sur_name, birthday, phone, personal_id, departament_id, salary):
		super().__init__(fam, name, sur_name, birthday, phone)
		self.personal_id = personal_id
		self.departament_id = departament_id
		self.salary = salary

	def get_salary(self):
		return self.salary

	def set_salary(self, new_salary):
		self.salary = new_salary

	def get_departament_id(self):
		return self.departament_id

	def set_departament_id(self, new_departament_id):
		self.departament_id = new_departament_id


class Enterprise:
	def __init__(self):
		self.workers = []

	def add_emploer(self, employee):
		self.workers.append(employee)

	def get_Employees(self):
		if len(self.workers) > 0:
			return self.workers
		else:
			return None


class Data_base():
	def __init__(self):
		base_name = 'test'
		pass

	def get_connection(self, base_name):
		try:
			conn = sqlite3.connect(str(base_name) + '.db')
			print(dir(conn.cursor()))
			return conn
		except Exception as ex:
			print(ex)

	def create_essence(self, base_name, query = 'CREATE TABLE test (date text, symbol text, price real)'):
		try:
			# query = 'CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)'
			conn =self.get_connection(base_name)
			c = conn.cursor()
			c.execute(query)
			conn.commit()
			conn.close()
		except Exception as ex:
			print(ex)


		# return c

	# def create_new_query(self, text):
	# 	conn = self.conn
	# 	c = conn.cursor()
	# 	try:
	# 		c.execute(text)
	# 	except Exception as ex:
	# 		print(ex)

	# def conn_commite(self):
	# 	self.conn = conn
	# 	conn.commit()

	# def conn_close(self):
	# 	conn = self.conn
	# 	conn.close()