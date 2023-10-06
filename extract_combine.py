from Plot_AQI import avg_data_2013,avg_data_2014,avg_data_2015,avg_data_2016,avg_data_2017,avg_data_2018
import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup
import os
import csv

def met_data(month, year):
    file_html = open('Data/Html_Data/{}/{}.html'.format(year, month),"rb")
    plain_text = file_html.read()

    tempD = []      # temporarily store the extracted data from HTML tables
    finalD = []     # store the final extracted data

    soup = BeautifulSoup(plain_text, 'lxml')
    for table in soup.find_all('table', {'class': 'medias mensuales numspan'}):
        for tbody in table:     # iterates through all the tbody elements within the table
            for tr in tbody:    # iterates through all tr table row with the tbody
                a = tr.get_text()
                tempD.append(a)

    rows = len(tempD)/15    # one row consists of 15 pcs of data (15 columns)

    for times in range(round(rows)):
        newtempD = []   # use to store a single row of data (15 fields)
        for i in range(15):
            newtempD.append(tempD[0])    # appending the first element of tempD list to newtempD list
            tempD.pop(0)        # remove the first element of the first field in tempD using pop method. This is to enusre that the next iteration of the nested loop processes the next field in 'tempD'
        finalD.append(newtempD)     # After the inner loop had processed all 15 fields in a single row, the newtempD list is appended to finalD list

    length = len(finalD)

    finalD.pop(length - 1)  # remove rows of "Monthly means and totals:"
    finalD.pop(0)           # remove the tile (Day,T,Tm,SLP,H,PP,VV,V,VM...)

    for a in range(len(finalD)):
        finalD[a].pop(6)    # remove column PP
        finalD[a].pop(13)   # remove column FG
        finalD[a].pop(12)   # remove column TS
        finalD[a].pop(11)   # remove column SN
        finalD[a].pop(10)   # remove column RA
        finalD[a].pop(9)    # remove column VG
        finalD[a].pop(0)    # remove column Day
    return finalD

def data_combined(year, cs):
    for a in pd.read_csv('Data/Real-Data/real_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist


if __name__ == "__main__":
    if not os.path.exists("Data/Real-Data"):
        os.makedirs("Data/Real-Data")
    for year in range(2013, 2019):
        final_data = []
        with open('Data/Real-Data/real_' + str(year) + '.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(
                ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        for month in range(1,13):
            temp = met_data(month, year)
            final_data = final_data + temp

        pm = getattr(sys.modules[__name__], 'avg_data_{}'.format(year))()

        if len(pm) == 364:
            pm.insert(364, '-')     # if the length of PM is 364, then insert - at 365th day

        for i in range(len(final_data) - 1):    # excluding the last element in the loop
            # final[i].insert(0, i + 1)
            final_data[i].insert(8, pm[i])

        with open('Data/Real-Data/real_' + str(year) + '.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == "" or elem == "-":
                        flag = 1
                if flag != 1:
                    wr.writerow(row)

    data_2013 = data_combined(2013, 600)
    data_2014 = data_combined(2014, 600)
    data_2015 = data_combined(2015, 600)
    data_2016 = data_combined(2016, 600)
    data_2017 = data_combined(2017, 600)
    data_2018 = data_combined(2018, 600)


    total = data_2013 + data_2014 + data_2015 + data_2016 + data_2017 + data_2018

    with open('Data/Real-Data/Real_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['T', 'TM', 'Tm','SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)

df = pd.read_csv('Data/Real-Data/Real_Combine.csv')
print(df)






