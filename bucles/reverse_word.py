'''
Escribir un programa que pida al usuario una palabra 
y luego muestre por pantalla una a una las letras de 
la palabra introducida empezando por la última.
'''

def reverse_word(cadena:str)->None:
    for i in range(len(cadena)-1,-1,-1):
        print(cadena[i], end='-')
        

def run():
    reverse_word('Hola josue')


if __name__=='__main__':
    run()