import time
from rich.console import Console 

console=Console()

def mMenu():
    print("Choose your option");
    print("[1] Submit a Health report");
    print("[2] Request Health report feedback");
    print("[3] Medical History");
    print("[4] Exit");
    reply=input(">>");
    if reply == 1:
        print ("%ist Option was chosen." %reply);
    elif reply==2:
        print ("{reply}nd Option was chosen.");
    elif reply==3:
        print ("{reply}rd Option was chosen.");
    elif reply==4:
        print ("Exiting...", style="Success")
        time.sleep(5);
    else:
        console.print("Enter a valid choice" ,style="Red" )
