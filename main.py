from algorithm import generator # Importa a função generator do módulo algoritmo
import manager as mg # Importa o módulo gerenciador com o apelido mg
import time # Importa o módulo time


def password_generator():
    list_passwords = []
    password = ''
    while True:
        try:
            size = int(input('Digite o tamanho desejado (min 8): '))

            if size < 8:
                print('O tamanho deve ser igual ou maior que 8.')
                continue

            password_type = int(input('''Escolha um tipo de senha

            [1] Apenas letras
            [2] Numérico
            [3] Alfanumérico
            [4] Letras + caracteres especiais
            [5] Numérico + caracteres especiais
            [6] Alfanumérico + caracteres especiais 

            Digite sua opção: '''))

            if password_type > 6 or password_type < 1:
                print("\nDigite uma opção de 1 a 6 por favor!")
                continue

            password = generator(size, password_type) # Chama a função generator para gerar a senha
            print('\n\nSua senha foi gerada: ', password)

        except ValueError:
            print('\nDigite um valor válido!')

        
        save = input("\nDeseja salvar a senha? (S/N): ")
        save = save.upper()

        if save == 'S':
            list_passwords.append(password) # Adiciona a senha à lista de senhas

        choice = input("\nDeseja gerar uma nova senha? (S/N):")
        choice = choice.upper()

        if choice == 'N':
            if len(list_passwords) >= 1:
                archive = input('Digite um nome para o arquivo de senhas: ')
                archive += '.json'
                mg.save_json(archive, list_passwords) # Salva as senhas no arquivo JSON usando a função salvar_json do módulo mg
            print("\nObrigado por utilizar o gerador de senha\n")
            break

    return list_passwords

def password_manager():
    list_passwords_manual = []
    continue_program = 'S'
    while True:
        try:
            choice = int(input('''Digite uma opção:

            [1] Salvar senha manualmente
            [2] Buscar uma senha
            [3] Sair do gerenciador
            
            Digite sua escolha: '''))

            if choice == 1:
                archive = input('Digite um nome para o arquivo: ') + '.json'
                while continue_program == 'S':
                    password = input('Digite a senha: ')
                    list_passwords_manual.append(password) # Adiciona a senha à lista de senhas manualmente inseridas
                    continue_program = input('Deseja inserir uma nova senha? (S/N): ')
                    continue_program = continue_program.upper()

                mg.save_json(archive, list_passwords_manual) # Salva as senhas no arquivo JSON usando a função salvar_json do módulo mg

            elif choice == 2:
                archive = mg.search_json() # Obtém o arquivo de senhas usando a função buscador_json do módulo mg
                if archive == None:
                    time.sleep(3) # Aguarda 3 segundos antes de retornar ao menu do gerenciador
                    continue # Em caso de não ter arquivos de senha será emitido um aviso e voltará para o menu do gerenciador
                data = mg.read_json(archive)
                print('\nSenhas do arquivo:')
                for passwords in data:
                    print(passwords)
                print()
                time.sleep(3) # Aguarda 3 segundos antes de retornar ao menu do gerenciador

            else:
                print("\nObrigado por utilizar o gerenciador de senha\n")
                break

        except ValueError:
            print('Digite uma opção válida!') 

while True:
    try:
        choice = int(input('''Digite uma opção:

        [1] Gerador de senha
        [2] Gerenciador de senha
        [3] Fechar o programa

        Digite sua escolha: '''))

        if choice == 1:
            list_passwords = password_generator()
 
        elif choice == 2:
            password_manager()
        
        else:
            print('Obrigado por utilizar o programa!')
            break

    except ValueError:
        print('Digite um valor válido!')