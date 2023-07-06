import json
import glob


def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as archive:
        json.dump(data, archive, ensure_ascii=False, indent=2)
        # Salva os dados em formato JSON no arquivo especificado
        # A opção ensure_ascii=False garante que os caracteres não ASCII sejam salvos corretamente
        # O parâmetro indent=2 define a indentação de 2 espaços para melhor legibilidade



def search_json():
    json_file_list = glob.glob('*.json')

    if json_file_list:
        print('Selecione um archive:\n')
        for index, archive in enumerate(json_file_list, start=1):
            print(f'[{index}] {archive}')
            # Enumera os arquivos encontrados e exibe-os na tela com um índice correspondente

        while True:
            try:
                choice = int(input('choice um archive de senhas: '))
                if choice < 1:
                    print('Digite um valor maior ou igual a 1')
                else:
                    return json_file_list[choice - 1] # Retorna o arquivo escolhido com base no índice fornecido
                
            except ValueError:
                print('\nDigite um valor válido!\n') # Lida com exceção caso um valor inválido seja inserido
    else:
        print('Nenhum archive de senhas encontrado.')
        return None # Retorna None se nenhum arquivo de senha for encontrado


def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as archive:
        data = json.load(archive) # Carrega os dados do arquivo JSON
    return data # Retorna os dados carregados do arquivo JSON
