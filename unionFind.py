class Node:

    def __init__(self, data):
        self.nextNode = None  # reference to head node in DLL
        self.head = None  # reference to first node in DLL
        self.data = data  # data == (vertice)


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertNode(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.head = self.head
        else:
            self.tail.nextNode = newNode
            self.tail = newNode
            newNode.head = self.head
        self.size = self.size + 1

    def printDLL(self):
        if self.head is not None:
            tmpNode = self.head
            print(tmpNode.data, end='')
            while tmpNode.nextNode is not None:
                tmpNode = tmpNode.nextNode
                print(',', tmpNode.data, end='')
        print()

    def getSize(self):
        return self.size

    def appendDll(self, dll):
        self.tail.nextNode = dll.head
        self.tail = dll.tail
        # aggiusta le testa della lista da appendere
        tmpNode = dll.head
        tmpNode.head = self.head
        while tmpNode.nextNode is not None:
            tmpNode = tmpNode.nextNode
            tmpNode.head = self.head
        self.size = self.size + dll.getSize()


# UNION-FIND

def makeSet(SET, node):
    dll = DoublyLinkedList()
    dll.insertNode(node)
    SET.add(dll)


def findSet(node):
    return node.head.data


def union(dll1, dll2):
    dll1.appendDll(dll2)


def findListFromHead(SET, testa):
    for lista in SET:
        if testa == lista.head.data:
            return lista
