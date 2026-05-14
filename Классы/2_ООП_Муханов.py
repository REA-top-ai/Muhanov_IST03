# from abc import ABC, abstractmethod
#
# class AbstractEmployee(ABC):
#     new_id = 1
#     def __init__(self):
#         self.id = AbstractEmployee.new_id
#         AbstractEmployee.new_id += 1
#
#     @abstractmethod
#     def say_id(self):
#         pass
#
# class Employee(AbstractEmployee):
#     def __init__(self, _name = None):
#         super().__init__()
#         self._name = _name
#         # self._id = 111
#         # self.__id = 5555
#
#     def get_name(self):
#         return self._name
#
#     def del_name(self):
#         del self._name
#
#     def say_id(self):
#         print(f'My id is {self.id}')
#
# class User():
#     def __init__(self, username, role):
#         self.username = username
#         self.role = role
#
#     def say_user_info(self):
#         print(f'My username is {self.username}, I am an {self.role}')
#
# class Admin(Employee, User):
#     def __init__(self):
#         Employee.__init__(self)
#         User.__init__(self, self.id, "Admin")
#
#     def say_id(self):
#         super().say_id()
#         print('I am an Admin')
#
# class Manager(Admin):
#     def say_id(self):
#         super().say_id()
#
# # meeting = [Employee(), Admin(), Manager()]
# #
# # for human in meeting:
# #     human.say_id()
#
# class Meeting():
#     def __init__(self):
#         self.attendees = []
#
#     def __add__(self, e):
#         self.attendees.append(e)
#
#     def __len__(self):
#         for human in self.attendees:
#             human.say_id()
#         return len(self.attendees)
#
#
# e1 = Employee()
# e2 = Employee()
# e3 = Admin()
# e4 = Manager()
#
# # e1.say_id()
# # e2.say_id()
# # e3.say_id()
# # e3.say_user_info()
# # e4.say_id()
#
# m1 = Meeting()
#
# m1 + e1
# m1 + e2
# m1 + e3
#
# print(m1.__len__())
#
#
# # e = Employee()
# # print(dir(e))