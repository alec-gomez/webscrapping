from urllib.request import urlopen, Request 
from bs4 import BeautifulSoup 

url= "https://registrar.web.baylor.edu/exams-grading/spring-2023-final-exam-schedule"
#request in case 404 Forbidden error 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

webpage= urlopen(req).read()

soup= BeautifulSoup(webpage, 'html.parser') 

print(soup.title.text)  

myclasses= ['MW 1:00 p.m.', 'MW 2:30 p.m.'] 

finals_rows= soup.findAll('tr') 

for row in finals_rows: 
    final= row.findAll('td') 
    if final:                          #will make it run if soething is in there. Site had empty list and needed to skip it 
        myclass= final[0].text         #0 for the first row of MW etc 
        if myclass in myclasses: 
            print(f"For class: {myclass} the final is sceduled for {final[1].text} at {final[2].text}") 
            

