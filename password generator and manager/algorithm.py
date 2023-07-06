import random
import string


def generator(size, password_type):
    password = ''
    special_guarantee = 0

    def letter():
        return random.choice(string.ascii_letters) # Retorna uma letter aleatória maiúscula ou minúscula

    def numeric():
        return str(random.randint(0, 9)) # Retorna um dígito numérico aleatório

    def special_character():
        list_special_character = ['!', '@', '?', '+', '-', '*']
        return random.choice(list_special_character) # Retorna um caractere especial aleatório da lista

    def replace_character(password, index, func):
        character = func() # Obtém um caractere aleatório usando a função func
        new_password = password[:index] + character + password[index + 1:] # Substitui o caractere na posição do índice
        return new_password # Retorna a nova senha após substituição de caracteres

    def add_password_character(func):
        nonlocal password # Permite acessar a variável password definida no escopo externo
        character = func() # Obtém um caractere aleatório usando a função func
        password += character # Adiciona o caractere à password
 
    for _ in range(size):
        # Tipo de senha: Letra
        if password_type == 1:
            add_password_character(letter) # Adiciona uma letra à password

        # Tipo de senha: Numérico
        elif password_type == 2:
            add_password_character(numeric) # Adiciona um dígito numérico à password

        # Tipo de senha: Alfanumérico
        elif password_type == 3:
            decider = random.randint(0, 1)
            if decider == 0:
                add_password_character(letter) # Adiciona uma letra à password
            else:
                add_password_character(numeric) # Adiciona um dígito numérico à password

        # Tipo de senha: Letra + Caractere especial
        elif password_type == 4:
            decider = random.randint(0, 1)
            if decider == 0:
                add_password_character(letter) # Adiciona uma letra à password
            else:
                add_password_character(special_character) # Adiciona um caractere especial à password
                special_guarantee = 1

        # Tipo de senha: Numérico + Caractere especial
        elif password_type == 5:
            decider = random.randint(0, 1)
            if decider == 0:
                add_password_character(numeric) # Adiciona um dígito numérico à password
            else:
                add_password_character(special_character) # Adiciona um caractere especial à password
                special_guarantee = 1

        # Tipo de senha: Alfanumérico + Caractere especial
        elif password_type == 6:
            decider = random.randint(0, 2)
            if decider == 0:
                add_password_character(letter) # Adiciona uma letra à password
            elif decider == 1:
                add_password_character(numeric) # Adiciona um dígito numérico à password
            else:
                add_password_character(special_character) # Adiciona um caractere especial à password
                special_guarantee = 1

    if password_type in [3, 4, 6]:
        if not any(char.isalpha() for char in password):
            index_division = size // 3
            password = replace_character(password, index_division, letter) # Substitui um caractere na senha por uma letra

    if password_type in [3, 5, 6]:
        if not any(char.isdigit() for char in password):
            index_division = size // 2
            password = replace_character(password, index_division, numeric) # Substitui um caractere na senha por um dígito numérico

    if password_type in [4, 5, 6] and special_guarantee == 0:
        index_division = size // 5
        password = replace_character(password, index_division, special_character) # Substitui um caractere na senha por um caractere especial

    return password # Retorna a senha gerada