
import json


In_dict={}
Fin_dict={}
f=open('InitialPro.csv',"r")
list1=f.readlines()
Initial=['b','p','m','f','d','t','n','l','g','k','h','j','q','x','zh','ch','sh','r','z','c','s','y','w']

print(Initial[6],Initial[7])
for i in  range (len(Initial)):
  In_dict[Initial[i]]={}
  list2=list1[i+1].split(",")
  for j in range (len(Initial)):
    list3=list2[j].split(",")
    list3=list(float(list3))
    In_dict[Initial[i]][Initial[j]]=list3[0]
First="b"
Second="w"

output = json.dumps(In_dict)

print(output)