import feedparser
import requests
import pprint
from datetime import datetime

# fuel function | today and tomorrow
def get_fuel(product_id, day):
    url = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Suburb=Midvale&Surrounding=no'+str(day)
    data1 = feedparser.parse(url)
    return data1['entries']

# fuel function tomorrow
#def tomorrow_fuel(product_id, day):
#    url = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Suburb=Midvale&Surrounding=no'+str(day)
#    data3 = feedparser.parse(url)
#    return data3['entries']

# product_id
unleaded = 1
premium_unleaded = 2

# day
tod = "today"
tom = "tomorrow"

# variables - today
today_unleaded_prices = get_fuel(unleaded, tod)
today_premium_unleaded_prices = get_fuel(premium_unleaded, tod)

# variables - tomorrow
tomorrow_unleaded_prices = get_fuel(unleaded, tom)
tomorrow_premium_unleaded_prices = get_fuel(premium_unleaded, tom)

# today
# unleaded petroleum 
data1 = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Midvale&Surrounding=no&today')
# premium unleaded petroleum
data2 = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2&Suburb=Midvale&Surrounding=no&today')

# tomorrow
# unleaded petroleum
data3 = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Midvale&Surrounding=no&tomorrow')
# premium unleaded petroleum
data4 = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2&Suburb=Midvale&Surrounding=no&tomorrow')

# -----
# 15/02/2021, 10:31PM
# Search: how to manipulate a rss feed in python
# Info: https://www.tutorialspoint.com/python_text_processing/python_reading_rss_feed.htm
print("--- FuelFinder App Started ---")

# print the number of fuel stations in Midvale
print('There are', len(data1.entries), 'fuel stations in Midvale.')

# To-Do: displays brands on one line
# print the brands of the fuel stations in Midvale
# list3 = []
# for items in data.entries:
#     print(items.brand, '=', items.price + '¢')
# -----

## today
# notify user what the output is
time_date = datetime.now().strftime("%H:%M:%S")
print(" ")
print("Last updated on", time_date + ".")
print(" ")
print("Today's Fuel Prices are:")
newList = []

for i in data1.entries:
    price_str = i['price']
    brand_str = i['brand']
    address_str = i['address']
    location_str = i['location']
    # custom dictionary
    combined_dict = {'when': 'today', 'price': price_str, 'brand': brand_str, 'address': address_str, 'location': location_str}
    newList.append(combined_dict)

# fuel stations 
# output of newList
print(newList)
print(" ")

## tomorrow
# notify user what the output is
print("Note: Correct prices are only available after 2:30pm (AWST)")
print("Tomorrow's Fuel Prices are:")
newList2 = []

for ia in data3.entries:
    price_str = ia['price']
    brand_str = ia['brand']
    address_str = ia['address']
    location_str = ia['location']
    combined_dict = {'when': 'tomorrow', 'price': price_str, 'brand': brand_str, 'address': address_str, 'location': location_str}
    newList2.append(combined_dict)

# fuel stations
# output of newList2
print(newList2)



# PRINT: unleaded, today and tomorrow
#pprint.pprint (
#    get_fuel(unleaded, tod) + get_fuel(unleaded, tom)
#)




# start html
table_content = ''

#for item in combined_dict:
for item in newList2:
    #combined_dict = str(combined_dict) + '<li>' + str(price_str) + '</li>'
    #print('code line 140')
    #print(combined_dict)
    table_row = "<tr><td>(price_str)</td><td>(brand_str)</td><td>(address_str)</td><td>(location_str)</td>"
    table_content = table_content + table_row
    # variables
    price_str = ia['price']
    brand_str = ia['brand']
    address_str = ia['address']
    location_str = ia['location']
    # print
    print(type(item),item,"blah")
    print("-newList2 -")
    print(newList2)

# html table layout
html_content = '''
<html>
    <head>
        <title>Fuel Watch [WA]</title>
    </head>

    <body>
        <h2>Fuel Watch [WA]</h2>
        <table>
            <thead>
                <tr>
                    <th>Price</th>
                    <th>Brand</th>
                    <th>Address</th>
                    <th>Location</th>
                </tr>
            <thead>
            <tbody>
                {0}
            </tbody>
        </table>
    </body>
</html>'''.format(table_content)

# write code to html table file
f = open('D:\\Laptop\\Documents\\PythonWA\\table.html', 'w')
f.write(html_content)
f.close()
