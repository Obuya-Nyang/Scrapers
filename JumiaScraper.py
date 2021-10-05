'''we're going to create a scraper for jumia.co.ke on android phone sales and store the result in a csv file using python'''

#importing the modules
import requests as ureq
from bs4 import BeautifulSoup as kado

my_url = 'https://www.jumia.co.ke/android-phones/'

page = ureq.get(my_url)

soup = kado(page.text, "html.parser")

containers = soup.findAll("article", {"class":"prd _fb col c-prd"})

#inserting the result into a file in our local machine
filename = "C:/Users/User/Desktop/JumiaPhoneSales.csv"
f = open(filename, "w+")
#column headers
headers = ("ITEM, PRICE(KSH), OLDPRICE(KSH), PERC_DISCOUNT(%), REVIEWS")
f.write(headers + "\n")

#creating a for loop to iterate over all items in containers list
for container in containers:
	try:
		container_info = container.findAll("div", {"class":"info"})

		#getting the item name
		item_name = container_info[0].findAll("h3", {"class":"name"})
		name = item_name[0].text
		#extracting the company brand name from the name
		company_brand = name.split()[0].upper()

		#getting the price
		price = container_info[0].findAll("div", {"class":"prc"})
		pricenow = price[0].text
		oldprice = container_info[0].findAll("div", {"class":"s-prc-w"})
		pricebefore = oldprice[0].div.text
		#exctracting integer values from price
		newprice = int(''.join(filter(lambda x: x.isdigit(), pricenow)))
		olderprice = int(''.join(filter(lambda y: y.isdigit(), pricebefore)))
		#calculating the discount
		discount = olderprice - newprice
		percentage_disc = round(((discount * 100) / olderprice), 2)

		#getting the reviews
		revs = container_info[0].findAll("div", {"class":"rev"})
		reviews = revs[0].text

		print("\nCompany Brand: " + company_brand)
		print("Phone: " + name)
		print("Current Price: " + pricenow)
		print("Price Before: " + pricebefore)
		print("Discount: KSh " + str(discount))
		print("Percentage Discount: {}{}".format(percentage_disc, "%"))
		print("Reviews: " + reviews)
	except IndexError:
		pass
	finally:
		f.write(name.replace(",", "|") + "," + str(newprice) + "," + str(olderprice) + "," + str(round(percentage_disc, 0)) + "," + reviews + "\n")
#closing the file
f.close()




