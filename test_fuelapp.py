import feedparser
import requests
import pprint
from datetime import datetime

# fuel function | today and tomorrow
def get_fuel(product_id, suburb, day):
    url = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Suburb='+str(suburb)+'&Surrounding=no'+'&Day='+str(day)+''
    data1 = feedparser.parse(url)
    #return data1['entries']
    refinedList = []

    #fuelList = [
    #    {
            # Price | Brand | Address | Location #
    #        'price':    float(info['price']),
    #        'brand':    info['brand'],
    #        'address':  info['address'],
    #        'location': info['location']
    #    }
    #return(fuelList)

    for value in data1['entries']:
        refinedList.append(value['price'])
        refinedList.append(value['brand'])
        refinedList.append(value['address'])
        refinedList.append(value['location'])
    return(refinedList)

# var: product_id
unleaded = 1
premium_unleaded = 2

# var: day
tod = 'today'
tom = 'tomorrow'

midland = 'midland'

# variables - today
today_unleaded_prices = get_fuel(unleaded, 'midvale', tod)
today_premium_unleaded_prices = get_fuel(premium_unleaded, 'midvale', tod)

# variables - tomorrow
tomorrow_unleaded_prices = get_fuel(unleaded, 'midvale', tom)
tomorrow_premium_unleaded_prices = get_fuel(premium_unleaded, 'midvale', tom)

# variables - combined unleaded - today and tomorrow
comb_unleaded = [today_unleaded_prices] + [tomorrow_unleaded_prices]
comb_unleaded = [x for x in comb_unleaded if x]
print('print comb_unleased')
print(comb_unleaded)

# -----
# 15/02/2021, 10:31PM
print('--- FuelFinder App Started ---')

# print the number of fuel stations in Midvale
#print('There are', len(data1.entries), 'fuel stations in Midvale.')

## time retrieved
time_date = datetime.now().strftime('%H:%M:%S')
print('Last updated on', time_date + '.')

## tomorrow
print("Note: Tomorrow's fuel prices are only available after 2:30pm (AWST)")

def byPrice(item):
    return item[0]
sorted_CombUnleaded = sorted(comb_unleaded, key=byPrice)

# parameters
# Price | Brand | Address | Location
table_content = ''
for y in sorted_CombUnleaded:
    table_content = table_content + '<td>' + y[0] + '</td>'
    table_content = table_content + '<td>' + y[1] + '</td>'
    table_content = table_content + '<td>' + y[2] + '</td>'
    table_content = table_content + '<td>' + y[3] + '</td>'
    table_content = table_content + '</tr>'

# html table layout
html_content = f'''
<html>
    <head>
        <title>Fuel Watch [WA]</title>
    </head>

    <body>
        <h2>Fuel Watch | WA</h2>
        <table>
                <tr>
                    <th>Price</th>
                    <th>Brand</th>
                    <th>Address</th>
                    <th>Location</th>
                </tr>
            <tbody>
                <tr>
                    {table_content}
                </tr>
            </tbody>
        </table>
    </body>
</html>'''

# write code to html table file
f = open('D:\\Laptop\\Documents\\PythonWA\\table.html', 'w')
f.write(html_content)
f.close()