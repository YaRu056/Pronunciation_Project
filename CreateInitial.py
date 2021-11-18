import json

f=open('InitialPro.csv',"r")

line=f.readlines()

Initial=['b','p','m','f','d','t','n','l','g','k','h','j','q','x','zh','ch','sh','r','z','c','s','y','w']

index=line[0][1:-1].split(',')
remain=line[1:]
value=[]


for i in remain:
  temp=i[:-1].split(',')
  value.append([float(i) for i in temp])




_json = {
  'index': index,
  'values': value
}

#print(value)
InitialTable = json.dumps(_json)
print(InitialTable)

