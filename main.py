import connectedComponentsAndMST as ccmst


listOfProbabilityOfArches = [0.01, 0.02, 0.04, 0.08, 1.00]
numOfMatrices = 12
timesOfCC = []
timesOfMST = []
listsOfMatrices = ccmst.getListsOfSimmetricalWeightedAdjacencyMatrices(listOfProbabilityOfArches, numOfMatrices) # Costruisce matrici di adiacenza.
listsOfWeightsAndIndeces = ccmst.getListsOfWeightsAndIndecesfNonZeroValueSimmetricalMatrices(listsOfMatrices) # Matrici di adiacenza in Lista di indici.
listsOfCC = ccmst.getListsofALLConnectedComponents(listsOfMatrices, listsOfWeightsAndIndeces, timesOfCC)
listsOfAllMST_Kruskal = ccmst.getListsOfAllMST_Kruskal(listsOfMatrices, listsOfWeightsAndIndeces, listsOfCC, timesOfMST)

risultatiCCandMST = 'risultatiTXT/risultatiCCandMST.txt'
ccmst.writeResult(listOfProbabilityOfArches, listsOfCC, timesOfCC, timesOfMST, risultatiCCandMST)