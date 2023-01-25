'''Escribir un programa que pida al usuario un número entero 
y muestre por pantalla si es un número primo o no.'''

def number_verification(number:int):
    lts_valid = []
    for i in range(1,number+1):
        print(i)
        if number%i == 0:
            lts_valid.append(i)
    print(f'{lts_valid=}')
    
    return True if ( len(lts_valid)<3) else False

def run():
    numero = input('Ingresa un numero para ver si es priomo o no: ')
    result = number_verification(number=int(numero))
    if(result):
        print('Es primo')
    else:
        print('No es primo')

if __name__=='__main__':
    run()