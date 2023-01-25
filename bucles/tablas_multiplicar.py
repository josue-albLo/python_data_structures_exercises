'''
Escribir un programa que muestre por pantalla 
la tabla de multiplicar del 1 al 10.
'''
def run():
    endf = 'final'
    for i in range(1,11):
        for j  in range(1,11):
            print(f' {i} * {j} = {i*j}')
        print(f'{endf:-^20}')

if __name__=='__main__':
    run()