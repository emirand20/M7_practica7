
#Crear un csv
import csv

with open('texto.csv', 'w') as csvfile:
    fieldnames = ['Name', 'Surname', 'Age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows([{'Age': '18', 'Name': 'Alex', 'Surname': 'Brian'},
                     {'Age': '22', 'Name': 'Kennzy', 'Surname': 'Timothy'}])

print("writing complete")

#Leer un csv y muestra por consola
import csv

with open('texto.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

    print(data)

#Crear una funcion que lea un excel

import openpyxl

book = openpyxl.load_workbook('Python.xlsx')
sheet = book.active

a1 = sheet['A1']
a2 = sheet['A2']

print(a1.value)
print(a2.value)
print(type(a1.value))

book.save('Python.xlsx')

#Crear una funcion que crea un excel(Funcion a medias no creada)
from openpyxl import Workbook
from openpyxl.styles import Font


book = Workbook()
sheet = book.active

sheet['A1'] = 5
sheet['A2'] = 10

sheet['B1'] = 'rango'
sheet['B1'].font = Font(color='FF0000', bold=True)
for i in range(2, 15):
    sheet[f'B{i}'] = i**2

book.save()