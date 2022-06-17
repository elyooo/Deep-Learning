import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import csv
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import kendalltau
from scipy.stats import pearsonr

#Read dataset
data = pd.read_csv (r'D:\Σχολή\4ο\Βαθιά Μάθηση\compressed_dataset.csv')
#Convert to date
data['date'] = pd.to_datetime(data['timestamp'],unit='ms')
#Group by month
per = data['date'].dt.to_period("M")
data['month'] = per
data_month = data.groupby(per)
data['month_n'] = data['date'].dt.month
data['day'] = data['date'].dt.day

#country = []
#city = []
#mean_per_ev = []
#mean_per_cust = []
#mean_per_m = []
#final = []
#x_axis = ['9-2021', '10-2021', '11-2021', '12-2021', '1-2022', '2-2022', '3-2022']

############  Average Engagement taking into account the customer_id  ##############
#for i in data_month.groups.keys():
    #groups by customer_id in each month
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
        # groups b2 y event_id for each customer
    #    event = month[month['event_id'] == j]
     #   data_cust = event.groupby('customer_id')
      #  for k in data_cust.groups.keys():
            # calculates average engagement for each event
       #     cust = event[event['customer_id'] == k]
        #    mean_per_cust.append(cust['engagement'].mean())
        #mean_per_ev.append(sum(mean_per_cust)/len(mean_per_cust))
        #mean_per_cust.clear()
   # mean_per_m.append(sum(mean_per_ev)/len(mean_per_ev))
    #mean_per_ev.clear()

#plt.bar(x_axis, mean_per_m)
#plt.ylim(0.3, 0.5)
#plt.xlabel('Months')
#plt.ylabel('Average engagement')
#plt.show()

############  Average Engagement taking into account the country_id  ##############
#for i in data_month.groups.keys():
    #groups by customer_id in each month
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
        # groups by event_id for each customer
    #    event = month[month['event_id'] == j]
     #   data_cust = event.groupby('country_id')
      #  for k in data_cust.groups.keys():
            # calculates average engagement for each event
       #     cust = event[event['country_id'] == k]
        #    mean_per_cust.append(cust['engagement'].mean())
       # mean_per_ev.append(sum(mean_per_cust)/len(mean_per_cust))
        #mean_per_cust.clear()
   # mean_per_m.append(sum(mean_per_ev)/len(mean_per_ev))
    #mean_per_ev.clear()

#plt.bar(x_axis, mean_per_m)
#plt.ylim(0.3, 0.5)
#plt.xlabel('Months')
#plt.ylabel('Average engagement')
#plt.show()


############  Average Engagement taking into account the city_id  ##############
#for i in data_month.groups.keys():
    #groups by customer_id in each month
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
        # groups by event_id for each customer
    #    event = month[month['event_id'] == j]
     #   data_cust = event.groupby('city_id')
      #  for k in data_cust.groups.keys():
            # calculates average engagement for each event
       #     cust = event[event['city_id'] == k]
        #    mean_per_cust.append(cust['engagement'].mean())
        #mean_per_ev.append(sum(mean_per_cust)/len(mean_per_cust))
        #mean_per_cust.clear()
   # mean_per_m.append(sum(mean_per_ev)/len(mean_per_ev))
    #mean_per_ev.clear()

#plt.bar(x_axis, mean_per_m)
#plt.ylim(0.3, 0.5)
#plt.xlabel('Months')
#plt.ylabel('Average engagement')
#plt.show()


##################################################################################

############  Average QoE taking into account the customer_id  ##############
#for i in data_month.groups.keys():
    #groups by customer_id in each month
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
        # groups by event_id for each customer
    #    event = month[month['event_id'] == j]
     #   data_cust = event.groupby('customer_id')
      #  for k in data_cust.groups.keys():
            # calculates average engagement for each event
       #     cust = event[event['customer_id'] == k]
        #    mean_per_cust.append(cust['qoe'].mean())
        #mean_per_ev.append(sum(mean_per_cust)/len(mean_per_cust))
        #mean_per_cust.clear()
   # mean_per_m.append(sum(mean_per_ev)/len(mean_per_ev))
    #mean_per_ev.clear()

