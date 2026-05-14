# class Facade:
#     pass
#
# facade_1 = Facade()
# facade_1_type = type(facade_1)
# print(facade_1_type)
#
# class Grade:
#     minimum_passing = 65
#
# class Rules:
#     def washing_brushes(self):
#         return 'Point bristles towards the basin while washing your brushes'
#
# class Circle:
#
#     pi = 3.14
#
#     def __init__(self, diameter):
#         self.radius = 0.5 * diameter
#         print(f'New circle with diameter: {diameter}')
#
#     def area(self, radius):
#         area = pi * radius ** 2
#         return area
#
#     def circumference(self):
#         circumference = 2 * self.pi * self.radius
#         return circumference
#
#     def __repr__(self):
#         return f'Circle with radius {self.radius}'
#
#
# medium_pizza = Circle(12)
# teaching_table = Circle(36)
# round_room = Circle(11460)
#
# print(medium_pizza.circumference())
# print(teaching_table.circumference())
# print(round_room.circumference())
#
# print(medium_pizza.__repr__())
# print(teaching_table.__repr__())
# print(round_room.__repr__())
#
# print(dir(5))
#
# def this_function_is_an_object():
#     pass
#
# print(dir(this_function_is_an_object()))