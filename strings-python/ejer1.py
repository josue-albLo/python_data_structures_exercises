

def data_user(name:str,n:int)->None:
    """ imprime n veces name

    Args:
        name (str): cadena de texto o nombre
        n (int): numero que sirve par imprimir la cadena de texto 
    """
    for _ in range(0,n):
        print(name)


def run():
    """ Funcion principal 
    """
    nombre = input('Ingresa tu nombre: ')
    cantidad = int(input('Ingresa el numero de veces a imprimir: '))
    data_user(nombre,cantidad)


if __name__ == '__main__':
    run()
