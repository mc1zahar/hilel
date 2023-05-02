import this
import math as mt
import datetime
import art

a = 1
b = 5
c = 4
x1 = (-b-mt.sqrt(b**2-(4*a*c)))/(2*a)
x2 = (-b+mt.sqrt(b**2-(4*a*c)))/(2*a)
print('x1= ', int(x1), ',', 'x2= ', int(x2))
name = input("Введіть ваше ім'я: ")
print("Привіт", name)
kurs = 40
grivna = float(input("Введіть скількі гривень ви хочете обміняти :", ))
current_date = datetime.date.today()
print("Станом на ", current_date, 'це становить ', grivna/kurs, "доларів")
art_name = art.text2art('ARTEM')
print("hello", art_name)
print('hello')
