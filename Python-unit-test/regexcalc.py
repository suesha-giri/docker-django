#Using regex library to extract digits

import re

def extract_numbers(string):

    if type(string) not in [str]:
        raise TypeError("Invalid Type")

    if len(string)==0:
        raise ValueError("Invalid Input")

    num=[int(num) for num in re.findall(r'\d+',string)]

    return num