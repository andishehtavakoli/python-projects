from termcolor import colored, cprint
from typing import List, Tuple





def print_success(text, end=' '):
    print(colored(text, 'green', attrs=['reverse']), end=' ')
  

def print_warning(text, end=' '):
    print(colored(text, 'yellow', attrs=['reverse']), end=' ')
    

def print_error(text, end=' '):
    print(colored(text, 'red', attrs=['reverse']), end=' ')
    

def print_novalid(text, end=' '):
    print(colored(text, 'grey', attrs=['reverse']), end=' ')
    
