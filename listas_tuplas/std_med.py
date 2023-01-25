'''
Escribir un programa que pregunte por una muestra de números,
 separados por comas, los guarde en una lista y muestre por 
 pantalla su media y desviación típi
'''
def std_ex(dataset:list)->int:
    n_obser = len(dataset)
    med_arit = med_ex(data=dataset)
    sum = 0
    for x in dataset:
        print(f'{x}-{med_arit}^2')
        sum += (x-med_arit)**2
    print(f'{sum}/{n_obser}={sum/n_obser}')
    return (sum/n_obser)**0.5

def med_ex(data:list)->int:
    sum = 0
    
    for i in data:
        sum +=i
    return sum/len(data)

def run():
    data_obser = [1,2,3,4,5]
    result_std = std_ex(dataset=data_obser)
    result_med = med_ex(data=data_obser)
    print(f'{result_std=:.3f}\n{result_med=}')

if __name__=='__main__':
    run()