#plt.bar(x_axis, mean_per_m)
#plt.ylim(0.9, 1)
#plt.xlabel('Months')
#plt.ylabel('Average qoe')
#plt.show()


############  Average QoE taking into account the country_id  ##############
#for i in data_month.groups.keys():
    #groups by customer_id in each month
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
        # groups by event_id for each customer
    #    event = month[month['event_id'] == j]
     #   data_cust = event.groupby('country_id')
      #  for k in data_cust.groups.keys():
            # calculates average engagement for each event
       #     cust = event[event['country_id'] == k]
        #    mean_per_cust.append(cust['qoe'].mean())

        #mean_per_ev.append(sum(mean_per_cust)/len(mean_per_cust))
        #mean_per_cust.clear()
    #mean_per_m.append(sum(mean_per_ev)/len(mean_per_ev))
    #mean_per_ev.clear()

#plt.bar(x_axis, mean_per_m)
#plt.ylim(0.9, 1)
#plt.xlabel('Months')
#plt.ylabel('Average qoe')
#plt.show()

############  Average QoE taking into account the city_id  ##############
#for i in data_month.groups.keys():
    #groups by customer_id in each month
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
        # groups by event_id for each customer
    #    event = month[month['event_id'] == j]
     #   data_cust = event.groupby('city_id')
      #  for k in data_cust.groups.keys():
            # calculates average engagement for each event
       #     cust = event[event['city_id'] == k]
        #    mean_per_cust.append(cust['qoe'].mean())

        #mean_per_ev.append(sum(mean_per_cust)/len(mean_per_cust))
        #mean_per_cust.clear()
    #mean_per_m.append(sum(mean_per_ev)/len(mean_per_ev))
    #mean_per_ev.clear()

#plt.bar(x_axis, mean_per_m)
#plt.ylim(0.9, 1)
#plt.xlabel('Months')
#plt.ylabel('Average qoe')
#plt.show()


#######################################################################################

#############Viewers’ engagement/QoE distribution differences based on the viewer type parameter############

#x = np.arange(len(x_axis))
#office = []
#home = []
#office_final = []
#home_final = []

#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
    #    event = month[month['event_id']==j]
     #   office.append(event[event['viewer_type']=='WFO']['engagement'].mean())
      #  home.append(event[event['viewer_type'] == 'WFH']['engagement'].mean())
  #  office_final.append(np.nansum(office)/len(office))
   # home_final.append(np.nansum(home)/len(home))
    #office.clear()
    #home.clear()

#plt.bar(x - 0.2, office_final, 0.4, label='Office')
#plt.bar(x + 0.2, home_final, 0.4, label='Home')
#plt.xticks(x, x_axis)
#plt.xlabel('Months')
#plt.ylabel('Average Engagement')
#plt.ylim(0.3, 0.5)
#plt.legend()
#plt.show()

#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
    #    event = month[month['event_id']==j]
     #   office.append(event[event['viewer_type']=='WFO']['qoe'].mean())
      #  home.append(event[event['viewer_type'] == 'WFH']['qoe'].mean())
 #   office_final.append(np.nansum(office)/len(office))
  #  home_final.append(np.nansum(home)/len(home))
   # office.clear()
    #home.clear()

#plt.bar(x - 0.2, office_final, 0.4, label='Office')
#plt.bar(x + 0.2, home_final, 0.4, label='Home')
#plt.xticks(x, x_axis)
#plt.xlabel('Months')
#plt.ylabel('Average QoE')
#plt.ylim(0.8, 1)
#plt.legend()
#plt.show()




##############################################################################################

############Viewers’ engagement level duration over country###############

#low = []
#medium = []
#high = []
#low_sum = []
#medium_sum = []
#high_sum = []
#low_final = []
#medium_final = []
#high_final = []

