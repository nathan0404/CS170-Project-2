import matplotlib.pyplot as plt
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

def accuracy(data, current_set, j):
    length = len(data[0])

    correctlyClassified = 0

    for i in range(length):
        objectClassifier = []
        print(i)
        for k in range(len(data)): #creating object tsting
            objectClassifier.append(data[k][i])
        print(objectClassifier)
        nearestNeighborDis = float('inf')
        nearestNeighborLoc = float('inf')
        for j in range(length): #going through all data
            if j != i:
                distance = 0
                for k in range(1, len(data)): #finding distances with any dimensions
                    distance += (objectClassifier[k] - data[k][j]) ** 2
                    print(objectClassifier[k], data[k][j])
                print("hi")
                distance = sqrt(distance)
                if distance < nearestNeighborDis: #checks if new distance is smaller
                    nearestNeighborDis = distance
                    nearestNeighborLoc = data[0][j]
                print("distance: ", distance, "loc: ", data[0][j])
        if nearestNeighborLoc == objectClassifier[0]:
            print("sucess guess: ", nearestNeighborLoc, objectClassifier[0])
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
    data = openingFile("TestData.txt") #CS170_Small_Data__3.txt
    length = len(data)
    #forwardSelection(data, length)
    #print(data)
    #print(len(data[0]))
    current_set = []
    temp = accuracy(data, current_set, 0)
    print(temp)
    return 

main()