import functools

def delete_sig(lista:list)->list:
    lts = lista.copy()
    for i in range(0,len(lista)):
        print(f'Aprobo {lista[i]} index={i}')
        num = int(input('Con cuanto: '))
        if num > 5 and num <11:
            value = lista[i]
            index = lts.index(value)
            lts.pop(index)
        else:
            continue
    return lts
def run():
   asig = ['Matematica','Ciencia','Programacion','Historia']
   result = delete_sig(lista=asig)
   print(f'{result=}')

if __name__=='__main__':
    run()