# para rodar, digite no shell  cd Projetos_pessoais  e dps  python organizador_automático_de_arquivos.py
import os
import shutil


try:
    # variaveis globais
    local = input('digite o caminho a ser organizado: ') # C:/Users/p1kek/OneDrive/Documents/Testes
    archive = os.listdir(local)


    # funcao pra fazer uma nova pasta
    def create_folder(new_type):
        path = os.path.join(local, new_type)
        os.makedirs(path)


    #funcao pra definir o arquivo e ver se ele realmente faz sentido
    def file_type_def(file_name):
        # archive_type pega o tipo do arquivo (exemplo: 'txt', 'docs', 'exe', 'zip', etc)
        archive_type = file_name.rsplit('.')[-1]
        # cria o caminho completo
        path = os.path.join(local, archive_type)

        # se nao existe a pasta com o nome do tipo do arquivo
        if not os.path.exists(path):
            create_folder(path)

        # caminho completo do arquivo original e o destino final
        original = os.path.join(local, file_name)
        destination = os.path.join(local, archive_type, file_name)

        # move o arquivo para a pasta correspondente
        if not os.path.exists(destination):
            shutil.move(original, destination)
            print(f"Movido com sucesso: {file_name} -> {archive_type}/")


    # varredura principal da pasta
    for i in archive:
        dir_ = os.path.join(local, i)
        # verifica se e um file e entra no loop e na funcao
        if os.path.isfile(dir_):
            file_type_def(i)
        # se nao, ele e um folder e nn entra
        else:
            print(f'\033[1;41m{i} is a folder (ignored)\033[0m')

except Exception as e:
    print(f"\033[1;31man error occurred \n{e}\033[0m")
