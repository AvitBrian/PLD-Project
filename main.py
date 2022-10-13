import sys
import time
from rich.console import Console
from rich import print as rprint
from Classes.Menu import Menu
from Classes.Patient import Patient
from Functions import progress_bar
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
progress_bar.loading();
m.mMenu();
##############Running####################
a=1;

while a>0:
    if m.option==4:
        print(p.name, "logged out"); 
        break;
    else:
        p.printName();
        m.mMenu();
       
a+=a;



