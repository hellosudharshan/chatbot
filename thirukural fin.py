import numpy as np
import pandas as pd 
import random

df=pd.read_csv("Thirukural.csv")
df2=pd.read_csv("Thirukural With Explanation.csv")

#replacing tabs with spaces to read clearly
df['Verse']=df['Verse'].str.replace('\t',' ')
# I dont see more difference between df and df_exp than an Explanation column.
#Adding the Explanation column to df.
df.loc[:,'Explanation']=df2.loc[:,'Explanation']
df.reset_index()

sv=random.randint(0,1329)
result = df.loc[sv]
print("Kural        :",result["Verse"])
print("Kural Number :",sv)
print("Translation  :",result["Translation"])
print("Meaning      :",result["Explanation"].split("Explanation :")[1])
print("Paal         :",result["Chapter Name"])
print("Adigaram     :",result["Section Name"])
print("1"+result["Verse"])
