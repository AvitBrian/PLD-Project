import time
from rich.console import Console

console = Console()




def mMenu():
    a = 1
    while a > 0:
        
        print("Choose your option");
        print("[1] Submit a Health report");
        print("[2] Request Health report feedback");
        print("[3] Medical History");
        print("[4] Exit");
        reply = int(input(">>"));

        if reply == 1:
            print(str(reply) + "st Option was chosen.");
        elif reply == 2:
            print(str(reply) + "nd Option was chosen.");
        elif reply == 3:
            print(str(reply) + "rd Option was chosen.");
        elif reply == 4:
            console.print("Exiting...", style="Green");
            time.sleep(5);
            break;
        else:
            console.print("Enter a valid choice", style="Red");
    a += a
