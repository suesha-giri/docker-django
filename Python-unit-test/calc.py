
def extract_numbers(string):
    num = ""
    if type(string) not in [str]:
        raise TypeError("Input must be of type string")

    if len(string)==0:
        raise ValueError("Invalid input")
   
    for chr in string:
        if chr.isdigit():
            
            num = num + chr

    if not num:
        return False
    else:
        return int(num)
    








