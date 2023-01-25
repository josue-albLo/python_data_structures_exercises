
'''
Escribir un programa que pregunte por consola el precio 
de un producto en euros con dos decimales y muestre por 
pantalla el número de euros y el número de céntimos del 
precio introducido.
'''

def split_price(price:float)->str:
    """This function prints the price divided into two parts

    Args:
        price (float): Price of the product

    Returns:
        str: Returns prices divided into two parts by 
    """
    split_data = f'{price}'.split('.')
    return f'Dollars:{split_data[0]} and cents:{split_data[1]}'


def run():
    try:
        input_price = float(input('Enter price: '))
        result = split_price(input_price)
        print(result)
    except TypeError as err:
        print(err)

if __name__=='__main__':
    run()