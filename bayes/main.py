import Bayes
import LoadData





def main():
    train_set = LoadData.LoadData('trainingset.csv')
    test_set = LoadData.LoadData('testset.csv')

    labels, attributes = LoadData.Prepare(train_set)
    apriori = Bayes.apriori(labels)
    unique = Bayes.uniqueAttributes(attributes)
    counted = Bayes.counter(attributes, labels, unique)
    prob = Bayes.probabillity(counted, unique)
    while True:
        print('1. Testuj wszsytkie')
        print('2. Testuj pojedynczy')
        print('3. Testuj dla setu treningowego + dokladnosc')
        print('4. Wyjdz')

        wybor = int(input('Wprowadz nr opcji: '))
        if wybor == 1:
            Bayes.naiveBayes(test_set,LoadData.LoadData('trainingset.csv'))
        elif wybor == 2:
            Bayes.testOne(prob,labels)
        elif wybor == 3:
            Bayes.classifyForTrain(train_set,prob,apriori)
        elif wybor == 4:
            break

if __name__ == "__main__":
    main()



