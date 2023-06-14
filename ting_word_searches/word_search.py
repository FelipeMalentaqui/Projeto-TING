from ting_file_management.queue import Queue
# from ting_file_management.file_management import txt_importer


def exists_word(word: str, instance: Queue):
    conteudo = instance
    arquivo_nome = ''

    for arquivo in conteudo.queue:
        print('CONTEUDO: ', arquivo['nome_do_arquivo'])
        arquivo_nome = arquivo['nome_do_arquivo']

    print('NOME_ARQUIVO: ', arquivo_nome)
    linha_de_palavras = []

    print('LINHAS: ', linha_de_palavras)

    formato_arquivo = {
        "palavra": '',
        "arquivo": arquivo_nome,
        "ocorrencias": [
            linha_de_palavras
        ]
    }
    print('FORMATO: ', formato_arquivo)


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
