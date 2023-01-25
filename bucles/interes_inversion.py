'''
Escribir un programa que pregunte al usuario una cantidad 
a invertir, el interés anual y el número de años, y muestre 
por pantalla el capital obtenido en la inversión cada año que 
dura la inversión
'''

def enter_data(money:float, interest:float, num_years:int)->str:
    """_summary_ This function returns a string with annual investment interest.

    Args:
        money (float): _description_
        interest (float): _description_
        num_years (int): _description_

    Returns:
        str: returns an astring of data
    """
    for i in range(1,num_years+1):
        money += (interest/100) * money
        print(f'Year = {i} amount of interest = {money}')

    return f'Your money returned is ${money}'

def run():
    m = input('Enter your amount of money: ')
    inter = input('Enterthe bank interest: ')
    years = input('Enter the years of investment: ')
    result = enter_data(money=float(m),interest=float(inter),num_years=int(years))

    print(result)

if __name__=='__main__':
    run()