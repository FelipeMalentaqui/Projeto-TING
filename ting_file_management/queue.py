from ting_file_management.abstract_queue import AbstractQueue
# from collections import deque


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def is_empty(self):
        return not bool(self.__len__())

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def search(self, index):
        # if self.is_empty():
        #     raise IndexError("Índice Inválido ou Inexistente")

        if self.__len__() > index >= 0:
            return self.queue[index]

        raise IndexError("Índice Inválido ou Inexistente")

    # def __str__(self):
    #     return f'''
    #     tamanho: {self.__len__}
    #     lista: {self.queue}
    #     '''


# listaNome = Queue()
# print('1: ', listaNome.search(0))
# listaNome.enqueue('Felipe')
# print('2: ', listaNome)

# listaNome.enqueue('Bruno')
# print('3: ', listaNome.search)

# listaNome.dequeue()
# print('4: ', listaNome.search)
# print('5', listaNome.is_empty())
