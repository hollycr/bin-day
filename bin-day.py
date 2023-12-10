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

# TO-DO
# - use automation tools to text the result out
# - use automation tools so the programme runs on a weekly basis