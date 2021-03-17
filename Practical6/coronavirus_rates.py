import matplotlib.pyplot as plt
frequency = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924}
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK'
sizes = [frequency['USA'],frequency['India'],frequency['Brazil'],frequency['Russia'],frequency['UK']]#build a connection between sizes and dictionary
explode = (0,0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',startangle=90)
plt.axis('equal')#make sure it is a standard cycle
plt.show()
