import feedparser
import requests
import pprint
from datetime import datetime

print('--- FuelFinder App Started ---')

# fuel function
def get_fuel(product_id, suburb, day):
    todayList = []
    url = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Suburb='+str(suburb)+'&Surrounding=no'+'&Day='+str(day)+''
    data1 = feedparser.parse(url)
    for value in data1['entries']:
        price = value['price']
        brand = value['brand']
        address = value['address']
        location = value['location']
        sub_list = [price, brand, address, location, day]
        todayList.append(sub_list)
    #print(type(todayList))
    return todayList

# var: product_id
unleaded = 1
premium_unleaded = 2
# var: location
midvale = 'midvale'
# var: day
tod = 'today'
tom = 'tomorrow'

# variables - today
today_unleaded_prices = get_fuel(unleaded, 'midvale', tod)
today_premium_unleaded_prices = get_fuel(premium_unleaded, 'midvale', tod)
## variables - tomorrow
tomorrow_unleaded_prices = get_fuel(unleaded, 'midvale', tom)
tomorrow_premium_unleaded_prices = get_fuel(premium_unleaded, 'midvale', tom)
# variables - combined unleaded - today and tomorrow
comb_unleaded = today_unleaded_prices + tomorrow_unleaded_prices

### Test Area ###
# print('-- TODAY --', today_unleaded_prices)
# print('-- TOMORROW --', tomorrow_unleaded_prices)
# print('-- COMBINED --', comb_unleaded)
# print('-- PRINT comb_unleaded', comb_unleaded)

# print the number of fuel stations in Midvale
print('There are', len(today_unleaded_prices), 'fuel stations in Midvale.')

## time retrieved
time_date = datetime.now().strftime('%H:%M:%S')
print('Last updated on', time_date + '.')

## tomorrow
print("Note: Tomorrow's fuel prices are only available after 2:30pm (AWST).")

def byPrice(item):
    #print(type(item))
    #print('this one here', item)
    return item[0]

sorted_CombUnleaded = sorted(comb_unleaded, key=byPrice)
#print('-- SORTED COMBINED', sorted_CombUnleaded)
pprint.pprint(sorted_CombUnleaded)

# parameters
# Price | Brand | Address | Location | Day
table_content = ''
for y in sorted_CombUnleaded:
    table_content = table_content + '<tr>'
    #print('-- PRINT y', y)
    table_content = table_content + '<td>' + y[0] + '</td>'
    table_content = table_content + '<td>' + y[1] + '</td>'
    table_content = table_content + '<td style="text-align: right; padding-right: 20px;">' + y[2] + '</td>'
    table_content = table_content + '<td>' + y[3] + '</td>'
    table_content = table_content + '<td>' + y[4] + '</td>'
    table_content = table_content + '</tr>'
# print('-- PRINT table_content', table_content)

# creating the HTML table
style = '''
table {
    font-family: "Times New Roman", "Times", serif;
    border: 1px solid #FFFFFF;
    width: 550px;
    height: auto;
    text-align: center;
    border-collapse: collapse;
    left-padding: 5px;
    right-padding: 5px;
}

td {
    border: 1px #00468B solid;
}'''

html_content = f'''
<html>
    <head>
        <style>
            {style}
        </style>
    </head>
    <body>
    <h2>Fuel Watch | WA</h2>
        <table>
                <tr>
                    <th>Price</th>
                    <th>Brand</th>
                    <th>Address</th>
                    <th>Location</th>
                    <th>Day<th>
                </tr>
            <tbody>
                    {table_content}
            </tbody>
        </table>
    </body>
</html>
'''

# write code to html table file
f = open('D:\\Laptop\\Documents\\PythonWA\\table.html', 'w')
f.write(html_content)
f.close()