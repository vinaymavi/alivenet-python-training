from bs4 import BeautifulSoup as soup
import urllib
#from urllib.request import urlopen as uReq

url ='https://www.flipkart.com/search?q=iphone&marketplace=FLIPKART&otracker=start&as-show=on&as=off'
uClient  = urllib.urlopen(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div",{'class','bhgxx2'})
#print len(containers)
#print(soup(prettify)containers[0])

container =  containers[0]
#print container.div.img["alt"]

price = container.findAll("div",{"class":"col col-5-12 _207WAb"})
#price price[0].text
ratings = container.findAll('div',{"class":"niHOFQ"})

filename = "products.csv"
f = open(filename,"w")
headers = "Products_Name,Price,Rating\n"
f.write(headers )

for container in containers:
    products_name = container.div.img["alt"]
    price_container =  contaner.findAll("div",{"class":"col col-5-12 _207WAb"})
    price = price_container[0].text.strip()
    rating_container = container.findAll('div',{"class":"niHOFQ"})
    price = rating_container[0].text

    #string parsing 
    trim_price = "".join(price.split(','))
    rm_rupee = trim_price.split("R")
    add_rs_price = "Rs."+rm_rupee[1]
    splite_price = add_rs_price.split('E')
    final_price = splite_price[0]

    splite_ratig = rating.splite(" ")
    final_rating = splite_ratig[0]

    print products_name.replace(",","|")+","+final_price+","+final_rating+"\n"
    f.write(products_name.replace(",","|")+","+final_price+","+final_rating+"\n")
f.close()