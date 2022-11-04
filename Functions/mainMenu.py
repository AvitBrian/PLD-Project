import time
from rich.console import Console
from Functions import submitReport
from Functions import requestFeedback
from Functions import medicalHistory

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
            submitReport.printthis();
        elif reply == 2:
            requestFeedback.printthis();
        elif reply == 3:
            medicalHistory.printthis();
        elif reply == 4:
            console.print("Exiting...", style="Green");
            time.sleep(5);
            break;
        else:
            console.print("Enter a valid choice", style="Red");
    a += a
def medicalHistory():
    print ("this is your history")