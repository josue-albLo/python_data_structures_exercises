'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento 
en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
'''
def split_date(date:str)->str:
    """This function separates the day, month and year

    Args:
        date (str): parameter is your birthday

    Returns:
        str: retuns a string with the date separated into three parts
    """
    data = date.split('/')
    return f'Day:{data[0]}, Month:{data[1]}, Year:{data[2]}'

def run():
    input_date = input('Type your birthday in format day/month/year: ')
    result = split_date(input_date)
    print(result)


if __name__=='__main__':
    run()