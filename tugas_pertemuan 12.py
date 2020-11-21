import os 
os.system ('cls')

ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',]
ex = ['twen', 'thir', 'fif']

def numbers(x):
    if x < 13 :
        return ones[x]
    elif x < 20 :
        temp = x % 10
        if temp == 3 :
            return ex[1] + 'teen'
        elif temp == 5 :
            return ex[2] + 'teen'
        else :
            return ones[temp] + 'teen'
    elif x < 100 :
        if x // 10 == 2 : 
            return ex[0] + 'ty ' + (numbers(x % 10) if x % 10 != 0 else ' ')
        if x // 10 == 3 :
            return ex[1] + 'ty ' + (numbers(x % 10) if x % 10 != 0 else ' ')
        if x // 10 == 5 :
            return ex[2] + 'ty ' + (numbers(x % 10) if x % 10 != 0 else ' ')
        else :
            return ones[x // 10] + 'ty ' + (numbers(x % 10) if x % 10 != 0 else ' ')
    elif x < 1000 :
        if x // 100 == 1 : 
            return ones[x // 100] + ' hunderd and ' + (numbers(x % 100) if x % 100 != 0 else ' ')
        else : 
            return ones[x // 100] + ' hunderds and ' + (numbers(x % 100) if x % 100 != 0 else ' ')
    elif x < 1000000 :
        if x // 1000 == 1 : 
            return numbers(x // 1000) + ' thousand, ' + (numbers(x % 1000) if x % 1000 != 0 else ' ')
        else : 
            return numbers(x // 1000) + ' thousands, ' + (numbers(x % 1000) if x % 1000 != 0 else ' ')    
    elif x < 1000000000 :
        if x // 1000000 == 1 : 
            return numbers(x // 1000000) + ' million, ' + (numbers(x % 1000000) if x % 1000000 != 0 else ' ')
        else : 
            return numbers(x // 1000000) + ' millions, ' + (numbers(x % 1000000) if x % 1000000 != 0 else ' ')
    else:
        if x // 1000000000 == 1 : 
            return numbers(x // 1000000000) + ' billion, ' + (numbers(x % 1000000000) if x % 1000000000 != 0 else ' ')
        else : 
            return numbers(x // 1000000000) + ' billions, ' + (numbers(x % 1000000000) if x % 1000000000 != 0 else ' ')


while True:
    os.system ('cls')
    try :
        y = int(input('number ? '))
    except :
        print('Yang Anda masukan tidak valid')
        os.system('pause')
    else :
        print(f'{y} = {numbers(y)}')
        os.system('pause')
