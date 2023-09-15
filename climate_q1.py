import matplotlib.pyplot as plt
import sqlite3

#connecting sqlite to the db file
conn = sqlite3.connect('climate.db')
pointer = conn.cursor()

#Getting data from the climatedata table
pointer.execute("SELECT Year, CO2, Temperature FROM ClimateData")
wholeData = pointer.fetchall()

#Separating the data and moving it into the variables
years = [row[0] for row in wholeData]
co2 = [row[1] for row in wholeData]
temp = [row[2] for row in wholeData]

#Given plotting code
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
plt.savefig("co2_temp_1.png") 
