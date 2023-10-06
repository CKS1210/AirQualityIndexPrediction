import pandas as pd
import matplotlib.pyplot as plt

def avg_data_2013():
    i365days = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2013.csv', chunksize=24):  # chunksize means how many records to take, 24hours so is 24 records
        add_var = 0     # used to accumulate the sum of PM2.5 values for the 24 hours in each chunk
        avg = 0.0       # intended to store the average PM2.5 value for that chunk
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i       # if the value is a float or an integer, then add tgt
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)     # if the value is in diff data format (string) then convert to float
                    add_var = add_var + temp
        avg = add_var /24
        i365days = i365days + 1

        average.append(avg)
    return average

def avg_data_2014():
    i364days = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2014.csv', chunksize=24):  # chunksize means how many records to take, 24hours so is 24 records
        add_var = 0     # used to accumulate the sum of PM2.5 values for the 24 hours in each chunk
        avg = 0.0       # intended to store the average PM2.5 value for that chunk
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i       # if the value is a float or an integer, then add tgt
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)     # if the value is in diff data format (string) then convert to float
                    add_var = add_var + temp
        avg = add_var /24
        i364days = i364days + 1

        average.append(avg)
    return average

def avg_data_2015():
    i365days = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2015.csv', chunksize=24):  # chunksize means how many records to take, 24hours so is 24 records
        add_var = 0     # used to accumulate the sum of PM2.5 values for the 24 hours in each chunk
        avg = 0.0       # intended to store the average PM2.5 value for that chunk
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i       # if the value is a float or an integer, then add tgt
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)     # if the value is in diff data format (string) then convert to float
                    add_var = add_var + temp
        avg = add_var /24
        i365days = i365days + 1

        average.append(avg)
    return average

def avg_data_2016():
    i365days = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2016.csv', chunksize=24):  # chunksize means how many records to take, 24hours so is 24 records
        add_var = 0     # used to accumulate the sum of PM2.5 values for the 24 hours in each chunk
        avg = 0.0       # intended to store the average PM2.5 value for that chunk
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i       # if the value is a float or an integer, then add tgt
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)     # if the value is in diff data format (string) then convert to float
                    add_var = add_var + temp
        avg = add_var /24
        i365days = i365days + 1

        average.append(avg)
    return average

def avg_data_2017():
    i365days = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2017.csv', chunksize=24):  # chunksize means how many records to take, 24hours so is 24 records
        add_var = 0     # used to accumulate the sum of PM2.5 values for the 24 hours in each chunk
        avg = 0.0       # intended to store the average PM2.5 value for that chunk
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i       # if the value is a float or an integer, then add tgt
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)     # if the value is in diff data format (string) then convert to float
                    add_var = add_var + temp
        avg = add_var /24
        i365days = i365days + 1

        average.append(avg)
    return average

def avg_data_2018():
    i364days = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2018.csv', chunksize=24):  # chunksize means how many records to take, 24hours so is 24 records
        add_var = 0     # used to accumulate the sum of PM2.5 values for the 24 hours in each chunk
        avg = 0.0       # intended to store the average PM2.5 value for that chunk
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var = add_var + i       # if the value is a float or an integer, then add tgt
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i != '---' and i != 'InVld':
                    temp = float(i)     # if the value is in diff data format (string) then convert to float
                    add_var = add_var + temp
        avg = add_var /24
        i364days = i364days + 1

        average.append(avg)
    return average


if __name__ == '__main__':
    lst2013 = avg_data_2013()
    lst2014 = avg_data_2014()
    lst2015 = avg_data_2015()
    lst2016 = avg_data_2016()
    lst2017 = avg_data_2017()
    lst2018 = avg_data_2018()
    plt.plot(range(0,365),lst2013, label="2013 data")
    plt.plot(range(0,364),lst2014, label="2014 data")
    plt.plot(range(0,365),lst2015, label="2015 data")
    plt.plot(range(0,365),lst2016, label="2016 data")
    plt.plot(range(0,365),lst2017, label="2017 data")
    plt.plot(range(0,364),lst2018, label="2018 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()


    print(lst2013)







