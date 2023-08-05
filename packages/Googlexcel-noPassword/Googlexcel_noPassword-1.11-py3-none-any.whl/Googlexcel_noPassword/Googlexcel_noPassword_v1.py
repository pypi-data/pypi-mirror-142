#Headers relevant to processing the Google XML Spreadsheets and obtaining the sheet names.
import requests
from lxml import html as htmlx  #Approx. 10x better efficiency than Beautiful Soup
#from bs4 import BeautifulSoup #[Scrapped - because inefficent.]

#Headers relevant to Data Analysis.
import pandas as pd
import numpy as np


def fetch_sheetnameslist(url_GoogleSheets):
  '''Returns a list of sheet names
  from the excel workbook
  in the 'Shared' Google Spreadsheet url.
  '''
  
  #Converting html to string for efficient processing.
  html_text = requests.get(url_GoogleSheets).text

  #Converting string back to html and obtaining the sheetnames.
  list_sheetnames = [each.text for each in htmlx.fromstring(html_text).xpath('//div[@class="goog-inline-block docs-sheet-tab-caption"]')]

  #Returning the sheetnames as a list.
  return list_sheetnames


def data_OneSheet(url_GoogleSheets, sheet_name):
  '''Returns one Dataframe
  for the sheetname requested.
  '''

  #Defining the template to remove the prefix to obtain the cosmoID.
  template_GoogleUrl = r'https://docs.google.com/spreadsheets/d/'

  #Manipulating the string to remove the prefix from the template_GoogleUrl from the required url.
  cosmoID = url_GoogleSheets.replace(template_GoogleUrl, '')

  #Splitting the string based on the first '/' from the left to the right and obtaining the first value stored within the generated list using [0].
  cosmoID = cosmoID.split('/',1)[0]

  #The dynamic url to fetch the data within each sheet in the form of csv.
  csv_Sheetpath = f'https://docs.google.com/spreadsheets/d/{cosmoID}/gviz/tq?tqx=out:csv&sheet='

  #Account for spaces in the sheet_name with %20. (Oh yeah, we are going ALL GUNS in, baby!)
  sheet_name = sheet_name.replace(' ', '%20')

  #Generating the url to obtain the csv format of the Spreadsheet sheet with sheet_name.
  g_Sheetpath = csv_Sheetpath + f'{sheet_name}'

  #Creating the dataframe by obtaining the data from each sheet as a csv.
  one_Dataframe = pd.read_csv(g_Sheetpath)

  #Returning the dataframe.
  return one_Dataframe


 
def data_fromAllSheets(url_GoogleSheets):
  '''Return Dictionary with
  'Key' = Sheetname and 'Value' = Dataframe from the 
  excel workbook in the 'Shared' Google Spreadsheet url.
  '''

  #Fetching the list of sheetnames to name the keys.
  list_sheetnames = fetch_sheetnameslist(url_GoogleSheets)

  #Empty dictionary to store 'Key' = Sheetname and 'Value' = Dataframe for the Sheetname.
  dict_Dataframe = {}

  #Defining the template to remove the prefix to obtain the cosmoID.
  template_GoogleUrl = r'https://docs.google.com/spreadsheets/d/'

  #Manipulating the string to remove the prefix from the template_GoogleUrl from the required url.
  cosmoID = url_GoogleSheets.replace(template_GoogleUrl, '')

  #Splitting the string based on the first '/' from the left to the right and obtaining the first value stored within the generated list using [0].
  cosmoID = cosmoID.split('/',1)[0]

  #The dynamic url to fetch the data within each sheet in the form of csv.
  csv_Sheetpath = f'https://docs.google.com/spreadsheets/d/{cosmoID}/gviz/tq?tqx=out:csv&sheet='

  #Looping through the sheets to fetch the data.
  for sheet in list_sheetnames:

    #Account for spaces in the sheet_name with %20. (Oh yeah, we are going ALL GUNS in, baby!)
    sheet_name = sheet.replace(' ', '%20')

    #Generating the url to obtain the csv format of the Spreadsheet sheet with sheet_name.
    g_Sheetpath = csv_Sheetpath + f'{sheet_name}'
    
    #Creating the Key and Value pairs.
    dict_Dataframe[sheet] = pd.read_csv(g_Sheetpath)

  #Returning the output as a dictionary.
  return dict_Dataframe