#data['level'] = pd.cut(data['engagement'], bins = 3, labels = ('low', 'medium', 'high'))

#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
    #    event = month[month['event_id'] == j]
     #   data_country = event.groupby('country_id')
      #  for k in data_country.groups.keys():
       #     country = event[event['country_id'] == k]
        #    low.append((country[country['level'] =='low']['timestamp'].max() - country[country['level']=='low']['timestamp'].min())/60000)
         #   medium.append((country[country['level']=='medium']['timestamp'].max() - country[country['level']=='medium']['timestamp'].min())/60000)
          #  high.append((country[country['level']=='high']['timestamp'].max() - country[country['level']=='high']['timestamp'].min())/60000)
    #    low_sum.append(np.nansum(low)/len(low))
     #   medium_sum.append(np.nansum(medium)/len(medium))
      #  high_sum.append(np.nansum(high)/len(high))
       # low.clear()
        #medium.clear()
        #high.clear()
 #   low_final.append(np.nansum(low_sum)/len(low_sum))
  #  medium_final.append(np.nansum(medium_sum)/len(medium_sum))
   # high_final.append(np.nansum(high_sum)/len(high_sum))
    #low_sum.clear()
    #medium_sum.clear()
    #high_sum.clear()

#plt.bar(x, low_final, 0.25, label='Low')
#plt.bar(x + 0.25, medium_final, 0.25, label='Medium')
#plt.bar(x + 0.5, high_final, 0.25, label='High')
#plt.xticks(x+0.25, x_axis)
#plt.xlabel('Months')
#plt.ylabel('Engagement Level Duration (minutes)')
#plt.ylim(top=70)
#plt.legend()
#plt.show()


################Viewers’ engagement level duration over city###############

#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
    #    event = month[month['event_id'] == j]
     #   data_country = event.groupby('city_id')
      #  for k in data_country.groups.keys():
       #     country = event[event['city_id'] == k]
        #    low.append((country[country['level'] =='low']['timestamp'].max() - country[country['level']=='low']['timestamp'].min())/60000)
         #   medium.append((country[country['level']=='medium']['timestamp'].max() - country[country['level']=='medium']['timestamp'].min())/60000)
          #  high.append((country[country['level']=='high']['timestamp'].max() - country[country['level']=='high']['timestamp'].min())/60000)
      #  low_sum.append(np.nansum(low)/len(low))
       # medium_sum.append(np.nansum(medium)/len(medium))
        #high_sum.append(np.nansum(high)/len(high))
        #low.clear()
        #medium.clear()
        #high.clear()
 #   low_final.append(np.nansum(low_sum)/len(low_sum))
  #  medium_final.append(np.nansum(medium_sum)/len(medium_sum))
   # high_final.append(np.nansum(high_sum)/len(high_sum))
    #low_sum.clear()
    #medium_sum.clear()
    #high_sum.clear()

#plt.bar(x, low_final, 0.25, label='Low')
#plt.bar(x + 0.25, medium_final, 0.25, label='Medium')
#plt.bar(x + 0.5, high_final, 0.25, label='High')
#plt.xticks(x+0.25, x_axis)
#plt.xlabel('Months')
#plt.ylabel('Engagement Level Duration (minutes)')
#plt.ylim(top=50)
#plt.legend()
#plt.show()


#################Viewers’ engagement level duration over viewer type################

#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
    #    event = month[month['event_id'] == j]
     #   data_country = event.groupby('viewer_type')
      #  for k in data_country.groups.keys():
       #     country = event[event['viewer_type'] == k]
        #    low.append((country[country['level'] =='low']['timestamp'].max() - country[country['level']=='low']['timestamp'].min())/60000)
         #   medium.append((country[country['level']=='medium']['timestamp'].max() - country[country['level']=='medium']['timestamp'].min())/60000)
          #  high.append((country[country['level']=='high']['timestamp'].max() - country[country['level']=='high']['timestamp'].min())/60000)
   #     low_sum.append(np.nansum(low)/len(low))
    #    medium_sum.append(np.nansum(medium)/len(medium))
     #   high_sum.append(np.nansum(high)/len(high))
      #  low.clear()
       # medium.clear()
        #high.clear()
