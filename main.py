import sys
import time
from rich.console import Console
from Classes.Menu import Menu
from Classes.Patient import Patient
loop=0
name=None
age=None
choice=None
##############objects###################
p=Patient(name=name, age=age);
m=Menu(option=choice);
########################################
p.getName();
p.getAge();
m.mMenu();


a=1;


while a>0:
    
    p.printName();
    m.mMenu();
    
    if m.option==4:
        print(p.name, "logged out"); 
        break;       
            
    
a+=a;
    


