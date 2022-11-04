import time
from rich.console import Console

name="";
age=None

console = Console()


class Patient:
    def __init__(self,name,age,):
        
        self.name = name;
        self.age = age;
        
    def getNameAndAge(self):
        name=self.name=input("Name: ");
        age=self.age=input("Age: ");
        #will add try and catch to make sure the errors are caught and printed to the terminal
        data= name ,  age;
        file = open('database.txt', 'a');
        file.write(str(data) +'\n');
        file.close();
        
    def printName(self):
        print(self.name);
    def printAge(self):
        print(self.age);
        
p=Patient(name=name, age=age)