#    low_final.append(np.nansum(low_sum)/len(low_sum))
 #   medium_final.append(np.nansum(medium_sum)/len(medium_sum))
  #  high_final.append(np.nansum(high_sum)/len(high_sum))
   # low_sum.clear()
    #medium_sum.clear()
    #high_sum.clear()

#plt.bar(x, low_final, 0.25, label='Low')
#plt.bar(x + 0.25, medium_final, 0.25, label='Medium')
#plt.bar(x + 0.5, high_final, 0.25, label='High')
#plt.xticks(x+0.25, x_axis)
#plt.xlabel('Months')
#plt.ylabel('Engagement Level Duration (minutes)')
#plt.ylim(top=90)
#plt.legend()
#plt.show()



####################### Countries that follow different distributions per customer #######################

#low_d = 0
#medium_d = 0
#high_d = 0
#low_d_list = []
#medium_d_list = []
#high_d_list = []

#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
    #    event = month[month['event_id'] == j]
     #   data_cust = event.groupby('customer_id')
      #  for k in data_cust.groups.keys():
       #     cust = event[event['customer_id'] == k]
        #    data_country = cust.groupby('country_id')
         #   for l in data_country.groups.keys():
          #      country = cust[cust['country_id'] == l]
           #     if country['engagement'].mean() <= 0.33333:
            #        low_d += 1
             #   elif country['engagement'].mean() <= 0.66666:
              #      medium_d += 1
               # else:
                #    high_d += 1
    #low_d_list.append(low_d)
    #medium_d_list.append(medium_d)
    #high_d_list.append(high_d)
    #low_d = 0
    #medium_d = 0
    #high_d = 0

#plt.bar(x, low_d_list, 0.25, label='Low')
#plt.bar(x + 0.25, medium_d_list, 0.25, label='Medium')
#plt.bar(x + 0.5, high_d_list, 0.25, label='High')
#plt.xticks(x+0.25, x_axis)
#plt.xlabel('Months')
#plt.ylabel('Countries')
#plt.legend()
#plt.show()


#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
    #    event = month[month['event_id'] == j]
     #   data_cust = event.groupby('customer_id')
      #  for k in data_cust.groups.keys():
       #     cust = event[event['customer_id'] == k]
        #    data_country = cust.groupby('country_id')
         #   for l in data_country.groups.keys():
          #      country = cust[cust['country_id'] == l]
           #     if country['qoe'].mean() <= 0.33333:
            #        low_d += 1
             #   elif country['qoe'].mean() <= 0.66666:
              #      medium_d += 1
               # else:
                #    high_d += 1
    #low_d_list.append(low_d)
    #medium_d_list.append(medium_d)
#    high_d_list.append(high_d)
 #   low_d = 0
  #  medium_d = 0
   # high_d = 0

#plt.bar(x, low_d_list, 0.25, label='Low')
#plt.bar(x + 0.25, medium_d_list, 0.25, label='Medium')
#plt.bar(x + 0.5, high_d_list, 0.25, label='High')
#plt.xticks(x+0.25, x_axis)
#plt.xlabel('Months')
#plt.ylabel('Countries')
#plt.legend()
#plt.show()


#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
    #    event = month[month['event_id'] == j]
     #   data_cust = event.groupby('customer_id')
      #  for k in data_cust.groups.keys():
       #     cust = event[event['customer_id'] == k]
        #    data_country = cust.groupby('country_id')
         #   for l in data_country.groups.keys():
          #      country = cust[cust['country_id'] == l]
           #     if country['qoe'].mean() >= 0.9 and country['qoe'].mean() <= 0.93333:
            #        low_d += 1
             #   elif country['qoe'].mean() > 0.93333 and country['qoe'].mean() <= 0.96666:
              #      medium_d += 1
               # elif country['qoe'].mean() > 0.96666:
                #    high_d += 1
