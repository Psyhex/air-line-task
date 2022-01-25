import requests
from datetime import datetime
from datetime import timedelta
from bs4 import BeautifulSoup
from csv import writer

ten_days_from_now = datetime.now() + timedelta(days=10)
twenty_days_from_now = datetime.now() + timedelta(days=20)

ten_days_from_now_return = datetime.now() + timedelta(days=17)
twenty_days_from_now_return = datetime.now() + timedelta(days=27)


format_date_ten = ten_days_from_now.strftime("%a, %d %b %Y")
format_date_twenty = twenty_days_from_now.strftime("%a, %d %b %Y")

format_date_ten_return = ten_days_from_now_return.strftime("%a, %d %b %Y")
format_date_twenty_return = twenty_days_from_now_return.strftime("%a, %d %b %Y")

payload_ten = {
    'isoneway': 0,
    'currency': 'KES',
    'depairportcode': 'NBO',
    'arrvairportcode': 'MBA',
    'date_from': format_date_ten,
    'date_to': format_date_ten_return,
    'adult_no': 1,
    'children_no': 0,
    'infant_no': 0,
    'searchFlight': '',
    'change_flight': ''
}
payload_twenty = {
    'isoneway': 0,
    'currency': 'KES',
    'depairportcode': 'NBO',
    'arrvairportcode': 'MBA',
    'date_from': format_date_twenty,
    'date_to': format_date_twenty_return,
    'adult_no': 1,
    'children_no': 0,
    'infant_no': 0,
    'searchFlight': '',
    'change_flight': ''
}
url = 'https://www.fly540.com/flights/nairobi-to-mombasa'
r_ten = requests.get(url, params=payload_ten)
r_twenty = requests.get(url, params=payload_twenty)
print(r_ten.url)
print(r_twenty.url)
soup = BeautifulSoup(r_ten.content, 'html.parser')

results = soup.findAll('div', class_="fly5-results")

rez_list_first_full = []
results_first = results[0].findAll("div", class_="fly5-result")
for result_first in results_first:
    airport = result_first.findAll("span", class_="flfrom")
    airportfrom = airport[0].text.strip()[-4:].replace(")", "")
    airportto = airport[1].text[-4:].replace(")", "")

    airtime = result_first.findAll("span", class_="fltime")
    airtimefrom = airtime[0].text.strip()
    airtimeto = airtime[1].text.strip()

    airdate = result_first.findAll("span", class_="fldate")
    airdatefrom = airdate[0].text.replace(",", "").strip()
    airdateto = airdate[1].text.replace(",", "").strip()

    airprice = result_first.find("span", class_="flprice").text.replace(",", "")

    rez_list_first = [airportfrom, airportto, airdatefrom +' '+ airtimefrom, airdateto+' '+ airtimeto, int(airprice)]
    rez_list_first_full.append(rez_list_first)

rez_list_second_full = []
results_second = results[1].findAll("div", class_="fly5-result")
for result_second in results_second:
    airport = result_second.findAll("span", class_="flfrom")
    airportfrom = airport[0].text.strip()[-4:].replace(")", "")
    airportto = airport[1].text[-4:].replace(")", "")

    airtime = result_second.findAll("span", class_="fltime")
    airtimefrom = airtime[0].text.strip()
    airtimeto = airtime[1].text.strip()

    airdate = result_second.findAll("span", class_="fldate")
    airdatefrom = airdate[0].text.replace(",", "").strip()
    airdateto = airdate[1].text.replace(",", "").strip()
    airprice = result_second.find("span", class_="flprice").text.replace(",", "")

    rez_list_second = [airportfrom, airportto, airdatefrom +' '+ airtimefrom, airdateto+' '+ airtimeto, int(airprice)]
    rez_list_second_full.append(rez_list_second)


rez_list_first_full.sort(key = lambda rez_list_first_full: rez_list_first_full[-1], reverse=True)
rez_list_second_full.sort(key = lambda rez_list_second_full: rez_list_second_full[-1], reverse=True)
cheapest_first = rez_list_first_full[-1]
cheapest_second = rez_list_second_full[-1]

