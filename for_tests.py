

def check_string(string):
    if (string[0] or string[(len(string) - 1)]) == ' ':
        return False
    if string[0].isupper() == True and string[1:-1].islower() == True:
        return True
    else:
        return False
    if string[- 1] == '.':
        return True
    else:
        return False

check_string('В этом году будет особенно теплое море.')






