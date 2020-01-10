from bs4 import BeautifulSoup
import requests,pprint,json
def top():
	global data
	
	k=open("data.json","r")
	if k:
		return json.loads(k.read())
	a=requests.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in")
	data=BeautifulSoup(a.text,"lxml")
	data=data.find("tbody",class_="lister-list")

	data=data.find_all("tr")

	number=[]
	name=[]
	year=[]
	rating=[]
	link=[]
	for i in data:
		aaa=i.find("td",class_="titleColumn").get_text().strip()
		num=""
		for j in aaa:
			if j==".":
				break
			else:
				num+=j
		number.append(num)
		aaaa=i.find("td",class_="titleColumn").a.get_text()
		name.append(aaaa)
		aaaaa=i.find("td",class_="titleColumn").span.get_text()
		year_=aaaaa[1:5]
		year.append(year_)
		aaaaaa=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
		rating.append(aaaaaa)	
		aaaaaaa=i.find("td",class_="titleColumn").a["href"]
		link_="https://www.imdb.com"+aaaaaaa
		link.append(link_)

	top_rated_indian_movies=[]
	c={"Position":"","Name":"","Year":"","Url":"","Rating":""}
	for i in range(len(number)):
		c["Position"]=number[i]
		c["Name"]=name[i]
		c["Year"]=year[i]
		c["Url"]=link[i]
		c["Rating"]=rating[i]
		top_rated_indian_movies.append(c.copy())


	with open("data.json","w+") as b:
		json.dump(top_rated_indian_movies,b)
if __name__== "__main__":
	pprint.pprint(top())	
