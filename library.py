def large(arr): #max() 
    max_ = arr[0]
    for ele in arr:
        if ele > max_:
            max_ = ele
    return max_

def in_dec_num_syst(x, syst): #перевод в десятичную систему счисления
    summa = 0
    x = str(x)
    for i in range(len(x)):
        summa += int(x[i]) * syst ** (len(x) - i - 1)
    return summa

def from_dec_num_syst(x, syst): #перевод из десятичной системы счисления
    s = ''
    while x // syst != 0:
        s += str(x % syst)
        x = x // syst
    s += str(x)
    return s[::-1]

def amount_words(s): #количество слов в строке :)
    k = 0
    s = ' ' + s
    for i in range(len(s) - 1):
        if s[i] == ' ' and s[i + 1] != ' ':
            k += 1
    return k
