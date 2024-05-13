import pandas as pd

column_name = ['title20109271','genre20109271','type20109271','priceex20109271','pricein20109271','tax20109271','ava20109271','review20109271']

inFile = 'csvdataexamsrc20109271.csv'
df = pd.read_csv(inFile,names = column_name)

df = df[['genre20109271','priceex20109271','ava20109271']]

df['priceex20109271'] = df['priceex20109271'].str.split("£")
df['priceex20109271'] = [float(x[1]) for x in df['priceex20109271']]

df['ava20109271'] = df['ava20109271'].str.split("(")
df['ava20109271'] = [int(x[1].split(" ")[0]) for x in df['ava20109271']]

outFile = 'etldata20109271.csv'
df.to_csv(outFile, header=False, index=False)

print("Filename input: "+ inFile)
print(df.info())
print(df.describe(include = 'all'))
print("Filename output: "+ outFile)
