# UNION-FIND

import DoublyLinkedList as DLL


def makeSet(SET, node):  # Crea un nuovo insieme, (una nuova DLL) e la mette nell'insieme di tutte le DLL.
    dll = DLL.DoublyLinkedList()
    dll.insertNode(node)
    SET.add(dll)


def findSet(node):  # Ritorna il puntatore alla DLL che contiene il nodo
    return node.head


def union(dll1, dll2):  # unisce due insiemi, quindi due DLL
    dll1.appendDll(dll2)


# def findListFromHead(SET,nodoTesta):  # ritorna la DLL che ha come rappresentante nodoTesta. # trova la DLL nell'insieme che ha come head "testa".
#     return nodoTesta.head
#     # for lista in SET:
#     #     if nodoTesta == lista.head.data:
#     #         return lista
