'''
Escribir un programa que almacene la cadena de caracteres 
contraseña en una variable, pregunte al usuario por la 
contraseña hasta que introduzca la contraseña correcta.
'''

def login(user:str,password:str)->None:
    password_again = input('Ingresa nuevamente la contrasenia: ')
    validation = password_again != password
    while validation:
        password_again = input('Ingresa nuevamente la contrasenia: ')
        validation = password_again != password
    else:
        print('Successfuly')

def run():
    user = input('Ingresa tu usuario: ')
    passw = input('Ingresa tu constrasenia: ')
    login(user=user, password=passw)

if __name__=='__main__':
    run()