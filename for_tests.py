
answer = []
def process_string(string):
    answer = string[1:].lower()
    if 'intern' in answer:
        answer = answer.replace('intern', 'junior')
        print(answer)
    return answer

process_string('IIntern reads a lot of books')
