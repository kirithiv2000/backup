from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json,os,pprint,time,random,threading
from bs4 import BeautifulSoup
from learningselinium import ms
start=time.time()
URL = 'https://www.zomato.com/ncr/'
def asdf(URL):
	k=webdriver.Chrome(ChromeDriverManager().install())
	k.get(URL)
	i=k.execute_script("return document.documentElement.outerHTML")
	k.quit()
	return i
i=asdf(URL)

soup=BeautifulSoup(i,"lxml")

r=soup.find("div",class_="ui segment row")

t=r.find_all("a",class_="col-l-1by3 col-s-8 pbot0")

vv=[]
for h,i in zip(t,range(len(t))):
	v={}
	hh=h.text.strip()
	hhh=hh.split("   ")
	v["name"]=hhh[0]
	v["no of place"]=hhh[-1].strip("(").strip(")")
	v["url"]=h["href"]
	v["No"]=i+1
	print(i+1,hhh[0],"\n\t---",hhh[-1].strip("(").strip(")"))
	vv.append(v)
	# print()
# pprint.pprint(vv)
a=int(input())
for i in vv:
	if i["No"]==a:
		soup=asdf(i["url"])
		soup=BeautifulSoup(soup,"lxml")
		soup=soup.find("div",class_="col-l-4 col-s-16 ")
		soup=soup.find("a")
		j=asdf(soup["href"])
		h=soup["href"]
		j=BeautifulSoup(j,"lxml")
		j=j.find("div",class_="col-l-4 mtop pagination-number")
		a=j["aria-label"]
		a=a.split(" ")
		thread_list=[]
		for i in range(1,int(a[-2])+1):
			thread=threading.Thread(target=ms,args=(h+"&page"+str(i),))
			print("&page"+str(i))
			thread.start()
			
			time.sleep(60*5)
			# break
			for i in thread_list:
				i.join()
end=time.time()
print("TOTAL TIME TAKEN TO COMPLETE THE PROJECT {}".format(end-start))





