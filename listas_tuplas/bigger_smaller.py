'''
Escribir un programa que almacene en una lista los 
siguientes precios, 50, 75, 46, 22, 80, 65, 8, y 
muestre por pantalla el menor y el mayor de los precios
'''
def bigger(list_nums:list)->str:
    max, min = list_nums[0], list_nums[0]
    for item in list_nums:
        if max > item:
            max = item
        elif min < item:
            min = item

    return f'{max}--{min}'

def big(list_nums:list)->str:
    max = 0
    for item in list_nums:
        if max < item:
            max = item
    return f'Max = {max}'



def run():
    list_data = [100, 50, 75, 46,1000, 200, 22, 80, 65, 8,5000,12,9]
    result = bigger(list_nums=list_data)
    result1 = big(list_nums=list_data)
    print(result, result1)

if __name__=='__main__':
    run()