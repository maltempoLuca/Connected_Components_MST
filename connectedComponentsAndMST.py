import numpy as np
import random
import time
import unionFind
import matplotlib.pyplot as plt


def getSimmetricalWeightedAdjacencyMatrix(size, probabilityOfArch):
    tmpMatrix = np.zeros((size, size), dtype=int)
    for i in range(1, size):
        for j in range(0, i):
            randomTreshold = random.uniform(0, 1)
            if probabilityOfArch >= randomTreshold:
                randomNumber = random.randint(1, 9)
                tmpMatrix[i, j] = randomNumber
                tmpMatrix[j, i] = randomNumber
    return tmpMatrix


def getListsOfSimmetricalWeightedAdjacencyMatrices(listOfProbabilityOfArches, numOfMatrices):
    listsOfMatrices = []
    for i in range(len(listOfProbabilityOfArches)):
        tmpMatrix = []
        for j in range(numOfMatrices):
            tmpMatrix.append(
                getSimmetricalWeightedAdjacencyMatrix(pow(2, j + 1), listOfProbabilityOfArches[i]))  # 2^(numOfMatrices)
        listsOfMatrices.append(tmpMatrix)
    return listsOfMatrices


def getWeightsAndIndecesOfNonZeroValueSimmetricalMatrix(matrix):
    indiciMatrix = np.nonzero(matrix)
    indiciAndPesi = []
    for i in range(len(indiciMatrix[0])):
        indiceRiga = indiciMatrix[0][i]
        indiceColonna = indiciMatrix[1][i]
        if indiceRiga < indiceColonna:
            peso = matrix[indiceRiga, indiceColonna]
            archi = [indiciMatrix[0][i], indiciMatrix[1][i]]
            tupla = [peso, archi]
            indiciAndPesi.append(tupla)
    return indiciAndPesi


def getListsOfWeightsAndIndecesfNonZeroValueSimmetricalMatrices(listsOfMatrices):
    listsOfWeightsAndIndeces = []
    for i in range(len(listsOfMatrices)):
        tmpIndex = []
        for j in range(len(listsOfMatrices[i])):
            tmpIndex.append(getWeightsAndIndecesOfNonZeroValueSimmetricalMatrix(listsOfMatrices[i][j]))
        listsOfWeightsAndIndeces.append(tmpIndex)
    return listsOfWeightsAndIndeces


def getConnectedComponentsSET(adjacencyMatrix, listOfWeightsAndIndeces, tmpTime):
    startTime = time.time()
    # crea Nodi
    size = adjacencyMatrix.shape[0]
    SETDLL = set()
    listOfNodes = []
    for i in range(size):
        node = unionFind.Node(i)
        listOfNodes.append(node)
        unionFind.makeSet(SETDLL, node)

    # Trova CC
    nUnion = 0
    lengthListOfWeightsAndIndeces = len(listOfWeightsAndIndeces)
    for i in range(lengthListOfWeightsAndIndeces):
        testaLista1 = unionFind.findSet(listOfNodes[listOfWeightsAndIndeces[i][1][0]])
        testaLista2 = unionFind.findSet(listOfNodes[listOfWeightsAndIndeces[i][1][1]])
        if testaLista1 != testaLista2:
            lista1 = unionFind.findListFromHead(SETDLL, testaLista1)
            lista2 = unionFind.findListFromHead(SETDLL, testaLista2)
            if lista1.getSize() > lista2.getSize():
                unionFind.union(lista1, lista2)
                nUnion = nUnion + 1
                SETDLL.remove(lista2)

            else:
                unionFind.union(lista2, lista1)
                nUnion = nUnion + 1
                SETDLL.remove(lista1)

                # stampa nUnion e nCC
    nCC = len(SETDLL)
    endTime = time.time()
    tmpTime.append(endTime - startTime)
    return (nCC, SETDLL)


def printConnectedComponents(connectedComponents):
    print('CC =', connectedComponents[0])
    i = 1
    for dll in connectedComponents[1]:
        print('CC', i, ': ', end='')
        dll.printDLL()
        print()
        i = i + 1


def getListsofALLConnectedComponents(listsOfMatrices, listsOfWeightsAndIndeces, timesOfCC):
    listsOfCC = []
    for i in range(len(listsOfMatrices)):
        tmpCC = []
        tmpTime = []
        for j in range(len(listsOfMatrices[i])):
            tmpCC.append(getConnectedComponentsSET(listsOfMatrices[i][j], listsOfWeightsAndIndeces[i][j], tmpTime))
        listsOfCC.append(tmpCC)
        timesOfCC.append(tmpTime)
    return listsOfCC


