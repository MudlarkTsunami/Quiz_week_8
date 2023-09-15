import matplotlib.pyplot as plt
import pandas as pd

#Take the data from the CSV file and place it into a pandas dataframe
CSVDataFrame = pd.read_csv('climate.csv')

#Separate the data
years = CSVDataFrame['Year']
co2 = CSVDataFrame['C02']
temp = CSVDataFrame["Temperature"]


#Pre-existing code
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png")

