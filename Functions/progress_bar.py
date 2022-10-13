from time import sleep
from rich import print as rprint
from rich.progress import track
def loads():
    sleep(0.01)
def loading():
    for _ in track(range(100), description='logging in'):
        loads()
    print("");
    rprint("[green]Logged in!");

