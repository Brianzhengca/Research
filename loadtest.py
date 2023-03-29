import pickle as pkl
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("process_data_downloaded.txt", sep="\t")
seriesdt = pkl.load(open("seriesdt.pkl", "rb"))
#df = df.T
#print(df.columns)
df['ID_REF'].to_pickle("loadtype")
for type in seriesdt.keys():
    patients = seriesdt[type]
    tmp = []
    for patient in patients:
        tmp.append(df[patient].values.flatten().tolist())
    tmp = pd.DataFrame(tmp)
    tmp = tmp.mean(axis=0)
    tmp.to_pickle(str(type))
    tmp.plot()