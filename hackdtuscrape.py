import requests
from bs4 import BeautifulSoup as bs
import MySQLdb
db=MySQLdb.connect("localhost","root","plutonian","test1")
cursor2=db.cursor()
#titlef=alt[1]
#counter=alt[0]
src=requests.get("http://growyouthful.com/ailment-select.php").text
soup=bs(src,"html.parser")
soup1=soup.find_all('section',class_="width283")[0]        
soup2=soup1.find_all('a') 
condi=0;
#print "0"
for i in soup2:
     try:
         link=i["href"]
         title2="".join([str(k) for k in i.contents])
	 title2=title2[4:-5]
         print title2
         print "____________________________________________________"
     	 src2=requests.get("http://growyouthful.com/"+link).text
     	 soup3=bs(src2,"html.parser")
     	 soup4=soup3.find_all("article")[0].find_all("p")[1].find_all("a")
     	 for j in soup4:
     		title1="".join([str(k) for k in j.contents])
                title=title1[5:-5]
                
                sql="""insert into api_Remedy(id,title,remedy) values('%ld','%s','%s')"""%(condi,title2,title)
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
