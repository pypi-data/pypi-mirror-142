<h1>Googlexcel_noPassword</h1>   
_____________________________________________  

The First package built to easily obtain the data within an entire shared Google Spreadsheet without passing Google username/ password, credentials.json or OTP authentication.

_____________________________________________

<h2>Instructions.</h2>  

To install the package, perform:  

```python
pip install Googlexcel-noPassword
```
 
How to use the methods:  

<h3>1. To obtain the list of sheetnames:  </h3>

```python
#Importing Library.
import Googlexcel-noPassword as ggx

#url_GoogleSheets = The shared url of Google Spreadsheet document. (Ensure that the privilege is set to 'Anyone with the link'.)
list_ofSheetnames = ggx.fetch_sheetnameslist(url_GoogleSheets)
```

<h3>2. To obtain the dictionary with 'Key' = Sheetname and 'Value' = DataFrame:  </h3>

```python
#Returns a dictionary with all the sheetnames and their respective data as dataframe.
dict_Dataframes = ggx.data_fromAllSheets(url_GoogleSheets)
```

<h3>3. To obtain a single dataframe from one sheet.</h3>

```python
#Returns a dataframe for the data in one sheet.
df_sheetname = ggx.data_OneSheet(url_GoogleSheets, sheet_name)
``` 
_____________________________________________

<h3>Have fun with what is possibly the first library to bypass the credentials.json and the username/ password restrictions to fetch the entire Google Spreadsheet excel document.</h3>