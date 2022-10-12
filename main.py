import sys
from Functions import mainMenu
from rich.console import Console
a = 1
console = Console()

console.print("***********************************************************************************************************************")
console.print("NobleCure")
name = input("Name: ")
console.print("Welcome ", name)
mainMenu.mMenu()
