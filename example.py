import sqlite3
from my_tools import *



a = Employees("Петров", 'Игорь', "Васильевич", "22.10.1983", "+79207898778", 12, 1, 20000)

a.set_salary(10000)
a.set_phone("+7920746003")
em1 = Enterprise()
em1.add_emploer(a)
# print(em1.get_Employees()[0].get_salary())
new = Data_base()
new.create_essence('test_4')


# # text = "CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)"
# try:
# 	Data_base.create_new_query(text = "CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)")
# except Exception as ex:
# 	print(ex)
# # text = r"INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)"
# # Data_base.create_new_query(text)
# Data_base.conn_commite()
# Data_base.conn_close()