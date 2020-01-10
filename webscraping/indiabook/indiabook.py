import json,time,os,random,threading,requests,pprint
# from bs4 import BeautifulSoup
# request=requests.get("https://www.indiabookstore.net")       #url
# soup=BeautifulSoup(request.text,"lxml")                      
# # soup1=BeautifulSoup.prettify(soup)
# # print(soup1)
# finddiv=soup.find("ul",class_="navigation")
# # print(finddiv)
# find=finddiv.findAll("li",id="categoryList")
# # print(find)
# # print(len(find))
# catogaryindex=0
# urldict={}
# for li in find:
# 	list3=li.findAll("a")
# 	# print(list3)
# 	maina=li.find("a",class_="noDecoration")
# 	catogaryindex+=1
# 	urldict[catogaryindex]=maina["href"]

# 	print(" ")
# 	print(" "*20,catogaryindex,maina.text[:40])
# 	print(" ")

# 	for index,a in enumerate(list3):
# 		urldict[catogaryindex,index]=a["href"]
# 		a=a.text.strip()
# 		catogary=""
# 		no_of_book=""
# 		flag=False
# 		if "      " not in a:
# 			for name in a:
# 				if "(" == name:
# 					flag=True
# 				elif ")" ==name:
# 					pass
# 				elif flag:
# 					no_of_book+=name
# 				else:
# 					catogary+=name
# 			if len(no_of_book)==1 and ("0" in no_of_book):
# 				print(index," "*(2-len(str(index))),catogary," "*(35-len(catogary)),no_of_book," "*(7-len(no_of_book)),"Book"," |")
# 			elif len(no_of_book)==0:
# 				print(" "*20,"No catogary available")
# 				print(" ")
# 			else:
# 				print(index," "*(2-len(str(index))),catogary," "*(35-len(catogary)),no_of_book," "*(7-len(no_of_book)),"Books","|")
# 			print("-"*57)
	
# # pprint.pprint(urldict)
# tuple1=int(input("enter the number of your topic                                                                                     : "))
# tuple2=int(input("enter the number of your catogary (if there is no catogary press 0 if you press any wrong input it will show error): "))

# url=urldict.get((tuple1,tuple2))
# list1=[]
# if url:
	
# 	request=requests.get("https://www.indiabookstore.net"+url)
# 	soup=BeautifulSoup(request.text,"lxml")                      
# 	soup1=BeautifulSoup.prettify(soup)
# 	soup=soup.findAll("div",class_="col-md-3 col-xs-6 text-center ")
# 	for i in soup:
# 		div={}
# 		soup=i.find("a",class_="bookPageLink")
# 		div["URL"]="https://www.indiabookstore.net"+soup["href"]
# 		div["IMAGE URL"]=soup.find("img")["src"]
# 		div["NAME"]=soup.find("img")["title"].strip()
# 		x=soup.find("div",class_="userStoreSpecificRatingBox ratingPositive")
# 		if x!=None:
# 			div["RATING"]=x.text.strip()
# 		else:
# 			div["RATING"]=None
# 		list1.append(div)


# for i in list1:

# 	request=requests.get(i["URL"])
# 	soup=BeautifulSoup(request.text,"lxml")                      
# 	soup1=BeautifulSoup.prettify(soup)
# 	# print(soup1)
# 	x=soup.find("div",itemprop="author")
# 	if x!=None:
# 		i["author"]=soup.find("div",itemprop="author").text[9:]
# 	else:
# 		i["author"]=None
# 	SOME=soup.findAll("a",class_="bookPageBuyLink",target="_blank")
# 	i["RATE"]=""

# 	for rate in SOME:
# 		rate=rate.text
# 		rate+=", "
# 		i["RATE"]=i["RATE"]+rate
# 	# break
# 	if i["RATE"]=="":
# 		i["RATE"]="Not mentioned in website,"
# 	o=soup.find("td",itemprop="numberOfPages")
# 	if o!=None:
# 		i["No of pages "]=o.text
# 	else:
# 		i["No of pages "]=None
# 	o=soup.find("td",itemprop="inLanguage")
# 	if o!=None:
# 		i["Language"]=o.text
# 	else:
# 		i["Language"]=None

# for i in list1:
# 	print(" ")
# 	print("NAME          : ",i["NAME"],",")
# 	if i["author"]!=None:
# 		print("AUTHOR        : ",i["author"],",")
# 	print("RATE          : ",i["RATE"])
# 	if i["RATING"]!=None:
# 		print("RATING        : ",i["RATING"],",")
# 	if i["No of pages "]!=None:
# 		print("No of pages   : ",i["No of pages "],",")
# 	if i["Language"]!=None:
# 		print("LANGUAGE      : ",i["Language"],",")
# 	print("URL           : ",i["URL"],",")
# 	print("IMAGE URL     : ",i["IMAGE URL"],",")
# 	print("_"*80)
# 	# break

from bs4 import BeautifulSoup
count=1
dic={}
url=requests.get("https://www.indiabookstore.net/categories").text
soup=BeautifulSoup(url,"html.parser")
main_div=soup.find("div",id="leftNavContainer")
allatags=soup.find_all("a",class_="noDecoration")
for a in allatags:
    loop=2
    i=1
    print ("\n-----------------------------------%s--------------------------------------\n"%a["href"].split("/")[-1])
    while i<loop:
        link=("https://www.indiabookstore.net"+a["href"]+"?page=%s"%str(i))
        url2=requests.get(link).text
        soup2=BeautifulSoup(url2,"html.parser")
        lookcode=soup2.find("ul",class_="pagination")

        loop=int(lookcode.text.split("\n")[-3])
        i+=1
        books=soup2.find_all("div",class_="col-md-3 col-xs-6 text-center ")
        
        for j in books:
            bookname=(j.find("div",class_="truncateName").text)
            print (str(count)+" Name: "+bookname.strip("\n").strip())
            dic["Name"]=bookname
            dic["SN."]=count
            count+=1