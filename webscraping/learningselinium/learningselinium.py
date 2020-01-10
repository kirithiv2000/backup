from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from bs4 import BeautifulSoup               
import time,pprint,json,os,threading,random


def ms(url):

	start=time.time()
	URL = url     
	def gs(URL):
		driver = webdriver.Chrome(ChromeDriverManager().install())
		driver.get(URL)
		page=driver.execute_script("return document.documentElement.outerHTML")
		driver.quit()
		time.sleep(1)
		return page
	page=gs(URL)
	soup=BeautifulSoup(page,"lxml")
	b=soup.find("div",class_="ui cards",id="orig-search-list")
	b=b.findAll("div",class_="content")
	gg={}
	g=[]

	for i in b:
		d={}	
		i=i.find("div",class_="row")
		a=i.find("div",class_="col-m-16 search-result-address grey-text nowrap ln22")
		d["Address"]=(a.text).strip()
		c=i.find("a",class_="result-title hover_feedback zred bold ln24 fontsize0 ")
		d["Shop"]=(c.text).strip()
		d["URL"]=i.find("a")["href"]
		g.append(d)


	def forloop(i):

		page=gs(i["URL"])
		soup=BeautifulSoup(page,"lxml")
		a=soup.find("div",class_="res-info-cuisines clearfix")
		i["Food"]=a.text.strip()
		a=soup.find("div",class_="res-info-timings")
		a=a.find("div",class_="clearfix")
		# print(BeautifulSoup.prettify(a))

		a=a.find("div",class_="medium")
		a=a.text.split("\xa0\xa0")
		i["Opening Time"]=a[0]+","+a[1]

		a=soup.find("span",class_="tooltip_formatted fbold")
		i["Votes"]=a.text.strip()
		a=soup.find("a",class_="item respageMenu-item restaurant-tab-item-jumbo-track ")
		a=a["href"]
		a=gs(a)
		a=BeautifulSoup(a,"lxml")
		a=a.find("div",class_="rate_agg")
		i["Rating"]=(a.text.strip())[:3]
		a=soup.find("span",class_="tel")
		a=a.text.strip()
		if len(a)>13:
			a=a[:13]+","+a[15:]
		i["Phone Number"]=a
		a=soup.find("div",class_="res-info-detail")
		a=a.find("span",class_=False)
		v=""
		for j in a:
			for j in j:

				if j!="(" and j!=")":
					v+=j
		
		i["Cost"]=v.strip()


	thread_list=[]
	c=0
	for thread in g:
		c+=1
		print("page-----"+str(c))

		i=threading.Thread(target=forloop,args=(thread,))
		thread_list.append(i)
		i.start()
		if c%10==0:
			time.sleep(random.randint(60,61))

		
			for threads in thread_list:
				threads.join()

	end=time.time()
	pprint.pprint(g)
	print("Time Taken {}".format(end-start))
	if os.path.exists("vedio.json"):
		with open("vedio.json","r+") as a:
			a=json.load(a)
			a=json.loads(a)
			pprint.pprint(a)

			a=a["zomato"]
			g+=a
			print(len(a),"list")


	
	with open("vedio.json","w+") as a:
		print(len(g))

		gg["zomato"]=g
		gg=json.dumps(gg)
		json.dump(gg,a)


a=input(),input()


