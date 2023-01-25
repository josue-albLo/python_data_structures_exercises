'''
Escribir un programa que almacene el abecedario 
en una lista, elimine de la lista las letras que 
ocupen posiciones múltiplos de 3, y muestre por 
pantalla la lista resultante.
'''
import string as st 

abcedary = st.ascii_lowercase

def delete_letter(lts_abc:list)->list:
    """ This function returns a list with non-zeros elements 

    Args:
        lts_abc (list): value of the variable is a list of alphabetic elements

    Returns:
        list: returns a list with elements that are not multiples of three
    """
    tam = len(lts_abc)
    new_lts = []
    for i in range(0,tam-1):
        if i % 3 == 0:
            continue
        new_lts.append(lts_abc[i])
    return new_lts


def run()->None:
    result = delete_letter(lts_abc=list(abcedary))
    print(f'{result=}')
    print(f'{abcedary=}')

if __name__=='__main__':
    run()