import json

#json to python (dictonary)
x='{"name":"kowshik","age":24}'

y=json.loads(x)
print(y["name"])

#python(dictionaryt to json)
dic={
    "name":"raja",
    "age":35,
    "city":"chennai"

}
print(dic)
z=json.dumps(dic)
print(z)
