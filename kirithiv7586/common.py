import json,os,pprint

with open('insta.json','r') as file:
	lis=json.loads(file.read())

dic={}
l=[]
for i in lis:
	for j in i['followers']:
		for k in lis:
			v=i['name']+' and '+k['name']
			if i['name']+' and '+k['name'] not in l and k['name']+' and '+i['name'] not in l:
				l.append(i['name']+' and '+k['name'])
			if j in k['followers'] and i!=k and v in l:	
				if v not in dic :
					dic[v]=[j]
				else:
					dic[v].append(j)
pprint.pprint(dic)