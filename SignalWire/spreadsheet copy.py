
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
#rint(list_of_hashes)

numberlist = []
# Parse Phone Numbers
for i in list_of_hashes:
    numberlist.append(i['Phone Number'])
print(numberlist)

