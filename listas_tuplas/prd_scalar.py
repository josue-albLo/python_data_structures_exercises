'''
Escribir un programa que almacene los vectores 
(1,2,3) y (-1,0,2) en dos listas y muestre por 
pantalla su producto escalar.
'''

def mult_scalar(v1:list,v2:list)->str:
    if len(v1) == len(v2):
        size = len(v1)
        scalar = 0
        for i in range(0,size):
            print(i)
            scalar += (int(v1[i])*int(v2[i]))
    else:
        scalar = 0
    return f'Multipy scalar is {scalar}'

def run():
    l1 = [1,2,3]
    l2 = [-1,0,2]
    result = mult_scalar(v1=l1,v2=l2)
    print(result)

if __name__=='__main__':
    run()