def count_word(cadena:str,busqueda:str)->str:
    lts_palabras = cadena.split(' ')
    contador = 0
    for palabra in lts_palabras:
        if busqueda == palabra:
            contador +=1
    return f'Numero de coincidencias de {busqueda} = {contador}'

def run()->None:
    texto ='''
    hola mundo, quiero contar cuantos hola hay aqui
    para saludar se dice hola , para agradar hola . Hola 
    es una palabra muy utilizada a diario.
        '''
    resultado = count_word(cadena=texto,busqueda='hola')
    print(resultado)

if __name__=='__main__':
    run()