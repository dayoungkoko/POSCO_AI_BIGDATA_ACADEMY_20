t= int(input())
for _ in range(t) :
    bracket=input()
    stk=[]
    correct=True
    for b in bracket :
        if b in ['(', '{', '['] :
            stk.append(b)
        elif b in [')', '}', ']']: #스택이 비어있거나, pop된 괄호와 매칭 X인 경우
            if stk == [] :
                correct = False
            elif ord(b)//10 != ord(stk.pop())//10 :
                    correct = False
              
    
    if stk!=[] : #괄호열이 끝났는데, 닫혀지지 않은 괄호가 남은 경우 
        correct= False
    
    if correct == True:
        print('YES')
    else : 
        print('NO')