#    low_d_list.append(low_d)
 #   medium_d_list.append(medium_d)
  #  high_d_list.append(high_d)
   # low_d = 0
    #medium_d = 0
    #high_d = 0

#plt.bar(x, low_d_list, 0.25, label='Low')
#plt.bar(x + 0.25, medium_d_list, 0.25, label='Medium')
#plt.bar(x + 0.5, high_d_list, 0.25, label='High')
#plt.xticks(x+0.25, x_axis)
#plt.xlabel('Months')
#plt.ylabel('Countries')
#plt.legend()
#plt.show()



####################### Cities that follow different distributions per customer #######################

#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
    #    event = month[month['event_id'] == j]
     #   data_cust = event.groupby('customer_id')
      #  for k in data_cust.groups.keys():
       #     cust = event[event['customer_id'] == k]
        #    data_country = cust.groupby('city_id')
         #   for l in data_country.groups.keys():
          #      country = cust[cust['city_id'] == l]
           #     if country['engagement'].mean() <= 0.33333:
            #        low_d += 1
             #   elif country['engagement'].mean() <= 0.66666:
              #      medium_d += 1
               # else:
                #    high_d += 1
#    low_d_list.append(low_d)
 #   medium_d_list.append(medium_d)
  #  high_d_list.append(high_d)
   # low_d = 0
   # medium_d = 0
    #high_d = 0

#plt.bar(x, low_d_list, 0.25, label='Low')
#plt.bar(x + 0.25, medium_d_list, 0.25, label='Medium')
#plt.bar(x + 0.5, high_d_list, 0.25, label='High')
#plt.xticks(x+0.25, x_axis)
#plt.xlabel('Months')
#plt.ylabel('Cities')
#plt.legend()
#plt.show()


#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
    #    event = month[month['event_id'] == j]
     #   data_cust = event.groupby('customer_id')
      #  for k in data_cust.groups.keys():
       #     cust = event[event['customer_id'] == k]
        #    data_country = cust.groupby('city_id')
         #   for l in data_country.groups.keys():
          #      country = cust[cust['city_id'] == l]
           #     if country['qoe'].mean() <= 0.33333:
            #        low_d += 1
             #   elif country['qoe'].mean() <= 0.66666:
              #      medium_d += 1
               # else:
                #    high_d += 1
#    low_d_list.append(low_d)
 #   medium_d_list.append(medium_d)
  #  high_d_list.append(high_d)
   # low_d = 0
    #medium_d = 0
    #high_d = 0

#plt.bar(x, low_d_list, 0.25, label='Low')
#plt.bar(x + 0.25, medium_d_list, 0.25, label='Medium')
#plt.bar(x + 0.5, high_d_list, 0.25, label='High')
#plt.xticks(x+0.25, x_axis)
#plt.xlabel('Months')
#plt.ylabel('Countries')
#plt.legend()
#plt.show()


#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
    #    event = month[month['event_id'] == j]
     #   data_cust = event.groupby('customer_id')
      #  for k in data_cust.groups.keys():
       #     cust = event[event['customer_id'] == k]
        #    data_country = cust.groupby('city_id')
         #   for l in data_country.groups.keys():
          #      country = cust[cust['city_id'] == l]
           #     if country['qoe'].mean() >= 0.996 and country['qoe'].mean() < 0.99733:
            #        low_d += 1
             #   elif country['qoe'].mean() >= 0.99733 and country['qoe'].mean() < 0.99866:
              #      medium_d += 1
               # elif country['qoe'].mean() >= 0.99866:
                #    high_d += 1
#    low_d_list.append(low_d)
 #   medium_d_list.append(medium_d)
  #  high_d_list.append(high_d)
   # low_d = 0
    #medium_d = 0
    #high_d = 0

