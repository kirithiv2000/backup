import json
head="""<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>

.collapsible {
  background-color: #f1f1f1;
  color: #555;
  cursor: pointer;
  padding: 18px;
  /*width: 100;*/
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
  margin:10px;
}

.active, .collapsible:hover {
  /*background-color: #555;*/
}

.content {
  padding: 0 18px;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
  background-color: #f1f1f1;
}
</style>
</head>\n"""

startbody="<body>\n"
buttonstart="<button class=\"collapsible\">"
buttonclose="</button>\n"
contentstart="<div class=\"content\">\n"
divstart="\n\t\t<div >\n"
imgstart="<img src="
imgstyle="style=\"float: left;width: 100px;\"> \n"
divclose=" </div>\n"
h3="\n<h3>"
h3close="</h3>\n"
contentbody=""" <div style="display: flex;">
        <div style="color: blue;width: 200px;">
            <h3>Battery </h3>
            <h3>Camera  </h3>
            <h3>Display </h3>
            <h3>Memory  </h3>
            <h3>Price   </h3>
        </div>
        <div style="width: 20px;color: blue">
            <h3> : </h3>
            <h3> : </h3>
            <h3> : </h3>
            <h3> : </h3>
            <h3> : </h3>
        </div>\n"""


lasthalf="""

<script>
var person = prompt("Please enter your name", "Harry Potter");

</script>

<script>
var coll = document.getElementsByClassName("collapsible");
var i;
for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}
</script>
</body>
</html>
"""
centerstart="\n<center>"
centerclose="</center>\n"
h1="\n<h1>"
h1close="</h1>\n"
pricefloatdiv="\n<div style=\"float: right;\">"
classList=[head,startbody]
with open("flip.html","w") as b:
	for i in classList:
		b.write(i)
def short(a,int2):
	b=[]
	for i in a:
		o=i["Price"].split("₹")
		o=int("".join(o[1].split(",")))
		if o<=int2:
			b.append(i)
	return b

with open("flipkart.json","r") as a:
	a=json.load(a)
	int2=input()
	int2=int(int2)
	a=short(a,int2)
	# a=json.loads(a)
	with open("flip.html","a") as b:
		for i in a:
			 for j in [buttonstart,divstart,imgstart+i["Image Link(url)"]+" "+imgstyle,"<br>"+i["Mobile"].replace(" ","<br>"),h3,i["Price"],h3close,divclose,buttonclose]:
			 	b.write(j)
			 # for k in [contentstart,contentbody,divstart,h3,i["Battery"],h3close,h3,i["Camera"],h3close,h3,i["Display"],h3close,h3,i["Memory"],h3close,h3,i["Price"],h3close,divclose,divclose,divclose]:
			 # 	b.write(k)
			 # break
		b.write(lasthalf)