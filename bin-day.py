import re, requests, datetime
from bs4 import BeautifulSoup

myURL = "https://community.newcastle.gov.uk/my-neighbourhood/your-details?uprn=004510071116&ens=426954%2C565008&address=85+Tynemouth+Road%2CNewcastle+upon+Tyne%2CNE6+1SH&addresses=004510071116%3B426954%2C565008%3B87+Tynemouth+Road%2CNewcastle+upon+Tyne%2CNE6+1SH" # scraping this with BS doesn't work as it's not plain html, and has JavaScript dynamically loading content

newURL = "https://community.newcastle.gov.uk/my-neighbourhood/ajax/getBinsNew.php?uprn=004510071116" # scraping this with BS works because it's plain html - need to see if this still works when the info is updated after this next bin collection?

r = requests.get(newURL)
soup = BeautifulSoup(r.content, 'html5lib')

# .find('div', attrs = {'id', 'binsdiv})
data = soup.find('p', ) 
bigString = data.prettify()

start = bigString.find("Green")
end = bigString.find("Brown")
medString = bigString[start:end]
string = re.sub(r'<.*?>','',medString)
#print(string)

# times
now = datetime.datetime.now()
nextGreenStr = bigString[400:411]
nextGreenDate = datetime.datetime.strptime(nextGreenStr, "%d-%b-%Y")
nextBlueStr = bigString[570:581]
nextBlueDate = datetime.datetime.strptime(nextBlueStr, "%d-%b-%Y")
# print("nextBlueDate",nextBlueDate)
# print("nextGreenDate: ",nextGreenDate)
# print("now: ", now)

if nextGreenDate < nextBlueDate:
    print("It's GREEN bin day on Thursday (so put your bin out on Wednesday)!")
else:
    print("It's BLUE bin day on Thursday (so put your bin out on Wednesday)!")


'''BeautifulSoup is a web scraper tool for static HTML - it will read the HTML from a page, so at the minute i can read all the page info but it says "loading details" when i search for binsdiv
<div id="binsdiv">
 <p>
  Loading details....
 </p>
</div> 
The content I want is being loaded dynamically by JavaScript, so I need a different tool like Selenium to automate browser actions and interact with the dynamic elements on the page. Need to use Selenium to wait for the "loading details" message to disappear or for the details to become visible, indicating that the dynamic content has been loaded. Once the dynamic content is loaded, you can then use BeautifulSoup to parse the HTML and extract the information you need. 
'''

