'''1'''
# def f_to_c(f_temp):
#     c_temp = (f_temp - 32)*(5/9)
#     return c_temp
# f100_in_celsius = f_to_c(100)
#
# def c_to_f(c_temp):
#     f_temp = c_temp*(9/5) + 32
#     return f_temp
# c0_in_fahrenheit = c_to_f(0)
# print(f100_in_celsius, c0_in_fahrenheit)
'''2'''
# def get_force(m,a):
#     return m*a
# train_mass = 22680
# train_acceleration = 10
# train_force = get_force(train_mass,train_acceleration)
# print(train_force)
# print(f'Поезд GE поставляет {train_force} ньютонов силы')
# def get_energy(m,c=3*(10**8)):
#     return m*(c**2)
# bomb_mass=1
# bomb_energy = get_energy(bomb_mass)
# print(f'{bomb_mass} кг бомбы составляет {bomb_energy} Джоулей')
# def get_work(m,a,s):
#     f = get_force(m,a)
#     A = f*s
#     return A
# train_distance = 100
# train_work = get_work(train_mass,train_acceleration,train_distance)
# print(f'Поезд выполняет {train_work} Джоулей за {train_distance} метров')
'''3'''
# clothes = 'домашняя одежда'
# def itog(d):
#     ans = f'{d} лучше всего подходит {clothes}'
#     return ans
#
# def itog1(d):
#     ans = f'{d} лучше всего подходит {meal}'
#     return ans
# meal = 'хрен'
#
# time = ['Утром', "Днем", "Вечером", "Ночью"]
# eat = ['На завтрак',"На обед","На ужин"]
# print('У меня большой гардероб')
#
# print('\n'.join(itog(i) for i in time))
#
# print('мои предпочтения в еде')
# print('\n'.join(itog1(i) for i in eat))
'''4'''
# def username(us,IP):
#     spisok = ['Дмитрий номер APM 1', 'Ангелина номер APM 2', "Василий номер APM 3", 'Екатерина номер APM 4']
#     if us + ' номер APM ' + IP in spisok:
#         return "Добро пожаловать"
#     elif us + ' номер APM ' + IP not in spisok and us == 'Дмитрий':
#         return 'Дмитрий, твое рабочее место находится в другой комнате. Отойди от чужого компьютера и займись работой!'
#     else:
#         return "Логин или пароль не верный, попробуйте еще раз"
# print(username(input('Введите имя:'),input('Введите номер APM:')))
'''5'''
# num = float(input('Введите балл:'))
# def grades(grade):
#     if grade >= 4.0:
#         return 'A'
#     elif 4 > grade >= 3:
#         return 'B'
#     elif 3 > grade >= 2:
#         return 'C'
#     elif 2 > grade >= 1:
#         return 'D'
#     elif 1 > grade >= 0:
#         return 'F'
#     else:
#         return 'Некорректный балл'
# print(grades(num))
