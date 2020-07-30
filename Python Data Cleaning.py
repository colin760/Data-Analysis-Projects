#Data cleaning project using python
import pandas as pd
#First read in the data 
#Date is gifted and talented student data from New York City
GT_data = pd.read_csv("/Users/colinbrant/Downloads/G&T Results 2017-18 (Responses) - Form Responses 1.csv")
#Next investigate the data to get idea of what it looks like
GT_data.head(10)
GT_data.columns

#Now we can see all the different columns and types of values stored in the columns 
#Since we can see the columns we can gather the relevant ones but first lets rename a column
GT_data.rename(columns={'District':'School District'}, inplace=True)
GT_data.columns
cols = ['Entering Grade Level', 'School District', 'OLSAT Verbal Score', 'OLSAT Verbal Percentile', 
        'NNAT Non Verbal Raw Score', 'NNAT Non Verbal Percentile', 'Overall Score', 'School Assigned']
GT_data1 = GT_data[cols]
GT_data1.head(10)
#Now we have the relevent data selected

#However we still have lots of missing data in the new data frame 
#In order to have better data we need to remove these values 
GT_data1 = GT_data1.dropna()
#Now we have removed rows that have missing values we can better intrept the data
#Now we need to drop the duplicate rows from the data 
GT_data1 = GT_data1.drop_duplicates()
print(GT_data1)

#Now that we have no null values and no duplicates its time to fix some of the formatting
GT_data1['OLSAT Verbal Percentile'] = GT_data1['OLSAT Verbal Percentile'].astype(str) + '%'
GT_data1['NNAT Non Verbal Percentile'] = GT_data1['NNAT Non Verbal Percentile'].astype(str) + '%'
GT_data1.head()
#Unfortunately this dataset is too small for removing outliers to help the overall data quality
#So we are done cleaning this small dataset