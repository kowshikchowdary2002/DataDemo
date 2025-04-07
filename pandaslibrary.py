import pandas as pd

a=pd.Series([10,20,30,40],index=['a','b','c','d'])

print(a)
#output
#a    10
# b    20
# c    30
# d    40

data={
        "name":["kowshik","madhu","lokesk"],
         "age":[23,34,56],
         "address":["hyd","sam","chennni"]
}

df=pd.DataFrame(data)
print(df)
# out put
#         name  age  address
# 0  kowshik   23      hyd
# 1    madhu   34      sam
# 2   lokesk   56  chennni
print("-----head-------")
print(df.head()) # first 5 rows
print("-----tail-------")
print(df.tail(1))
print("-----describe-------")
print(df.describe())
print("-----age-------")
print(df["age"])
print(df[["name","address"]])

print(df.address[1])
df["age"]+=1
df["address"]="kanupurupalli"
df.rename(columns={"age":"years"},inplace=True)
df.drop("address",axis=1)
print(df)
