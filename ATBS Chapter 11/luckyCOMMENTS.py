#! python3
# lucky.py - Opens several Google search results

import requests, sys, webbrowser, bs4

print('Googling...')   
res = requests.get('https://google.com/search?q=' + ' '.join(sys.argv[1:]))    
res.raise_for_status()
# This Response Object contains the downloaded HTML file of the google URL,
# which is joined with the keyword from the command line arguments


# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each search result.
linkElems = soup.select('a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
   webbrowser.open('http://google.com' + linkElems[i].get('href'))
