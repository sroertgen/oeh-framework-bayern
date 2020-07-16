import pandas as pd
from pathlib import Path

# path to curriculum data
curriculum_xlsx = Path('./data/Lerhplan_all.xlsx')
curriculum_txt = Path('./data/curriculum_all_txt')


# create Node Class
class Node:
    def __init__(
        self,
        _id=None,
        prefLabel=None,
        description=None,
        educationalLevel=None,
        ):
        self.id = _id
        self.prefLabel = prefLabel
        self.description = description
        self.educationalLevel = educationalLevel
        self.children = []

    def __repr__(self):
        return self.prefLabel


# read in xlsx and convert to txt
with open(curriculum_txt, 'w') as file:
    pd.read_excel(curriculum_xlsx).to_string(file, index=False)


# open txt-file and clean up a little
txt = open(curriculum_txt).readlines()
txt_clean = []
for line in txt:
    line = line.replace('\n', '')
    if line == '':
        continue
    txt_clean.append(line)


# get data out of table
# see eaf-schlagwortsystematiken for approach
data = []