#plt.bar(x, low_d_list, 0.25, label='Low')
#plt.bar(x + 0.25, medium_d_list, 0.25, label='Medium')
#plt.bar(x + 0.5, high_d_list, 0.25, label='High')
#plt.xticks(x+0.25, x_axis)
#plt.xlabel('Months')
#plt.ylabel('Countries')
#plt.legend()
#plt.show()



####################### Correlations between the data points ###################################

#cust = []
#event = []
#viewer = []
#city = []
#country = []
#buffer = []
#engage = []
#qoe = []
#engage_all = []
#qoe_all = []
#cust_all = []
#city_all = []
#country_all = []
#event_all = []
#viewer_all = []
#buffer_all = []

#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  country.append(month['country_id'].nunique())
   # cust.append(month['customer_id'].nunique())
    #event.append(month['event_id'].nunique())
    #viewer.append(month['viewer_id'].nunique())
    #city.append(month['city_id'].nunique())
    #buffer.append(month['buffer_ms'].mean())
    #engage.append(month['engagement'].mean())
    #qoe.append(month['qoe'].mean())


#df = pd.DataFrame({'countries': country, 'customers': cust, 'events': event, 'viewers': viewer, 'cities': city, 'engagement': engage, 'qoe': qoe, 'buffer': buffer})
#corr = df.corr(method='pearson')
#sns.heatmap(corr, annot=True)
#plt.show()

#plt.scatter(country, event)      #Number of countries and events
#plt.plot(np.unique(country), np.poly1d(np.polyfit(country, event, 1))
#(np.unique(country)), color='red')
#plt.xlabel('Number of countries')
#plt.ylabel('Number of events')
#plt.title('Correlation')
#plt.show()

#plt.scatter(country, viewer)      #Number of countries and viewers
#plt.plot(np.unique(country), np.poly1d(np.polyfit(country, viewer, 1))
#(np.unique(country)), color='red')
#plt.xlabel('Number of countries')
#plt.ylabel('Number of viewers')
#plt.title('Correlation')
#plt.show()

#plt.scatter(country, city)      #Number of countries and cities
#plt.plot(np.unique(country), np.poly1d(np.polyfit(country, city, 1))
#(np.unique(country)), color='red')
#plt.xlabel('Number of countries')
#plt.ylabel('Number of cities')
#plt.title('Correlation')
#plt.show()

#plt.scatter(cust, event)      #Number of customers and events
#plt.plot(np.unique(cust), np.poly1d(np.polyfit(cust, event, 1))
#(np.unique(cust)), color='red')
#plt.xlabel('Number of customers')
#plt.ylabel('Number of events')
#plt.title('Correlation')
#plt.show()

#plt.scatter(cust, viewer)      #Number of customers and viewers
#plt.plot(np.unique(cust), np.poly1d(np.polyfit(cust, viewer, 1))
#(np.unique(cust)), color='red')
#plt.xlabel('Number of customers')
#plt.ylabel('Number of viewers')
#plt.title('Correlation')
#plt.show()

#plt.scatter(cust, city)      #Number of customers and cities
#plt.plot(np.unique(cust), np.poly1d(np.polyfit(cust, city, 1))
#(np.unique(cust)), color='red')
#plt.xlabel('Number of customers')
#plt.ylabel('Number of cities')
#plt.title('Correlation')
#plt.show()

#plt.scatter(event, viewer)      #Number of events and viewers
#plt.plot(np.unique(event), np.poly1d(np.polyfit(event, viewer, 1))
#(np.unique(event)), color='red')
#plt.xlabel('Number of events')
#plt.ylabel('Number of viewers')
#plt.title('Correlation')
#plt.show()

#plt.scatter(event, city)      #Number of events and cities
#plt.plot(np.unique(event), np.poly1d(np.polyfit(event, city, 1))
#(np.unique(event)), color='red')
#plt.xlabel('Number of events')
#plt.ylabel('Number of cities')
#plt.title('Correlation')
#plt.show()

