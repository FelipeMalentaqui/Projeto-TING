from ting_file_management.queue import Queue
# from ting_file_management.file_management import txt_importer


def exists_word(word: str, instance: Queue):
    conteudo = instance
    arquivos = ''
    text_palvra = ''
    linha_de_palavras = []

    for arquivo in conteudo.queue:
        arquivos = arquivo['nome_do_arquivo']
        text_palvra = arquivo['linhas_do_arquivo']

    # print('NOME_ARQUIVO: ', arquivos)
    # print('TEXTO_FORA: ', texto_palvra)

    # A MINHA LINHA É O MEU INDEX

    for linha in text_palvra:
        if word.lower() in linha.lower():
            linha_de_palavras.append({"linha": (text_palvra.index(linha) + 1)})

    formato_arquivo = [{
        "palavra": word,
        "arquivo": arquivos,
        "ocorrencias": linha_de_palavras
    }]
    return formato_arquivo if linha_de_palavras else list()


def search_by_word(word, instance):
    return list()
