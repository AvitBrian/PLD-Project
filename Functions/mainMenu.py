import time
from rich.console import Console

console = Console()


def mMenu():
    print("Choose your option")
    print("[1] Submit a Health report")
    print("[2] Request Health report feedback")
    print("[3] Medical History")
    print("[4] Exit")
    reply = input(">>")
    
    
    if (reply==1):
        print(reply, "st Option was chosen.")
   
