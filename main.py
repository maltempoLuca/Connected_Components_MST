import connectedComponentsAndMST as ccmst


listOfProbabilityOfArches = [0.2, 0.4, 0.6, 0.8, 1]
numOfMatrices = 12
timesOfCC = []
timesOfMST = []
listsOfMatrices = ccmst.getListsOfSimmetricalWeightedAdjacencyMatrices(listOfProbabilityOfArches, numOfMatrices)    #2^(numOfMatrices)
listsOfWeightsAndIndeces = ccmst.getListsOfWeightsAndIndecesfNonZeroValueSimmetricalMatrices(listsOfMatrices)
listsOfCC = ccmst.getListsofALLConnectedComponents(listsOfMatrices, listsOfWeightsAndIndeces, timesOfCC)
listsOfAllMST_Kruskal = ccmst.getListsOfAllMST_Kruskal(listsOfMatrices, listsOfWeightsAndIndeces, listsOfCC, timesOfMST)

risultatiCCandMST = 'risultatiCCandMST.txt'
ccmst.writeResult(listOfProbabilityOfArches, listsOfCC, timesOfCC, timesOfMST, risultatiCCandMST)