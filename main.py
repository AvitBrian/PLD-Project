import sys
import time
import datetime
from rich.console import Console
from rich import print as rprint
from Classes.Menu import Menu
from Classes.Patient import Patient
from Functions import progress_bar
today = datetime.date.today()
loop=0
name=None
age=None
choice=None
##############objects###################
p=Patient(name=name, age=age);
m=Menu(option=choice);
########################################
p.getNameAndAge();

progress_bar.loading();
print("Welcome "+p.name);
m.mMenu();
##############Running####################
a=1;

while a>0:
    if m.option==4:
        print(p.name, "logged out"); 
        break;
    else:
        print();
        print (today.strftime('%d, %b %Y'))
        p.printName();
        print();
        m.mMenu();
       
a+=a;



