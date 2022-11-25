import sys
import time
import datetime
from rich.console import Console
from rich import print as rprint
from Classes.Menu import Menu
from Classes.Patient import Patient
from Functions import progress_bar
import keyboard
import random
today = datetime.date.today()
loop = 0
patient_name = None
patient_age = None
choice = None
##############objects###################
p = Patient(p_name=patient_name, p_age=patient_age)
m = Menu(option=choice)
########################################
progress_bar.loading()
patient_id = random.randint(1000, 9000)
patient_name = p.p_name
patient_age = p.p_age
with open("database.txt", mode="a", encoding="utf-8") as f:
    f.write("\t \"{}\": {{ \"{}\": \"{}\" }},\n".format(
        patient_id, patient_name, patient_age))
    f.close()
print("Welcome " + patient_name)
m.mMenu()
##############Running####################

a = 1

while a > 0:
    if m.option == 4:
        print(p.p_name, "logged out")
        break
    else:
        print()
        print(today.strftime('%d, %b %Y'))
        p.printName()
        print()
        m.mMenu()

a += a
