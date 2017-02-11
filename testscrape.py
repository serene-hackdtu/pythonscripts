import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","plutonian","test1")
cursor2=db.cursor()
#titlef=alt[1]
#counter=alt[0]
src=requests.get("https://www.thyrocare.com/disorders.html").text
soup=bs(src,"html.parser")
soup1=soup.find_all('div',class_="tabs")[0]       
soup2=soup1.find_all('a') 
condi=0;
#print "0"
for i in soup2:
     try:
         link="https://www.thyrocare.com/disorders.html"+i["href"]
         title2="".join([str(k) for k in i.contents])
	 title2=title2[4:-5]
         print title2
	 print "------------------------------------------------"
     	 src2=requests.get(link).text
     	 soup3=bs(src2,"html.parser")
     	 soup4=soup3.find_all('div',class_="one_half")[0].find_all("li")
     	 for j in soup4:
		if condi == 1:
			condi = 0
			break
     		title1="".join([str(k) for k in j.contents])
                
                sql="""insert into api_Tests(id,title,) values('%ld','%s',)"""%(condi,title,)
     		#cursor2.execute(sql)
        	print title
        	
                condi=condi+1
     except:
	 print "sorry no item"
         continue;
     print "____________________________________________________"
         
#file1.close()
db.commit()
cursor2.close()
#cursor3.close()
db.close()
