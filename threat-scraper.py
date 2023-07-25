import requests 
from bs4 import BeautifulSoup

# URL of threat feed to scrape  
url = 'https://urlhaus.abuse.ch/feeds/dga/'

# Fetch page content  
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find table with indicator data
table = soup.find('table', {'class':'table'}) 

# Iterate through rows 
for row in table.find_all('tr')[1:]:
  
  # Get columns 
  cols = row.find_all('td')
  
  # Extract indicator  
  indicator = cols[1].text.strip() 
  
  # Print indicator
  print(indicator)
