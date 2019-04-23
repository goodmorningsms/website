print("Hello world")
__pacage__ = None
from signalwire.rest import Client as signalwire_client
import private_key as key
txt_service = signalwire_client(key.project_key, key.api_key,
                               signalwire_space_url = key.signalwire_url)
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('GM_Test.json', scope)
client = gspread.authorize(creds)
print(scope)
# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("GM Test").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
# rint(list_of_hashes)


numberlist = []
# Parse Phone Numbers
for i in list_of_hashes:
    numberlist.append(i['Phone Number'])

"""
numberlist = ['9018286567']#, #'9012860576','4043172600']
api ='23LPQNOOOJSFP5T2'

from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key=api)
data = ts.get_batch_stock_quotes(symbols=['TSLA'])
print(data[0][0]['2. price'])
for i in numberlist:
    i = '+1' + i
    print(i)
    message = txt_service.messages.create(
        from_='+19014259501',
        body='Hey Mr. Doug ( ͡° ͜ʖ ͡°)The current TSLA price is: ' + data[0][0]['2. price'] ,
        to=i
    )
    print(message.status)