'''
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla un triángulo rectángulo como el de más 
abajo, de altura el número introducido.
'''
def triangulo_caracteres(num:int,caracter:str):
    for i in range(0,num+1):
        print(i*f'{caracter}')

def triangulo_caracteres2(num:int, caracter:str)->None:
    for i in range(1,num):
        for i in range(1,i):
            print(f'{caracter}', end=' ')
        print('\n')

def run():
    num = input('Ingresa el numero de veces: ')
    character = input('Ingresa el caracter: ')
    triangulo_caracteres2(num=int(num),caracter=character)


if __name__=='__main__':
    run()