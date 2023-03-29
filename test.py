import GEOparse
import pickle as pkl
indexfile = open("meta_index.txt", 'r')
seriesdt = { #dictionary storing the id of all the cancer types
    "bone and soft tissue sarcomas":[],
    "intraparenchymal brain tumors":[],
    "benign disease in the breast":[],
    "extraparenchymal brain tumor":[],
    "benign disease in the ovary":[],
    "benign disease in the prostate":[],
    "benign disease in the bone and soft tissue":[],
    "no cancer":[],
    "breast":[],
    "bladder":[],
    "biliary tract":[],
    "colorectal":[],
    "esophageal squamous cell":[],
    "lung":[],
    "gastric":[],
    "hepatocellular":[],
    "pancreatic":[],
    "prostate":[],
    "ovarian":[],
}

for line in indexfile.readlines():
    try:
        index = line.split()[-1]
        gse = GEOparse.get_GEO(geo=index)
        for cancer in seriesdt.keys():
            if cancer in gse.metadata["characteristics_ch1"][0]:
                seriesdt[cancer].append(gse.metadata['title'])
                break
        continue
    except Exception as e:
        print(e)
        pass

pkl.dump(seriesdt, open("seriesdt.pkl", "wb"))




