import time
from rich.console import Console
from rich import print as rprint
from rich.progress import track
from Functions import medicalHistory
from Functions import requestFeedback
from Functions import submitReport
from Functions import progress_bar
import keyboard


console = Console()


class Menu:
    def __init__(self, option):

        self.option = option

    title = "Welcome"
    c = title.center(120)
    print("***********************************************************************************************************************")
    print(c)
    print("***********************************************************************************************************************")

    def mMenu(self):

        print("****************************************************")
        rprint("|                  [bold] NOBLE CURE [/]                    |")
        print("--------------------------------------------------")
        rprint("*      [1] Submit a Health report                  *")
        rprint("*      [2] Request a Health report feedback        *")
        rprint("*      [3] Medical History                         *")
        rprint("*      [4] Exit                                    *")
        print("****************************************************")
        self.option = int(input(">>  "))

        if isinstance(self.option, int):
            # if keyboard.read_key() == "q":
            #     time.sleep(0.25)
            #     print("Back to menu")
            #     console.print("Exiting...", style="Green")

            if self.option == 1:
                print("selected option" + "[" + str(self.option) + "]")
                submitReport.printthis()
                print("____________________________________________________")

            elif self.option == 2:
                print("selected option" + "[" + str(self.option) + "]")
                requestFeedback.printthis()
                print("____________________________________________________")

            elif self.option == 3:
                print("selected option" + "[" + str(self.option) + "]")
                medicalHistory.printthis()
                print("____________________________________________________")

            elif self.option == 4:
                print("selected option" + "[" + str(self.option) + "]")
                console.print("Exiting...", style="Green")

        else:
            console.print("Enter a valid choice", style="Red")