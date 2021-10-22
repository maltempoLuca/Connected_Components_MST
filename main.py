import connectedComponentsAndMST as ccmst


listOfProbabilityOfArches = [0.2, 0.25, 0.30, 0.35, 0.4]
numOfMatrices = 12
timesOfCC = []
timesOfMST = []
listsOfMatrices = ccmst.getListsOfSimmetricalWeightedAdjacencyMatrices(listOfProbabilityOfArches, numOfMatrices)    #2^(numOfMatrices)
listsOfWeightsAndIndeces = ccmst.getListsOfWeightsAndIndecesfNonZeroValueSimmetricalMatrices(listsOfMatrices)
listsOfCC = ccmst.getListsofALLConnectedComponents(listsOfMatrices, listsOfWeightsAndIndeces, timesOfCC)
listsOfAllMST_Kruskal = ccmst.getListsOfAllMST_Kruskal(listsOfMatrices, listsOfWeightsAndIndeces, listsOfCC, timesOfMST)

risultatiCCandMST = 'risultatiTXT/risultatiCCandMST.txt'
ccmst.writeResult(listOfProbabilityOfArches, listsOfCC, timesOfCC, timesOfMST, risultatiCCandMST)