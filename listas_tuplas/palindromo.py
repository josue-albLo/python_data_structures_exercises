'''
Escribir un programa que pida al usuario una palabra 
y muestre por pantalla si es un palíndromo
'''

def valid_palindromo(word:str)->bool:
    word = word.lower().replace(' ','')
    word2 = word[::-1]
    print(word2,word)
    
   
    return  True if word==word2 else False

def valid_pal2(word:str)->bool:
    word = word.lower().replace(' ','')
    word2 = word[::-1]
    valid = True
    size = len(word)
    for i in range(0,size-1):
        if word[i] == word2[i]:
            continue
        else:
            valid = False
    return valid 

def run()->None:
    input_word = input('Enter the word: ')
    result = valid_pal2(word=input_word)
    print(f'{result=}')

if __name__=='__main__':
    run()