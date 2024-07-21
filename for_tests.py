
int_value = []

def sum_as_ints(list_):
    for element in list_:
        try:
            int_value.append(int(element))
        except ValueError:
            print("Can't be converted to int")
    return sum(int_value)


int("2,2")