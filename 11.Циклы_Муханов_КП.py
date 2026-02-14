'''1'''
# board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
# sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
# for game in board_games:
#     print(game)
# for game in sport_games:
#     print(game)
'''2'''
# promise = "I will not chew gum in class"
# for i in range(5):
#     print(promise)
'''3'''
# students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
# students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
# for st in students_period_A:
#     students_period_B.append(st)
#     print(st)
# print(students_period_B)
'''4'''
# dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
# dog_breed_I_want = 'dalmatian'
# for i in dog_breeds_available_for_adoption:
#     print(i)
#     if i == dog_breed_I_want:
#         print("У них есть собака, которую я хочу!")
#         break
#
'''5'''
# sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
# scoops_sold = 0
# scoops_sold1 = 0
# for i in sales_data:
#     scoops_sold1 += sum(i)
#     for j in i:
#         scoops_sold += j
# print(scoops_sold, scoops_sold1)
'''6'''
single_digits = list(range(10))
squares = []
for i in single_digits:
    print(i)
    squares.append(i**2)
print(squares)
cubes = [digit**3 for digit in single_digits]
print(cubes)