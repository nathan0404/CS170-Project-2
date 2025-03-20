#import matplotlib.pyplot as plt
from math import sqrt


def forwardSelection(data, length):
    current_set = []

    for i in range(1, length):  
        print(f"On the {i}th level of the search tree")
        featuresAdd = 0 #feature location
        best_feature = 0 #feature acccuracy
        for j in range(1, length):  
            if j not in current_set:  
                print(f"--Considering adding {j} feature")
                acc = accuracy(data, current_set, j) 
                if acc > best_feature:  
                    featuresAdd = j
                    best_feature = acc
        
        print(f"On level {i} added feature {featuresAdd} to current set")
        #print(f"Feature set {best_feature} was best, accuracy is {highest_value}%")
        current_set.append(featuresAdd)

def accuracy(data, current_set, testing):
    length = len(data[0]) #finding length of rows to be searached

    correctlyClassified = 0

    for i in range(length): #searching all rows
        objectClassifier = [] 
        print(i)
        if len(current_set) != 0: #adds all current set to object Classifier
            print("current set is empty")
            for k in range(len(current_set)): #creating object tsting
                objectClassifier.append(current_set[k])
        objectClassifier.append(testing) #adds testing column to object classsfier to tst
        print("object calssifier: ", objectClassifier)
        nearestNeighborDis = float('inf')
        nearestNeighborLoc = float('inf')
        for j in range(length): #going through all data
            print("checking ", i, j)
            if j != i:
                distance = 0
                for k in range(0, len(objectClassifier)): #finding distances with any dimensions
                    distance += (data[objectClassifier[k]][i] - data[objectClassifier[k]][j]) ** 2
                    print(data[objectClassifier[k]][i], data[objectClassifier[k]][j])
                print()
                distance = sqrt(distance)
                if distance < nearestNeighborDis: #checks if new distance is smaller
                    nearestNeighborDis = distance
                    nearestNeighborLoc = data[0][j]
                    print("         better distance found: ", nearestNeighborDis, nearestNeighborLoc)
                print("distance: ", distance, "loc: ", data[0][j])
        print("testing calssification           ", nearestNeighborLoc,  data[0][i])
        if nearestNeighborLoc == data[0][i]:
            print("sucess guess: ", nearestNeighborLoc, data[0][i])
            correctlyClassified+= 1
        else:
            print("not good guess")
        print("cc: ", correctlyClassified, "leng:", length)

    return correctlyClassified / length

def visualize(data):
    x = data[1]
    y = data[2]
    classes = data[0]
    plt.scatter(x, y, c=classes)
    plt.show()

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
    #forwardSelection(data, length)
    #print(data)
    #print(len(data[0]))
    current_set = []
    temp = accuracy(data, current_set, 1)
    print(temp)
    return 

main()