#plt.scatter(viewer, city)      #Number of viewers and cities
#plt.plot(np.unique(viewer), np.poly1d(np.polyfit(viewer, city, 1))
#(np.unique(viewer)), color='red')
#plt.xlabel('Number of viewers')
#plt.ylabel('Number of cities')
#plt.title('Correlation')
#plt.show()

#plt.scatter(engage, buffer)
#plt.plot(np.unique(engage), np.poly1d(np.polyfit(engage, buffer, 1))
#(np.unique(engage)), color='red')
#plt.xlabel('Average engagement')
#plt.ylabel('Average buffer')
#plt.title('Correlation')
#plt.show()

#plt.scatter(qoe, buffer)
#plt.plot(np.unique(qoe), np.poly1d(np.polyfit(qoe, buffer, 1))
#(np.unique(qoe)), color='red')
#plt.xlabel('Average qoe')
#plt.ylabel('Average buffer')
#plt.title('Correlation')
#plt.show()


#Group by country
#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_country = month.groupby('country_id')
   # for j in data_country.groups.keys():
    #    country_id = data[data['country_id'] == j]
     #   qoe.append(country_id['qoe'].mean())
      #  engage.append(country_id['engagement'].mean())
       # cust.append(country_id['customer_id'].nunique())
        #city.append(country_id['city_id'].nunique())
     #   event.append(country_id['event_id'].nunique())
      #  viewer.append(country_id['viewer_id'].nunique())
       # buffer.append(country_id['buffer_ms'].mean())
#    engage_all.append(sum(engage)/len(engage))
 #   qoe_all.append(sum(qoe)/len(qoe))
  #  cust_all.append(sum(cust) / len(cust))
   # city_all.append(sum(city)/len(city))
    #event_all.append(sum(event)/len(event))
#    viewer_all.append(sum(viewer)/len(viewer))
 #   buffer_all.append(sum(buffer)/len(buffer))
  #  qoe.clear()
   # engage.clear()
    #cust.clear()
    #city.clear()
    #event.clear()
    #viewer.clear()
    #buffer.clear()

#df = pd.DataFrame({'customers': cust_all, 'cities': city_all, 'events': event_all, 'viewers': viewer_all, 'engagement': engage_all, 'qoe': qoe_all, 'buffer': buffer_all})
#corr = df.corr(method='pearson')
#sns.heatmap(corr, annot=True)
#plt.show()


#Group by customer
#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_cust = month.groupby('customer_id')
   # for j in data_cust.groups.keys():
    #    cust_id = data[data['customer_id'] == j]
     #   qoe.append(cust_id['qoe'].mean())
      #  engage.append(cust_id['engagement'].mean())
       # country.append(cust_id['country_id'].nunique())
        #city.append(cust_id['city_id'].nunique())
    #    event.append(cust_id['event_id'].nunique())
     #   viewer.append(cust_id['viewer_id'].nunique())
      #  buffer.append(cust_id['buffer_ms'].mean())
#    engage_all.append(sum(engage)/len(engage))
 #   qoe_all.append(sum(qoe)/len(qoe))
  #  country_all.append(sum(country)/len(country))
   # city_all.append(sum(city)/len(city))
    #event_all.append(sum(event)/len(event))
#    viewer_all.append(sum(viewer)/len(viewer))
 #   buffer_all.append(sum(buffer)/len(buffer))
  #  qoe.clear()
   # engage.clear()
    #country.clear()
    #city.clear()
    #event.clear()
    #viewer.clear()
    #buffer.clear()

#df = pd.DataFrame({'countries': country_all, 'cities': city_all, 'events': event_all, 'viewers': viewer_all, 'engagement': engage_all, 'qoe': qoe_all, 'buffer': buffer_all})
#corr = df.corr(method='pearson')
#sns.heatmap(corr, annot=True)
#plt.show()





####################### Correlation between viewer engagement and number of viewers during the event ####################

#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
    #    event_id = data[data['event_id'] == j]
     #   engage.append(event_id['engagement'].mean())
      #  viewer.append(event_id['viewer_id'].nunique())
