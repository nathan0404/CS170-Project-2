from math import sqrt

def forwardSelection(data, length):
    current_set = []

    max_acc = 0
    max_set = []

    for i in range(1, length):  
        #print(f"On the {i}th level of the search tree")
        featuresAdd = 0 #feature location
        best_feature = 0 #feature acccuracy
        for j in range(1, length):  
            if j not in current_set:  
                acc = accuracy(data, current_set, j, 1) * 100
                temp_set = current_set + [j]  # Simulating the addition of j for printing purposes
                print(f"        Using feature(s) {{{', '.join(map(str, temp_set))}}} accuracy is {acc:.1f}%")
                if acc > best_feature:  
                    featuresAdd = j
                    best_feature = acc
        current_set.append(featuresAdd) 
        print(f"Feature set {{{', '.join(map(str, current_set))}}} was best, accuracy is {best_feature:.1f}%")
        if best_feature > max_acc:
            max_acc = best_feature
            max_set = current_set[:]
    print(f"Finished search!! The best feature subset is {{{', '.join(map(str, max_set))}}}, which has an accuracy of {max_acc}%")
    
def backwardElimination(data, length):
    current_set = []
    for i in range(1, length):
        current_set.append(i)

    print(current_set)

    for i in range(1, length):  
        print(f"On the {i}th level of the search tree")
        featuresAdd = 0 #feature location
        best_feature = 0 #feature acccuracy
        for j in range(1, length):  
            if j in current_set:  
                #print(f"--Considering removing {j} feature")
                acc = accuracy(data, current_set, j, 2) 
                #print(f"        Using feature(s) accuracy is {acc}")
                if acc > best_feature:  
                    featuresAdd = j
                    best_feature = acc
        
        #print(f"On level {i} added feature {featuresAdd} to current set")
        print(f"Feature set {featuresAdd} was best, accuracy is {best_feature}%")
        #print("removing set")
        current_set.remove(featuresAdd)
        print(current_set)

def accuracy(data, current_set, testing, distingisher):
    length = len(data[0]) #finding length of rows to be searached

    correctlyClassified = 0

    for i in range(length): #searching all rows
        objectClassifier = [] 
        #print(i)
        if len(current_set) != 0: #adds all current set to object Classifier
            #print("current set is empty")
            for k in range(len(current_set)): #creating object tsting
                objectClassifier.append(current_set[k])
        if distingisher == 1:
            objectClassifier.append(testing) #adds testing column to object classsfier to test
            #print("added column")
        else:
            objectClassifier.remove(testing)
            #print("removed column")
        #print("object calssifier: ", objectClassifier, " and i value of ", i)
        nearestNeighborDis = float('inf')
        nearestNeighborLoc = float('inf')
        for j in range(length): #going through all data
            #print("checking ", i, j)
            if j != i:
                distance = 0
                for k in range(0, len(objectClassifier)): #finding distances with any dimensions
                    distance += (data[objectClassifier[k]][i] - data[objectClassifier[k]][j]) ** 2
                    #print(data[objectClassifier[k]][i], data[objectClassifier[k]][j])
                #print()
                distance = sqrt(distance)
                if distance < nearestNeighborDis: #checks if new distance is smaller
                    nearestNeighborDis = distance
                    nearestNeighborLoc = data[0][j]
                    #print("         better distance found: ", nearestNeighborDis, nearestNeighborLoc)
                #print("distance: ", distance, "loc: ", data[0][j])
        #print("testing calssification           ", nearestNeighborLoc,  data[0][i])
        if nearestNeighborLoc == data[0][i]:
            #print("sucess guess: ", nearestNeighborLoc, data[0][i])
            correctlyClassified+= 1
        #else:
            #print("not good guess")
        #print("cc: ", correctlyClassified, "leng:", length)

    return correctlyClassified / length

def openingFile(fileName):
    file = open(fileName, "r")
    f=file.readline().split()
    length = len(f)

    features = []
    for i in range(length): #creating arrays
        features.append([])
        features[i].append(float(f[i])) #adding initalf
        #print(features)
    while True:
        f=file.readline().split()
        if not f:
            break
        for i in range(length):
            features[i].append(float(f[i]))

    #for i in range(len(features[0])):
    #    print(features[0][i], features[1][i], features[2][i], features[3][i], features[4][i], features[5][i], features[6][i])

    return features
    

def main():
    data = openingFile("CS170_Small_Data__4.txt") #CS170_Small_Data__3.txt
    length = len(data)
    print(f"This dataset has {length-1} features, with {len(data[0])} instances.")
    print()
    print("Running nearest neightbor, using leaving-one-out evaluation")
    print()
    print("Beginning search.")
    forwardSelection(data, length)
    #backwardElimination(data, length)
    #current_set = []
    #temp = accuracy(data, current_set, 1)
    #print(temp)
    return 

"""
On small dataset 1 the error rate can be 0.95 when using only features 5  4  3
On small dataset 2 the error rate can be 0.958 when using only features 4  1  5
On small dataset 3 the error rate can be 0.954 when using only features 2  5  6
On small dataset 4 the error rate can be 0.918 when using only features 4  6  3
On large dataset 83 the error rate can be 0.95 when using only features 22   2  14"""
main()