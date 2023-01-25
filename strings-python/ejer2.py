'''Escribir un programa que pregunte el nombre completo del usuario en 
la consola y después muestre por pantalla el nombre completo del usuario 
tres veces, una con todas las letras minúsculas, otra con todas las 
letras mayúsculas y otra solo con la primera letra del nombre y de los 
apellidos en mayúscula. El usuario puede introducir su nombre combinando 
mayúsculas y minúsculas como quiera.'''


def upper_name(names: str, last_names:str):
    """Prints names and surnames in lower, upper and capitalize

    Args:
        names (str): names of the person 
        last_names (str): last names of the person 
    """
    nam = names.split(' ')
    last = last_names.split(' ')
    print(f'{nam[0].upper()} {nam[1].upper()} {last[0].upper()} {last[0].upper()}')
    print(f'{nam[0].lower()} {nam[1].lower()} {last[0].lower()} {last[1].lower()}')
    print(f'{nam[0].capitalize()} {nam[0].capitalize()} {last[0].capitalize()} {last[0].capitalize()}')




def run():
    names = input('Ingrese sus nombres: ')
    last_names = input('Ingrese sus apellidos: ')
    upper_name(names,last_names)

if __name__=='__main__':
    run()