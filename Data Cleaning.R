#Data Cleaning Project Using New York City Bed and Breakfast Data from 
#https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data

#First load in the data using read.csv()
NYC_BnB <- read.csv("/Users/colinbrant/Downloads/AB_NYC_2019.csv")

#Next use the head and glimpse functions to investigate the dataset
head(NYC_BnB)
glimpse(NYC_BnB)


#Next using the select function we will gather the relevant columns of data 
new_NYC_BnB <- select(NYC_BnB, name, neighbourhood_group, neighbourhood, room_type, price)

#Now check for missing data in the new dataset
is.na(new_NYC_BnB)
#Since there are so many rows we can use the sum function 
sum(is.na(new_NYC_BnB))
#The sum is 0 so there are no missing values 

#Another thing we need to check for is duplicate values in the data
duplicated(new_NYC_BnB)
sum(duplicated(new_NYC_BnB))
#There are 149 duplicate values in the dataset
#Using the unique function we can remove duplicated rows from the dataset
new_NYC_BnB <- unique(new_NYC_BnB)


#Next we want to remove outliers from the data however in order to do this we need
#to filter by room type
privateRoom_NYC <- filter(new_NYC_BnB, room_type == "Private room")
entireHome_NYC <- filter(new_NYC_BnB, room_type == "Entire home/apt")
other_NYC <- filter(new_NYC_BnB, room_type == "Shared room")
#Now make boxplots to find outliers
boxplot(privateRoom_NYC$price)
boxplot(entireHome_NYC$price)
boxplot(other_NYC$price)
#Now store the outliers 
private_outliers <- boxplot(privateRoom_NYC$price, plot = FALSE)$out
entireHome_outliers <- boxplot(entireHome_NYC$price, plot = FALSE)$out
other_outliers <- boxplot(other_NYC$price, plot = FALSE)$out
#The next step is to remove the outliers 
privateRoom_NYC <- privateRoom_NYC[-which(privateRoom_NYC$price %in% private_outliers),]
entireHome_NYC <- entireHome_NYC[-which(entireHome_NYC$price %in% entireHome_outliers),]
other_outliers <- other_NYC[-which(other_NYC$price %in% other_outliers),]
#Now that we have removed the outliers from each room type we need to join together
#the filtered data frames.
f_NYC_BnB <- rbind(privateRoom_NYC, entireHome_NYC)
full_NYC_BnB <- rbind(f_NYC_BnB, other_NYC)
#Now we have the full dataset withoout outliers and the dataset is cleaned


