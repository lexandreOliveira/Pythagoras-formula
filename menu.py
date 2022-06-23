import os
from rich import print


def menu(): 
    print('*' * 52)
    print(f'{os.linesep}           >>>[on red] PYTHAGORAS FORMULA [/] <<<<{os.linesep}')
    print('')
    print(f'Choose the option you want to know the value!!!{os.linesep} ')
    print(f'{os.linesep}    Select: {os.linesep}'.center(50))
    print(f'{os.linesep}            "h" [on yellow]of the Hypotenuse[/]{os.linesep}')
    print(f'{os.linesep}            "b" [on yellow]of the cathetus B[/] {os.linesep}')
    print(f'{os.linesep}            "c" [on yellow]of the cathetus C[/] {os.linesep}')
    print('*' * 52)

menu()
