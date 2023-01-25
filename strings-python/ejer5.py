
'''
Escribir un programa que pida al usuario que introduzca 
una frase en la consola y una vocal, y después muestre por 
pantalla la misma frase pero con la vocal introducida en mayúscula.
'''

def sustitution(word: str, letter:str):
    """The fucntion returns a word with a single uppercase letter

    Args:
        word (str): this parameter is a sentence or letters
        letter (str):the parameter kind vowel

    Returns:
        _type_: returns a sentence with letter uppercase 
    """
    return word.replace(letter,letter.upper())


def run():
    word = input('Enter a word: ')
    lyric = input('Enter a lyric: ')
    result = sustitution(word, lyric)
    print(f'New word:\n{result}')

if __name__=='__main__':
    run()