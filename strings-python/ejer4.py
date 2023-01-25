
'''
Los teléfonos de una empresa tienen el siguiente formato 
prefijo-número-extension donde el prefijo es el código 
del país +34, y la extensión tiene dos dígitos 
(por ejemplo +34-913724710-56). Escribir un programa 
que pregunte por un número de teléfono con este formato 
y muestre por pantalla el número de teléfono sin el prefijo 
y la extensión.
'''

def cellphone_number(cell_num:str)->str:
    """This function returns the cellphone number

    Args:
        cell_num (str): the parameter has to be a prefix-number-extension

    Returns:
        str: returns el number of the phone
    """
    lst_data = cell_num.split('-')
    return f'The number of cellphone is: {lst_data[1]}'

def run():
    number = input('Enter your cellphone number: ')
    result = cellphone_number(number)
    print(f'{result}')

if __name__=='__main__':
    run()