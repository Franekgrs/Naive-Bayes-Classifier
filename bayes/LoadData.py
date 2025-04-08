
def LoadData(filnename):
    dataset = []
    with open(filnename, 'r') as file:
        for line in file:
            if not line:
                continue
            dataset.append(line.strip().split(','))
    return dataset

def Prepare(dataset):
    labels = [x[-1] for x in dataset]
    attributes = [x[:-1] for x in dataset]
    return labels,attributes
