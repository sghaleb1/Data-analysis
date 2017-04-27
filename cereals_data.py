import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the file, seperate with ';', due to the 'names' column within the data contains names seperated with commas 
df = pd.read_csv('cereal.csv', sep=';')

# drop index 0 as it consists of data types, as well as the H = hot and C = cold 'types' after mfr
cereals = df.drop(df.index[0])
cereals = cereals.drop(['name', 'type'], axis=1)

# For each in column in cereals from index 1 onwards we convert to a float
for col in cereals.columns[1:]:
    cereals[col] = cereals[col].astype('float')

# Assign a new variable and group by 'mfr' and return mean value
cereals_mfr = cereals.groupby('mfr').mean()
# Replpace the 'mfr' index name to 'Manufacturer' so the viewer can understand our the index name and for better visualisation
cereals_mfr.index.name = 'Manufacturer'
# Extract the ratings column only
cereals_mfr['rating']

#We use Seaborn's barplot and return the x and y values as well as giving the data we want to use.
ratings_g = sns.barplot(x=cereals_mfr.index, y='rating', data=cereals_mfr)
plt.show()

# Return the count of each value in mfr
mfr_count = pd.value_counts(cereals['mfr'].values, sort=False)

# Create a new dataframe consisting of only the data we need
mfr_count = pd.DataFrame(mfr_count, index = ['A', 'G', 'K', 'N', 'P', 'Q', 'R'])
# Rename count index
mfr_count.columns = ['Cereal counts']
# Rename manufacturers index
mfr_count.index.name = "Manufacturer's Key"

#Create the bar chart for counts
count_g = sns.barplot(x=mfr_count.index, y='Cereal counts', data=mfr_count)
plt.show()