'''
Escribir un programa que pregunte al usuario los 
números ganadores de la lotería primitiva, los 
almacene en una lista y los muestre por pantalla 
ordenados de menor a mayor.
'''
def ordenamiento(loteria:str)->list:
    lts_loteria = list(loteria)
    for i in range(0,len(lts_loteria)):
        for j in range(0,len(lts_loteria)):
            if lts_loteria[i]>lts_loteria[j]:
                lts_loteria[i], lts_loteria[j] = lts_loteria[j], lts_loteria[i]
                # aux = lts_loteria[i]
                # lts_loteria[i] = lts_loteria[j]
                # lts_loteria[j] = aux

            elif lts_loteria[i]==lts_loteria[j]:
                continue
                
    return lts_loteria

def run():
    result1 = ordenamiento('564231054668')
    print(f'Resultado 1 {result1=}')
    


if __name__=='__main__':
    run()