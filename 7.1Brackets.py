def solution(S):
    
    if len(S) == 0:
        return 1
    
    mapping = {'{':1, '[':2, '(':3, '}':-1, ']':-2, ')':-3}
    digit = []
    for element in S:
        digit.append(mapping[element])

    check = []
    for number in digit:
        
        if len(check) == 0 and number<0:
            return 0
        elif number<0 and number != -check[-1]:
            return 0
        elif number < 0:
            check.pop()
        elif number > 0 :
            check.append(number)

          
    
    if check == []:
        return 1
    else:
        return 0
