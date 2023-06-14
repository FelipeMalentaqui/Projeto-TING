from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file: str, instance: Queue):
    conteudo = instance
    for existe in conteudo.queue:
        if existe['nome_do_arquivo'] == path_file:
            return

    # print('CONTEUDO: ', conteudo.queue)
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


def remove(instance: Queue):
    # aquivo = txt_importer()
    conteudo = instance
    # print('TAMANHO: ', len(conteudo.queue))
    if conteudo.is_empty():
        print('Não há elementos', file=sys.stdout)

    # if len(conteudo.queue) == 0:
    #     print('Não há elementos')

    # try:
        # print('CONTEUDO: ', conteudo.dequeue())
    # except FileNotFoundError():
    #     print('Não há elementos')
    else:
        data = conteudo.dequeue()['nome_do_arquivo']
        print(f"Arquivo {data} removido com sucesso", file=sys.stdout)


def file_metadata(instance: Queue, position):
    conteudo = instance
    try:
        conteudo.search(position)
        print(conteudo.search(position))
    except IndexError:
        print('Posição inválida', file=sys.stderr)
