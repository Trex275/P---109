import csv
from os import fstat
import plotly.figure_factory
import statistics
import pandas as pd

df = pd.read_csv("Projects\P109\archive\StudentsPerformance.csv")
mathlist = df["math score"].tolist()
readlist = df["reading score"].tolist()

meanmath = statistics.mean(mathlist)
medianmath = statistics.median(mathlist)
modemath = statistics.mode(mathlist)
stddev = statistics.stdev(mathlist)
print(meanmath, medianmath, modemath, stddev)

# first standard deviation
fstart = meanmath - stddev
fend = meanmath + stddev
print(fstart, fend)

list_of_mathdata_in_first_stdev = []
for data in mathlist:
    if data >= fstart and data <= fend:
        list_of_mathdata_in_first_stdev.append(data)

percent_of_mathdata_in_first_stdev = len(list_of_mathdata_in_first_stdev)/len(mathlist)
print(percent_of_mathdata_in_first_stdev)


# second standard deviation
sstart = meanmath - 2 * stddev
send = meanmath + 2 * stddev

list_of_mathdata_in_second_stdev = []
for data in mathlist:
    if data >= sstart and data <= send:
        list_of_mathdata_in_second_stdev.append(data)

percent_of_mathdata_in_second_stdev = len(list_of_mathdata_in_second_stdev)/len(mathlist)
print(percent_of_mathdata_in_second_stdev)

meanread = statistics.mean(readlist)
medianread = statistics.median(readlist)
moderead = statistics.mode(readlist)
stddevread = statistics.stdev(readlist)
print(meanread, medianread, moderead, stddevread)

# first standard deviation
fstart = meanread - stddevread
fend = meanread + stddevread
print(fstart, fend)

list_of_readdata_in_first_stdev = []
for data in readlist:
    if data >= fstart and data <= fend:
        list_of_readdata_in_first_stdev.append(data)

percent_of_readdata_in_first_stdev = len(list_of_readdata_in_first_stdev)/len(readlist)
print(percent_of_readdata_in_first_stdev)

# second standard deviation
sstart = meanread - 2 * stddevread
send = meanread + 2 * stddevread

list_of_readdata_in_second_stdev = []
for data in readlist:
    if data >= sstart and data <= send:
        list_of_readdata_in_second_stdev.append(data)

percent_of_readdata_in_second_stdev = len(list_of_readdata_in_second_stdev)/len(readlist)
print(percent_of_readdata_in_second_stdev)