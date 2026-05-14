
"1"
contains_a = lambda my_input: "a" in my_input #"a" английская
print(contains_a(input()))

"2"
long_string = lambda my_input: len(my_input) > 12
print(contains_a(input()))

"3"
end_in_a = lambda my_input: my_input[-1] == 'a'
print(contains_a(input()))

"4"
even_or_odd = lambda my_input:"Четное" if my_input % 2 == 0 else 'Нечетное'
print(even_or_odd(int(input())))

"5"
multiple_of_three = lambda my_input:"Кратное трем" if my_input % 3 == 0 else 'Не кратное'
print(multiple_of_three(int(input())))

"6"
rate_movie = lambda rating: "Мне понравился этот фильм" if rating > 8.5 else "Этот фильм был не очень хорошим"
print(rate_movie(float(input())))