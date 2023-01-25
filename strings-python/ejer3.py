
'''
Escribir un programa que pregunte el nombre del usuario 
en la consola y después de que el usuario lo introduzca 
muestre por pantalla <NOMBRE> tiene <n> letras, donde 
<NOMBRE> es el nombre de usuario en mayúsculas y <n> 
es el número de letras que tienen el nombre.
'''

def data_user(name: str)->str:
    """this function returns a string 

    Args:
        name (str): this parameter is a name or anything word

    Returns:
        str: returns the name with size of the string or name.
    """
    longitude = len(name)
    return f'the name is {name} with longitude ={longitude}'

def run():
    name = input('Enter your name:')
    data = data_user(name)
    print(data)

if __name__=='__main__':
    run()

