import time
from rich.console import Console

pname = ""
age = None

console = Console()


class Patient:
    def __init__(self, p_name, p_age,):
        '''setting attributes'''
        self.p_name = p_name
        self.p_age = p_age

    @property
    def p_age(self):
        return (self.__p_age)

    @p_age.setter
    def p_age(self, value):
        value = input("age: ")
        self.__p_age = value

    @property
    def p_name(self):
        return (self.__p_name)

    @p_name.setter
    def p_name(self, value):
        value = input("Name: ")
        self.__p_name = value

    def printName(self):
        print(self.__p_name)

    def printAge(self):
        print(self.__p_age)
