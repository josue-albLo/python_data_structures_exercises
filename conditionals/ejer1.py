import string
'''
Los alumnos de un curso se han dividido en dos grupos A y B 
de acuerdo al sexo y el nombre. El grupo A esta formado por 
las mujeres con un nombre anterior a la M y los hombres con un 
nombre posterior a la N y el grupo B por el resto. Escribir un 
programa que pregunte al usuario su nombre y sexo, y muestre por 
pantalla el grupo que le corresponde.

'''


def validation(name: str, sex: str):
    letras = list(string.ascii_uppercase)
    lts_mans = ['M', 'N']
    if (name[0:1].upper() in letras):
        if (name[0:1].upper() in lts_mans and  sex.capitalize() == 'Masculino'):
            print(f'Your name is: {name.capitalize()},your sex: {sex}\
                and your group is B')
        else:
            print(f'Your name is: {name.capitalize()},your sex: {sex}\
                and your group is A')
    else:
        print('Enter a valid name ')


def run():
    input_name = input('Enter your name: ')
    input_sex = input('Enter your sex: ')
    validation(name=input_name, sex=input_sex)


if __name__ == '__main__':
    run()
