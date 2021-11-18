import json

f1=open('FinalPro.csv',"r")
line1=f1.readlines()
Final=['i','u','v','a','o','e','ai','ei','ao','ou','an','en','ang','eng','er','ia','io','ie','iao','iu','ian','in','iang','ing','ua','uo','uai','ui','uan','un','uang','ong','ue','uan1','un1','iong']


index1=line1[0][1:-1].split(',')
remain1=line1[1:]
value1=[]

for i in remain1:
    temp=i[:-1].split(',')
    value1.append([float(i) for i in temp])

_json1 = {
  'index': index1,
  'values': value1
}
FinialTable = json.dumps(_json1)
print(FinialTable)