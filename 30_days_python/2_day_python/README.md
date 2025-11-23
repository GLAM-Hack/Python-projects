print('Hello World!') #выводит на экран слова и тд

len('Hello World!') #считает длину. для списков, строк и элементов

type('Hello Woeld!') #функция которая возвращает тип объекта

str(10) #для преобразования любого объекта в его текст

int('10') #работает только с целыми числами

float(10) #переобразует из целого в дробное

input('Enter you name') #можно записать совой ответ

min(20, 30, 40, 50) #показывает самый минимальный из аргументов

max(20, 30, 40, 50) #показывает самый максимальный из аргументов

min([20, 30, 40, 50]) #показывает самый минимальный из списка

max([20, 30, 40, 50]) #показывает самый максимальный из списка

sum([20, 30, 40, 50]) #сумирует все в один ответ из списка

#пример названия переменых

#first_name = 'Asabeneh'
#last_name = 'Yetayeh'
#country = 'Finland'
#city = 'Helsinki'
#age = 250
#is_married = True
#skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
#person_info = {
#   'firstname':'Asabeneh',
#   'lastname':'Yetayeh',
#   'country':'Finland',
#   'city':'Helsinki'
#   }

#использовать функции print and len

print('Hello, World!')
print('Hello',',', 'World','!')
print(len('Hello, World!'))

#---------------------------------------------------------------------------

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City:', city)
print('Age', age)
print('Married', is_married)
print('Skills:', skills)
print('Person information:', person_info)

#----------------------------------------------------------------------------

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#----------------------------------------------------------------------------

first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

#---------------------------------------------------------------------------

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250

#пример аргумента types

print(type('Asabeneh')) 	#str
print(type(first_name)) 	#str
print(type(10))			#int
print(type(3.14))		#float
print(type(1+ 1j))		#complex
print(type(True))		#bool
print(type([1, 2, 3, 4]))	#list
print(type({'name' : 'Asabeneh'})) #dict
print(type((1,2)))		   #tuple
print(type(zip([1,2],[3,4])))	   #zip


#пример аргументов int,float,str,list,set

num_int = 10
print('num_int',num_int)         #10
num_float = float(num_int)
print('num_float:', num_float)   #10.0

gravity = 9.81
print(int(gravity))             #9

num_int = 10
print(num_int)                  #10
num_str = str(num_int)
print(num_str)                  #'10'

num_str = '10.6'

num_float = float(num_str)
print('num_float', float(num_str))  #10.6
num_int = int(num_float)
print('num_int', int(num_int))      #10

first_name = 'Asabeneh'
print(first_name
first_name_to_list = list(first_name)
print(first_name_to_list)
