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
p=Patient(name=name, age=age)
m=Menu(option=choice);
########################################
p.getName()
m.mMenu();
print(m.option);

a=1


while a>0:
    p.printName();
    if (m.option in range(4)):
        m.mMenu();
        print(m.option);
    else:
        break;
a+=a;
    


