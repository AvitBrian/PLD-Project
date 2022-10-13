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
        
       
    
 

