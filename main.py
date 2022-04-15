import pandas as pd
import matplotlib.pyplot as plt


#Read dataset
data = pd.read_csv (r'D:\Σχολή\4ο\Βαθιά Μάθηση\compressed_dataset.csv')
#Convert to date
data['date'] = pd.to_datetime(data['timestamp'],unit='ms')
#Group by month
per = data['date'].dt.to_period("M")
data['month'] = per
data_month = data.groupby(per)

mean_per_ev = []
mean_per_cust = []
mean_per_m = []
final = []


############  Average Engagement taking into account the customer_id  ##############
for i in data_month.groups.keys():
    #groups by customer_id in each month
    month = data[data['month'] == i]
    data_cust = month.groupby('customer_id')
    for j in data_cust.groups.keys():
        # groups by event_id for each customer
        cust = data[data['customer_id'] == j]
        data_event = cust.groupby('event_id')
        for k in data_event.groups.keys():
            # calculates average engagement for each event
            event = data[data['event_id'] == k]
            mean_per_ev.append(event['engagement'].mean())

        mean_per_cust.append(sum(mean_per_ev)/len(mean_per_ev))

        mean_per_ev.clear()
    mean_per_m.append(sum(mean_per_cust)/len(mean_per_cust))
    plt.hist(mean_per_m)
    plt.xlabel('Average engagement')
    plt.show()
    final.extend(mean_per_m)
    mean_per_cust.clear()
    mean_per_m.clear()

plt.plot(final)
plt.xlabel('Months')
plt.ylabel('Average engagement')
plt.show()

############  Average Engagement taking into account the country_id  ##############
#for i in data_month.groups.keys():
#    #groups by country_id in each month
#    month = data[data['month'] == i]
#    data_cust = month.groupby('country_id')

#    for j in data_cust.groups.keys():
#        # groups by event_id for each country
#        cust = data[data['country_id'] == j]
#        data_event = cust.groupby('event_id')
#        for k in data_event.groups.keys():
#            # calculates average engagement for each event
#            event = data[data['event_id'] == k]
#            mean_per_ev.append(event['engagement'].mean())

#        mean_per_cust.append(sum(mean_per_ev)/len(mean_per_ev))

#        mean_per_ev.clear()
#    mean_per_m.append(sum(mean_per_cust)/len(mean_per_cust))
#    plt.hist(mean_per_m)
#    plt.xlabel('Average engagement')
#    plt.show()
#    final.extend(mean_per_m)
#    mean_per_cust.clear()
#    mean_per_m.clear()

#plt.plot(final)
#plt.xlabel('Months')
#plt.ylabel('Average engagement')
#plt.show()


############  Average Engagement taking into account the city_id  ##############
#for i in data_month.groups.keys():
#    #groups by city_id in each month
#    month = data[data['month'] == i]
#    data_cust = month.groupby('city_id')

#    for j in data_cust.groups.keys():
#        # groups by event_id for each city
#        cust = data[data['city_id'] == j]
#        data_event = cust.groupby('event_id')
#        for k in data_event.groups.keys():
#            # calculates average engagement for each event
#            event = data[data['event_id'] == k]
#            mean_per_ev.append(event['engagement'].mean())

#        mean_per_cust.append(sum(mean_per_ev)/len(mean_per_ev))

#        mean_per_ev.clear()
#    mean_per_m.append(sum(mean_per_cust)/len(mean_per_cust))
#    plt.hist(mean_per_m)
#    plt.xlabel('Average engagement')
#    plt.show()
#    final.extend(mean_per_m)
#    mean_per_cust.clear()
#    mean_per_m.clear()

#plt.plot(final)
#plt.xlabel('Months')
#plt.ylabel('Average engagement')
#plt.show()


##################################################################################


############  Average QoE taking into account the customer_id  ##############
#for i in data_month.groups.keys():
#    #groups by customer_id in each month
#    month = data[data['month'] == i]
#    data_cust = month.groupby('customer_id')

#    for j in data_cust.groups.keys():
#        # groups by event_id for each customer
#        cust = data[data['customer_id'] == j]
#        data_event = cust.groupby('event_id')
#        for k in data_event.groups.keys():
#            # calculates average qoe for each event
#            event = data[data['event_id'] == k]
#            mean_per_ev.append(event['qoe'].mean())

#        mean_per_cust.append(sum(mean_per_ev)/len(mean_per_ev))

#        mean_per_ev.clear()
#    mean_per_m.append(sum(mean_per_cust)/len(mean_per_cust))
#    plt.hist(mean_per_m)
#    plt.xlabel('Average qoe')
#    plt.show()
#    final.extend(mean_per_m)
#    mean_per_cust.clear()
#    mean_per_m.clear()

#plt.plot(final)
#plt.xlabel('Months')
#plt.ylabel('Average qoe')
#plt.show()


############  Average QoE taking into account the country_id  ##############
#for i in data_month.groups.keys():
#    #groups by country_id in each month
#    month = data[data['month'] == i]
#    data_cust = month.groupby('country_id')

#    for j in data_cust.groups.keys():
#        # groups by event_id for each country
#        cust = data[data['country_id'] == j]
#        data_event = cust.groupby('event_id')
#        for k in data_event.groups.keys():
#            # calculates average qoe for each event
#            event = data[data['event_id'] == k]
#            mean_per_ev.append(event['qoe'].mean())

#        mean_per_cust.append(sum(mean_per_ev)/len(mean_per_ev))

#        mean_per_ev.clear()
#    mean_per_m.append(sum(mean_per_cust)/len(mean_per_cust))
#    plt.hist(mean_per_m)
#    plt.xlabel('Average qoe')
#    plt.show()
#    final.extend(mean_per_m)
#    mean_per_cust.clear()
#    mean_per_m.clear()

#plt.plot(final)
#plt.xlabel('Months')
#plt.ylabel('Average qoe')
#plt.show()

############  Average QoE taking into account the city_id  ##############
#for i in data_month.groups.keys():
#    #groups by city_id in each month
#    month = data[data['month'] == i]
#    data_cust = month.groupby('city_id')

#    for j in data_cust.groups.keys():
#        # groups by event_id for each city
#        cust = data[data['city_id'] == j]
#        data_event = cust.groupby('event_id')
#        for k in data_event.groups.keys():
#            # calculates average qoe for each event
#            event = data[data['event_id'] == k]
#            mean_per_ev.append(event['qoe'].mean())

#        mean_per_cust.append(sum(mean_per_ev)/len(mean_per_ev))

#        mean_per_ev.clear()
#    mean_per_m.append(sum(mean_per_cust)/len(mean_per_cust))
#    plt.hist(mean_per_m)
#    plt.xlabel('Average qoe')
#    plt.show()
#    final.extend(mean_per_m)
#    mean_per_cust.clear()
#    mean_per_m.clear()

#plt.plot(final)
#plt.xlabel('Months')
#plt.ylabel('Average qoe')
#plt.show()



