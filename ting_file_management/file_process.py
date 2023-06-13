from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file: str, instance: Queue):
    conteudo = instance
    for existe in conteudo.queue:
        if existe['nome_do_arquivo'] == path_file:
            return

    print('CONTEUDO: ', conteudo.queue)
    msg = txt_importer(path_file)
    # print('LINHAS: ', linhas)
    # print('MSG: ', msg)
    formato_arquivo = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(msg),
        "linhas_do_arquivo": msg
        }

    conteudo.enqueue(formato_arquivo)
    print(formato_arquivo)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
