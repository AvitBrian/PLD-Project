import time
from rich.console import Console


console = Console()


class Patient:
    def __init__(self,name,age,):
        
        self.name = name;
        self.age = age;
        
    def getName(self):
        self.name=input("Name: ")
    def printName(self):
        print(self.name);
    def getAge(self):
        self.age=input("Age: ")
    def printAge(self):
        print(self.age);
        
       
    
 

