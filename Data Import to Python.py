# Lab 1: Importing a CSV dataset

# Import pandas library
import pandas as pd

# Read the data 
url = input('Enter the URL: ')
dataframe = pd.read_csv(url, header=None)

# Show the first and last 2 rows
print ('The first 2 rows:') 
dataframe.head(5)
print ('The last 2 rows:') 
dataframe.tail(2)

# Create headers - Firstly, we create a list "headers" that include all column names in order. 
#Then, we use dataframe.columns = headers to replace the headers by the list we created 
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
dataframe.columns = headers

# If there is a missing value in a column that can be dropped
dataframe.dropna(subset=["price"], axis=0)

# Find the name of the columns of the dataframe
print(dataframe.columns)

# To save the csv
dataframe.to_csv("automobile.csv")

# For csv: pd.read_csv() and df.to_csv()
# For json: pd.read_json() and df.to_json()
# For excel: pd.read_excel() and df.to_excel()
# For hdf: pd.read_hdf() and df.to_hdf()
# For sql: pd.read_sql() and df.to_sql()

# to get a statistical summary of each column, such as count, column mean value, column standard deviation, etc. 
# We use the describe method: dataframe.describe()
dataframe.describe()
# describe all the columns in "df" 
dataframe.describe(include = "all")

# select the columns of a data frame by indicating the name of  each column using 
# dataframe[[' column 1 ',column 2', 'column 3']]
dataframe[['length', 'compression-ratio']].describe()

# To get a concise summary of your DataFrame use - dataframe.info
dataframe.info