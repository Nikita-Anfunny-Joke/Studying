

test1 = ['e',6,8,'A','>','^','S','$','R','C',6,'+','#',9,'/',1,'T','!','%','K',7,'-','O','*','<',2,'h',4,'g']

print(len(test1))
answer = []

def fifth_element(full_list: list) -> list:
    for n in range(len(full_list) // 5):
        print(n)
        answer.append(full_list[(len(full_list)) - (5 * (n + 1))])
        print(answer)
    return answer




fifth_element(test1)