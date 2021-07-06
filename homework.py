import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv("sf.csv")

dice = df["reading score"].to_list()

mean =sum(dice)/len(dice)
median=statistics.median(dice)
mode = statistics.mode(dice)

fig = ff.create_distplot([dice],["Result"],show_hist=False)
# find the % of data that lies between -sd and +sd

#first sd
sd = statistics.stdev(dice)
#Finding 1 standard deviation start and end values, and 2 standard deviations stard and end values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
sd1_start , sd1_end =mean-sd , mean+sd
sd2_start , sd2_end =mean-(2*sd) , mean +(2*sd)
sd3_start , sd3_end =mean-(3*sd) , mean +(3*sd)

#plot
fig.add_trace(go.Scatter (x=[mean,mean],y=[0,0.19],mode ="lines", name = "MEAN"))
# first sd
fig.add_trace(go.Scatter (x=[sd1_start,sd1_start],y=[0,0.19],mode ="lines", name = "standard deviation 1"))
fig.add_trace(go.Scatter (x=[sd1_end,sd1_end],y=[0,0.19],mode ="lines", name = "standard deviation 1"))

#second sd
fig.add_trace(go.Scatter (x=[sd2_start,sd2_start],y=[0,0.19],mode ="lines", name = "standard deviation 2"))
fig.add_trace(go.Scatter (x=[sd2_end,sd2_end],y=[0,0.19],mode ="lines", name = "standard deviation 2"))

#third sd
fig.add_trace(go.Scatter (x=[sd3_start,sd3_start],y=[0,0.19],mode ="lines", name = "standard deviation 3"))
fig.add_trace(go.Scatter (x=[sd3_end,sd3_end],y=[0,0.19],mode ="lines", name = "standard deviation 3"))

fig.show()

#list of data within -sd and +sd
list_of_data_within_1_std_deviation = [result for result in dice if result > sd1_start and result < sd1_end]
list_of_data_within_2_std_deviation = [result for result in dice if result > sd2_start and result < sd2_end]
list_of_data_within_3_std_deviation = [result for result in dice if result > sd3_start and result < sd3_end]


print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(sd))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice)))


