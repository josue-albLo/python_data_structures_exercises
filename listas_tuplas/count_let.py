'''
Escribir un programa que pida al usuario una palabra 
y muestre por pantalla el número de veces que contiene 
cada vocal.
'''

def count_letter(paragraph:str,letter:str)->str:
    size = len(paragraph)
    count = 0
    for i in range(0,size-1):
        if paragraph[i]==letter:
            count += 1
    
    return f'letter matches {letter}, is {count}.'

def run():
    paph = 'One, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten'
    let = 'e'
    result = count_letter(paragraph=paph,letter=let)
    count_f = paph.count(let)
    print(result,'--',count_f)

if __name__=='__main__':
    run()