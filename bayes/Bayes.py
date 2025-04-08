import LoadData


def apriori(labels):
    apriori = {}
    for i in labels:
        if i in apriori:
            apriori[i] += 1
        else:
            apriori[i] = 1
    allElements = len(labels)
    for i in apriori:
        apriori[i] /= allElements
    return apriori


def uniqueAttributes(attributes):
    uniqueAttr = [set() for _ in range(len(attributes[0]))]
    for record in attributes:
        for i, x in enumerate(record):
            uniqueAttr[i].add(x)
    return uniqueAttr

def counter(attributes,labels,uniqueAttributes):
    dictClass = {}
    for label in set(labels):
            dictClass[label] = [{value:0 for value in uniqueAttributes[i]} for i in range(len(uniqueAttributes))]
    print(dictClass)
    for i in range(len(attributes)):
        for j in range(len(attributes[i])):
            attribute = attributes[i][j]
            label = labels[i]
            dictClass[label][j][attribute] += 1
    return dictClass

def probabillity(counted, uniqueAttributes):
    prob_dict = {}
    for label in counted:
        prob_dict[label] = []
        for attr_index in range(len(uniqueAttributes)):
            prob_dict[label].append({})
            total1 = sum(counted[label][attr_index].values())
            total2 = total1 + len(uniqueAttributes[attr_index])
            for attribute in uniqueAttributes[attr_index]:
                count = counted[label][attr_index].get(attribute,0)
                if count == 0:
                    prob_dict[label][attr_index][attribute] = 1 / total2
                else:
                    prob_dict[label][attr_index][attribute] = count / total1
    return prob_dict


def classify(testSet, prob_dict, apriori):
    result = {}
    for label in prob_dict:
        prob = apriori.get(label,0)         # prawdopodobieństwo a priori dla klasy
        for i, attribute in enumerate(testSet):
            atr_prob = prob_dict[label][i].get(attribute,0)
            prob *= atr_prob
        result[label] = prob
    print(result)
    return max(result, key=result.get)  # zwracamy klasę z największym prawdopodobieństwem


def testAll(testSet,prob,labels):
    results = []
    for testLine in testSet:
        probb_label = classify(testLine,prob,apriori(labels))
        results.append((testLine, probb_label))
    return results

def testOne(prob,labels):
    testSet = input('"Wprowadź atrybuty oddzielone przecinkiem (np. slonecznie,nie,srednia,wysoka): ')
    testSetReady = testSet.split(',')
    result = classify(testSetReady,prob,apriori(labels))
    print(f'Czy wychodzić na dwór?: {result}')


def classifyForTrain(data, prob_dict, apriori):
    sum = 0
    for record in data:
        attributes = record[:-1]  # Wszystkie atrybuty z wyjątkiem etykiety
        actual_label = record[-1]  # Rzeczywista etykieta
        predicted_label = classify(attributes, prob_dict, apriori)  # Użycie funkcji classify
        if actual_label == predicted_label:
            sum+=1
        print(f"{record[:-1]} | Rzeczywista: {actual_label} | Przewidywana: {predicted_label}")
    accuracy = sum / len(data)
    print(f"Accuracy: {accuracy}%")

def naiveBayes(testSet,trainSet):
    labels,attributes = LoadData.Prepare(trainSet)

    uniqueAttr = uniqueAttributes(attributes)
    counted = counter(attributes,labels,uniqueAttr)
    prob = probabillity(counted,uniqueAttr)

    results = []
    for testLine in testSet:
        predicted_label = classify(testLine, prob, apriori(labels))
        results.append((testLine, predicted_label))
        print(f"{testLine}, Czy wyjśc na dwór?: {predicted_label}")
    return results
























