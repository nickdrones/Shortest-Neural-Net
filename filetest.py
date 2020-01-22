f = open('dataset_A.txt', 'r')
aSet = f.readlines()
f.close()
for i in range(len(aSet)):
    aSet[i] = int(aSet[i].replace('\n',''))
print aSet
