import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def forwardSelection(data, length):
    current_set = []

    for i in range(1, length):  
        #print(f"On the {i}th level of the search tree")
        highest_value = 0
        best_feature = None 
        for j in range(1, length):  
            if j not in current_set:  
                temp_set = current_set + [j] 
                #print(f"--Considering adding {j} feature")
                acc = knnAlgorithm(data, temp_set) 
                if acc > highest_value:  
                    highest_value = acc
                    best_feature = j
        
        if best_feature is not None: 
            current_set.append(best_feature)
            #print(f"On level {i} added feature {best_feature} to current set")
            print(f"Feature set {best_feature} was best, accuracy is {highest_value}%")
        else:
            #print("No more features to add.")
            break  

        #print(f"Current selected set: {current_set}")

def knnAlgorithm(data, num):
    #print(num)
    X = list(zip(*[data[i] for i in num]))
    y = data[0]  
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) #random_state=42
    knn = KNeighborsClassifier()  
    knn.fit(X_train, y_train)    
    predicted = knn.predict(X_test)
    acc = accuracy_score(y_test, predicted)
    print(f"    Using feature(s) {num} accuracy is {acc*100:.6f}%")
    return acc*100

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
    data = openingFile("CS170_Small_Data__3.txt")
    length = len(data)
    #forwardSelection(data, length)
    temp = knnAlgorithm(data, [2,5,6]) #used for testing
    return 

main()