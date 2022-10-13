import time
from rich.console import Console
from rich import print as rprint
from rich.progress import track
from Functions import medicalHistory
from Functions import requestFeedback
from Functions import submitReport
from Functions import progress_bar


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
        
       
            print(" __________________________________________________")
            print("|                                                  |")
            rprint("|                  [bold] NOBLE CURE [/]                    |")
            print("|--------------------------------------------------|")
            rprint("|      [1] Submit a Health report                  |")
            rprint("|      [2] Request Health report feedback          |")
            rprint("|      [3] Medical History                         |")
            rprint("|      [4] Exit                                    |")
            print("|__________________________________________________|")
            self.option = int(input(">>  "))

            if self.option == 1:
                print("selected option"+ "[" + str(self.option) + "]");
                time.sleep(1)
                submitReport.printthis();
                
            elif self.option == 2:
                print("selected option"+ "[" + str(self.option) + "]");
                time.sleep(1)
                requestFeedback.printthis()
                
            elif self.option == 3:
                print("selected option"+ "[" + str(self.option) + "]");
                time.sleep(1)
                medicalHistory.printthis();
                
            elif self.option == 4:
                print("selected option"+ "[" + str(self.option) + "]");
                time.sleep(1)
                
                console.print("Exiting...", style="Green")
                
                
            else:
                print("selected option"+ "[" + str(self.option) + "]");
                console.print("Enter a valid choice", style="Red")
                
    
    
    

        
    



# def medicalHistory():
#     print ("this is your history")
    
# def requestFeedback():
#     print ("requested feedback!")

# def submitReport():
#     print ("Submitted request!")
 
