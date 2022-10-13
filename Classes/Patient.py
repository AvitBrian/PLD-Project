import time
from rich.console import Console

name=""
age=None

console = Console()


class Patient:
    def __init__(self,name,age,):
        
        self.name = name;
        self.age = age;
        
    def getName(self):
        self.name=input("Name: ")
        name=self.name;
    def printName(self):
        print(self.name);
    def getAge(self):
        age=self.age=input("Age: ")
    def printAge(self):
        print(self.age);
        
p=Patient(name=name, age=age)
    
 