def MST_Kruskal(adjacencyMatrix, listOfWeightsAndIndeces, tmpTime):  # ritorna listOfIndeces di UNA CC
    startTime = time.time()
    # lista di indici da ritornare
    newListOfWeightsAndIndeces = []
    # crea Nodi
    size = adjacencyMatrix.shape[0]
    SETDLL = set()
    listOfNodes = []
    for i in range(size):
        node = unionFind.Node(i)
        listOfNodes.append(node)
        unionFind.makeSet(SETDLL, node)

    # ordina Archi SENZA DEEP COPY
    orderedListOfWeightsAndIndeces = listOfWeightsAndIndeces  # deepcopy(listOfWeightsAndIndeces)
    orderedListOfWeightsAndIndeces.sort(key=lambda x: x[0])

    # trova MST
    nUnion = 0
    for i in range(len(orderedListOfWeightsAndIndeces)):
        if nUnion < size:  # MASSIMO V-1 UNION
            indiceRiga = orderedListOfWeightsAndIndeces[i][1][0]
            indiceColonna = orderedListOfWeightsAndIndeces[i][1][1]
            testaLista1 = unionFind.findSet(listOfNodes[indiceRiga])
            testaLista2 = unionFind.findSet(listOfNodes[indiceColonna])
            if testaLista1 != testaLista2:
                lista1 = unionFind.findListFromHead(SETDLL, testaLista1)
                lista2 = unionFind.findListFromHead(SETDLL, testaLista2)
                if lista1.getSize() > lista2.getSize():
                    unionFind.union(lista1, lista2)
                    nUnion = nUnion + 1
                    SETDLL.remove(lista2)
                    peso = adjacencyMatrix[indiceRiga, indiceColonna]
                    archi = [indiceRiga, indiceColonna]
                    tupla = [peso, archi]
                    newListOfWeightsAndIndeces.append(tupla)
                else:
                    unionFind.union(lista2, lista1)
                    nUnion = nUnion + 1
                    SETDLL.remove(lista1)
                    peso = adjacencyMatrix[indiceRiga, indiceColonna]
                    archi = [indiceRiga, indiceColonna]
                    tupla = [peso, archi]
                    newListOfWeightsAndIndeces.append(tupla)

    # stampa tempi
    endTime = time.time()
    tmpTime.append(endTime - startTime)
    return newListOfWeightsAndIndeces


def getListsOfAllMST_Kruskal(listsOfMatrices, listsOfWeightsAndIndeces, listsOfCC, timesOfMST):
    listsOfAllMST_Kruskal = []
    for i in range(len(listsOfMatrices)):
        tmplistsOfAllMST_Kruskal = []
        tmpTime = []
        for j in range(len(listsOfMatrices[i])):
            if listsOfCC[i][j][0] == 1:  # SE HO SOLO UNA COMPONENTE CONNESSA
                tmplistsOfAllMST_Kruskal.append(
                    MST_Kruskal(listsOfMatrices[i][j], listsOfWeightsAndIndeces[i][j], tmpTime))
            else:
                tmplistsOfAllMST_Kruskal.append([])
                tmpTime.append(0.0)
        listsOfAllMST_Kruskal.append(tmplistsOfAllMST_Kruskal)
        timesOfMST.append(tmpTime)
    return listsOfAllMST_Kruskal


def writeResult(listOfProbabilityOfArches, listsOfCC, timesOfCC, timesOfMST, fileOfResult):
    str00 = 'Tempi di esecuzione per la ricerca di componenti connesse e albero di copertura di costo minimo di un grafo non orientato. \n\n'
    File_object = open(fileOfResult, "w")
    File_object.write(str00)
    File_object = open(fileOfResult, "a")
    nNodi = [pow(2, i + 1) for i in range(len(listsOfCC[0]))]
    for i in range(len(listOfProbabilityOfArches)):
        str0 = 'Tempi per ricerca di CC e MST con probabilità di arco tra nodi del grafo = ' + str(
            listOfProbabilityOfArches[i]) + '.\n'
        File_object.write(str0)
        for j in range(len(listsOfCC[i])):
            str1 = 'Numero di Nodi nel grafo = ' + str(nNodi[j]) + ', Numero di CC = ' + str(listsOfCC[i][j][0]) + ', TempoCC = ' + str(
                "{:.5f}".format(timesOfCC[i][j])) + ', TempoMST = ' + str("{:.5f}".format(timesOfMST[i][j])) + '.\n'
            File_object.write(str1)
        File_object.write('\n')
    File_object.close()

    for i in range(len(timesOfCC)):
        # Grafico CC
        strPath = "risultatiGrafici/"
        plt.plot(nNodi, timesOfCC[i])
        str000 = 'Tempo per ricerca di Componenti Connesse, probabilità di arco = ' + str(listOfProbabilityOfArches[i])
        str001 = 'tempiCCProb' + str(listOfProbabilityOfArches[i]) + '.png'
        plt.title(str000)
        plt.xlabel("Nodi nel Grafo")
        plt.ylabel("Tempo in secondi")
        plt.grid()
        plt.savefig(strPath+str001)
        plt.clf()
        plt.cla()
        # Grafico MST
        plt.plot(nNodi, timesOfMST[i])
        str000 = 'Tempo per ricerca di MST, probabilità di arco = ' + str(listOfProbabilityOfArches[i])
        str001 = 'tempiMSTProb' + str(listOfProbabilityOfArches[i]) + '.png'
        plt.title(str000)
        plt.xlabel("Nodi nel Grafo")
        plt.ylabel("Tempo in secondi")
        plt.grid()
        plt.savefig(strPath+str001)
        plt.clf()
        plt.cla()
    print('Finito :D')

