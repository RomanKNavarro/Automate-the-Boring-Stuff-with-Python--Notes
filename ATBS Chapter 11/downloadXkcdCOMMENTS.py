#! python3
# downloads image

import requests, os, bs4


url = 'http://xkcd.com'                      # url of the webpage
os.makedirs('xkcd', exist_ok=True)           # ensures that the folder exists, and exit_ok=True ensures not to return an error if it already exists


while not url.endswith('#'):

   
   print('Downloading page %s...' % url)
   res = requests.get(url)             # downloads the webpage until the url ends with '#'
   res.raise_for_status()              # checks if download is successful


   soup = bs4.BeautifulSoup(res.text)  # stores the webpage's html in 'soup'
   comicElem = soup.select('#comic img')            # contains a list of all elements found in 'soup' that have an 'img' element in their attribute
   if comicElem == []:
      print('Could not find comic image.')          # If nothing was matched with the selector, this is printed

      
   else:
      comicUrl = 'http:' + comicElem[0].get('src')  # The image file's link (src), is combined with 'http', since it doesn't have it already
      print(comicElem)
      print('Downloading image %s...' % (comicUrl))  
      res = requests.get(comicUrl)                  # The image file is downloaded
      res.raise_for_status()


      imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb') # creates the files where the downloaded files will be saved
      for chunk in res.iter_content(100000):                                   # The content of the image file is downloaded to imageFile
         imageFile.write(chunk)
      imageFile.close()

      
   prevlink = soup.select('a[rel="prev"]')     # matches the <a> attribute of the previous comic's url, which contains the comic'c number
   url = 'http://xkcd.com' + prevlink[0].get('href')  

print('Done.')




         
         

         













