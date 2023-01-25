
'''
Escribir un programa que pregunte el correo electrónico del usuario 
en la consola y muestre por pantalla otro correo electrónico con el 
mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

'''
def change_email(email:str, suffix='ceu.es')->str:
    """Email suffix change.

    Args:
        email (str): this parameter must be an email
        suffix (str, optional): you can make email suffix change. Defaults to 'ceu.es'.

    Returns:
        str: returns a new email
    """
    new_email = email.split('@')
    return f'{new_email[0]}@{suffix}'

def run():
    input_email = input('Type your email: ')
    result = change_email(input_email)
    print(result)

if __name__=='__main__':
    run()