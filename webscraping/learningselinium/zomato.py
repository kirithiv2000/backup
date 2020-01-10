import json,pprint
with open("vedio.json") as file:
	zomatodictinary=json.load(file)
	zomatodictinary=json.loads(zomatodictinary)
zomatolist=zomatodictinary["zomato"]
print(len(zomatolist))

for zomatoshopdictionary in zomatolist:
	if len(zomatoshopdictionary)!=9:
		zomatolist.pop(zomatolist.index(zomatoshopdictionary))

print(len(zomatolist))
with open("vedio.json") as file:
	zomatodictinary["zomato"]=zomatolist
	zomatodictinarydump=json.dumps(zomatodictinary)
	print(type(zomatodictinarydump))
	pprint.pprint(zomatodictinarydump)
	json.dump(zomatodictinarydump, file)

 