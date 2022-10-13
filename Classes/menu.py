import time
from rich.console import Console


console = Console()


class Menu:
    def __init__(self,option):
        
        self.option = option;
        
    
    title="Welcome"
    c= title.center(120);
    print("***********************************************************************************************************************")
    print(c);
    print("***********************************************************************************************************************")
    def mMenu(self):
        
       
            
            print("Choose your option")
            print("[1] Submit a Health report")
            print("[2] Request Health report feedback")
            print("[3] Medical History")
            print("[4] Exit")
            self.option = int(input(">>"))

            if self.option == 1:
                submitReport();
            elif self.option == 2:
                requestFeedback();
            elif self.option == 3:
                medicalHistory();
            elif self.option == 4:
                console.print("Exiting...", style="Green")
                time.sleep(3)
            else:
                console.print("Enter a valid choice", style="Red")
    
    
    

        
    



def medicalHistory():
    print ("this is your history")
    
def requestFeedback():
    print ("requested feedback!")

def submitReport():
    print ("Submitted request!")
 
