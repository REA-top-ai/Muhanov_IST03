import sys
sys.setrecursionlimit(10000)
"1"
def fact(num):
    answer = 1
    if num == 0:
        return 1
    for i in range(1,abs(num+1)):
        answer *= i
    return answer

def fact_recourse(num):
    if num == 0:
        return 1
    return num*fact_recourse(num-1)

my_input = int(input())
print(fact(my_input))
print(fact_recourse(my_input))
"2"
def kvadr(mas):
    otv = []
    for i in mas:
        otv.append(i**2)
    return otv


def kvadr_recourse(mas,otv):
    if len(mas) == 0:
        return otv
    otv.append(mas[0]**2)
    return kvadr_recourse(mas[1:],otv)

mas = [1, 2, 3, 4, 5]
otv = []
print(kvadr(mas))
print(kvadr_recourse(mas,otv))