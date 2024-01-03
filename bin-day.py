import datetime, re, requests, smtplib
from bs4 import BeautifulSoup

myURL = "https://community.newcastle.gov.uk/my-neighbourhood/your-details?uprn=004510071116&ens=426954%2C565008&address=85+Tynemouth+Road%2CNewcastle+upon+Tyne%2CNE6+1SH&addresses=004510071116%3B426954%2C565008%3B87+Tynemouth+Road%2CNewcastle+upon+Tyne%2CNE6+1SH" # scraping this with BS doesn't work as it's not plain html, and has JavaScript dynamically loading content

newURL = "https://community.newcastle.gov.uk/my-neighbourhood/ajax/getBinsNew.php?uprn=004510071116" # scraping this with BS works because it's plain html - need to see if this still works when the info is updated after this next bin collection?

r = requests.get(newURL)
soup = BeautifulSoup(r.content, 'html5lib')

# .find('div', attrs = {'id', 'binsdiv})
data = soup.find('p', ) 
bigString = data.prettify()

greenStart = bigString.find("Green")
greenEnd = bigString.find("Blue")
greenString = bigString[greenStart:greenEnd]
nextGreenIndex = greenString.find("Next collection : ") + 18
nextGreenStr = greenString[nextGreenIndex:nextGreenIndex+11]

blueStart = bigString.find("Blue")
blueEnd = bigString.find("Brown")
blueString = bigString[blueStart:blueEnd]
nextBlueIndex = blueString.find("Next collection : ") + 18
nextBlueStr = blueString[nextBlueIndex:nextBlueIndex+11]
# readable string = re.sub(r'<.*?>','',greenString)
# print(string)

# times
now = datetime.datetime.now()

nextGreenDate = datetime.datetime.strptime(nextGreenStr, "%d-%b-%Y")
nextBlueDate = datetime.datetime.strptime(nextBlueStr, "%d-%b-%Y")

# print("now: ", now)

if nextGreenDate < nextBlueDate:
    print("It's GREEN bin day on Thursday (so put your bin out on Wednesday)!")
else:
    print("It's BLUE bin day on Thursday (so put your bin out on Wednesday)!")

# TO-DO
# - use automation tools to email the result out using gmail API



# - use automation tools so the programme runs on a weekly basis