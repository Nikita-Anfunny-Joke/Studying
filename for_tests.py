

def find_substr(unstr, full_str):
    first_znac = unstr[0]
    last_znac = unstr[len(unstr)-1]
    print(first_znac, last_znac)
    if unstr in full_str:
        return (full_str.index(first_znac), full_str.index(last_znac) +1)
    else:
        pass


find_substr("ма", "маленькая машина")
