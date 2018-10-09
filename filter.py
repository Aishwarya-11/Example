import pandas as pd

df = pd.read_excel('sample.xlsx')
print ("Enter the Team to be retrieved :")
inp = raw_input()
data = df.loc[df["Team"]==inp]
print data