final_cheapest_price = cheapest_first[-1]+cheapest_second[-1]

cheapest_first_final = cheapest_first[:-1]
cheapest_second_final = cheapest_second[:-1]

cheapest_ten_day_fare = cheapest_first_final + cheapest_second_final
cheapest_ten_day_fare.append(final_cheapest_price)
#-----------------------------------------------------------------------------------------------------------------------
soup_twenty = BeautifulSoup(r_twenty.content, 'html.parser')

results_twenty = soup_twenty.findAll('div', class_="fly5-results")

rez_list_first_full_twenty = []
results_first_twenty = results_twenty[0].findAll("div", class_="fly5-result")
for result_first_twenty in results_first_twenty:
    airport = result_first_twenty.findAll("span", class_="flfrom")
    airportfrom = airport[0].text.strip()[-4:].replace(")", "")
    airportto = airport[1].text[-4:].replace(")", "")

    airtime = result_first_twenty.findAll("span", class_="fltime")
    airtimefrom = airtime[0].text.strip()
    airtimeto = airtime[1].text.strip()

    airdate = result_first_twenty.findAll("span", class_="fldate")
    airdatefrom = airdate[0].text.replace(",", "").strip()
    airdateto = airdate[1].text.replace(",", "").strip()

    airprice = result_first_twenty.find("span", class_="flprice").text.replace(",", "")

    rez_list_first = [airportfrom, airportto, airdatefrom +' '+ airtimefrom, airdateto+' '+ airtimeto, int(airprice)]
    rez_list_first_full_twenty.append(rez_list_first)

rez_list_second_full_twenty = []
results_second_twenty = results[1].findAll("div", class_="fly5-result")
for result_second_twenty in results_second_twenty:
    airport = result_second_twenty.findAll("span", class_="flfrom")
    airportfrom = airport[0].text.strip()[-4:].replace(")", "")
    airportto = airport[1].text[-4:].replace(")", "")

    airtime = result_second_twenty.findAll("span", class_="fltime")
    airtimefrom = airtime[0].text.strip()
    airtimeto = airtime[1].text.strip()

    airdate = result_second_twenty.findAll("span", class_="fldate")
    airdatefrom = airdate[0].text.replace(",", "").strip()
    airdateto = airdate[1].text.replace(",", "").strip()
    airprice = result_second_twenty.find("span", class_="flprice").text.replace(",", "")

    rez_list_second = [airportfrom, airportto, airdatefrom +' '+ airtimefrom, airdateto+' '+ airtimeto, int(airprice)]
    rez_list_second_full_twenty.append(rez_list_second)


rez_list_first_full_twenty.sort(key = lambda rez_list_first_full_twenty: rez_list_first_full_twenty[-1], reverse=True)
rez_list_second_full_twenty.sort(key = lambda rez_list_second_full_twenty: rez_list_second_full_twenty[-1], reverse=True)
cheapest_first_twenty = rez_list_first_full_twenty[-1]
cheapest_second_twenty = rez_list_second_full_twenty[-1]

final_cheapest_price_twenty = cheapest_first_twenty[-1]+cheapest_second_twenty[-1]

cheapest_first_final_twenty = cheapest_first_twenty[:-1]
cheapest_second_final_twenty = cheapest_second_twenty[:-1]

cheapest_twenty_day_fare = cheapest_first_final_twenty + cheapest_second_final_twenty
cheapest_twenty_day_fare.append(final_cheapest_price_twenty)
#-----------------------------------------------------------------------------------------------------------------------
with open('rez.csv', 'w', newline='', encoding='utf8') as f:
    thewriter = writer(f)
    header = ['outbound_departure_airport', 'outbound_arrival_airport', 'outbound_departure_time', 'outbound_arrival_time',
              'inbound_departure_airport', 'inbound_arrival_airport', 'inbound_departure_time', 'inbound_arrival_time', 'total_price']
    thewriter.writerow(header)
    thewriter.writerow(cheapest_ten_day_fare)
    thewriter.writerow(cheapest_twenty_day_fare)