#    engage_all.append(sum(engage)/len(engage))
 #   viewer_all.append(sum(viewer)/len(viewer))
  #  engage.clear()
   # viewer.clear()

#df = pd.DataFrame({'engagement': engage_all, 'viewers': viewer_all})
#corr = df.corr(method='pearson')
#sns.heatmap(corr, annot=True)
#plt.show()
#plt.scatter(engage_all, viewer_all)
#plt.plot(np.unique(engage_all), np.poly1d(np.polyfit(engage_all, viewer_all, 1))
#(np.unique(engage_all)), color='red')
#plt.show()


####################### Correlation between viewer engagement and the day of the event ###########################

#days = []

#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  unique_days = set(month['day'])
   # for k in unique_days:
    #    days.append(k)
   # data_day = month.groupby('day')
    #for j in data_day.groups.keys():
     #   day = month[month['day'] == j]
      #  data_event = day.groupby('event_id')
       # for l in data_event.groups.keys():
        #    event_id = day[day['event_id']==l]
         #   engage.append(event_id['engagement'].mean())
      #  engage_all.append(sum(engage)/len(engage))
       # engage.clear()
#    df = pd.DataFrame({'engagement': engage_all, 'day': days})
#    corr = df.corr(method='pearson')
 #   sns.heatmap(corr, annot=True)
  #  plt.title(i)
   # plt.show()
    #engage_all.clear()
    #days.clear()




####################### Correlation between viewer engagement and duration of the event ###########################

#dur = []

#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
    #    event = month[month['event_id'] == j]
     #   engage.append(event['engagement'].mean())
      #  dur.append(event['timestamp'].max() - event['timestamp'].min())

#df = pd.DataFrame({'engagement': engage, 'duration': dur})
#corr = df.corr(method='pearson')
#sns.heatmap(corr, annot=True)
#plt.show()
#plt.scatter(engage, dur)
#plt.plot(np.unique(engage), np.poly1d(np.polyfit(engage, dur, 1))
#(np.unique(engage)), color='red')
#plt.show()



####################### Correlation between viewer engagement and countries ###########################

#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
    #    event_id = data[data['event_id'] == j]
     #   engage.append(event_id['engagement'].mean())
      #  country.append(event_id['country_id'].nunique())
 #   engage_all.append(sum(engage)/len(engage))
  #  country_all.append(sum(country)/len(country))
   # engage.clear()
    #country.clear()

#df = pd.DataFrame({'engagement': engage_all, 'countries': country_all})
#corr = df.corr(method='pearson')
#sns.heatmap(corr, annot=True)
#plt.show()



####################### Correlation between viewer engagement and viewers’ retention ###########################

#ret = []
#ret_all = []
#final_eng = []
#final_ret = []

#for i in data_month.groups.keys():
 #   month = data[data['month'] == i]
  #  data_event = month.groupby('event_id')
   # for j in data_event.groups.keys():
    #    event = month[month['event_id'] == j]
     #   data_cust = event.groupby('viewer_id')
      #  for k in data_cust.groups.keys():
       #     cust = event[event['viewer_id'] == k]
        #    engage.append(cust['engagement'].mean())
         #   ret.append(cust['timestamp'].max() - cust['timestamp'].min())
    #    engage_all.append(sum(engage)/len(engage))
     #   ret_all.append(sum(ret)/len(ret))
      #  engage.clear()
       # ret.clear()
#    final_eng.append(sum(engage_all)/len(engage_all))
 #   final_ret.append(sum(ret_all)/len(ret_all))
  #  engage_all.clear()
   # ret_all.clear()

#df = pd.DataFrame({'engagement': final_eng, 'retention': final_ret})
#corr = df.corr(method='spearman')
#sns.heatmap(corr, annot=True)
#plt.show()
#plt.scatter(final_eng, final_ret)
#plt.plot(np.unique(final_eng), np.poly1d(np.polyfit(final_eng, final_ret, 1))
#(np.unique(final_eng)), color='red')
#plt.show()
