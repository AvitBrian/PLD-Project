import sys
from mainMenu import *
from rich.console import Console 

console=Console()

console.print("***********************************************************************************************************************");
console.print("NobleCure");
name= input ("Reply: ");
console.print("Nice to meet you then ",name); 
mMenu()