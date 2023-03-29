import matplotlib.pyplot as plt
import pandas as pd
import pickle as pkl

cancer = pd.read_pickle("lung")
control = pd.read_pickle("breast")
reference = pd.read_pickle("loadtype")

cancer.plot(color="red")
control.plot(color="blue")
plt.show()

tmp = [0, 0, 0, 0, 0]
referencedt = {}
cancer = list(cancer.values)
control = list(control.values)

for index, rna in enumerate(cancer):
    difference = abs(rna-control[index]) #finds the difference between average expression level in cancer vs control
    if difference > max(tmp):
        tmp.remove(min(tmp))
        tmp.append(difference)
        referencedt[difference] = reference.iloc[[index]]
for diff in tmp:
    print(referencedt[diff], diff)