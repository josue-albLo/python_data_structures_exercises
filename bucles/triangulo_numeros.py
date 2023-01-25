'''
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla un triángulo rectángulo como el de más abajo.
'''

def triangulo_nums(num:int)->None:
    for i in range(1,num+1,2):
        for j in range(i,0,-2):
            print(f'{j}',end=' ')
        print('\n')


def run():
    triangulo_nums(9)

if __name__=='__main__':
    run()