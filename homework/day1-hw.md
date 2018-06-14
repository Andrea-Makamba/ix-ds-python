# Homework

## Problem 1

The file `crime_data.csv` contrains data on types of crimes commited in the US from 1960 - 2016. Complete the following problems using this data.

- Load the data into a pandas DataFrame, using the column names in the file and the column titled “Year” as the index. Make sure to skip lines that don’t contain data.
- Insert a new column into the data frame that contains the crime rate by year (the ratio
of “Total” column to the “Population” column).
- Plot the crime rate as a function of the year
- List the 5 years with the highest crime rate in descending order.
- Calculate the average number of total crimes as well as burglary crimes between 1960 and
2012.
- Find the years for which the total number of crimes was below average, but the number
of burglaries was above average.
- Plot the number of murders as a function of the population.
- Select the Population, Violent, and Robbery columns for all years in the 1980s, and save
this smaller data frame to a CSV file crime_subset.csv

## Problem 2

The file `titanic.csv` has various features on who survived the accident. We first start by cleaning

- Read the data into a DataFrame. Use the first row of the file as the column labels, but
do not use any of the columns as the index.
-  Drop the columns "Sibsp", "Parch", "Cabin", "Boat", "Body", and "home.dest"
-  Drop any entries without data in the "Survived" column, then change the remaining
entries to True or False (they start as 1 or 0).
- Replace null entries in the "Age" column with the average age.
- Save the new DataFrame as titanic_clean.csv

Next, answer the following questions

- How many people survived? What percentage of passengers survived?
- What was the average price of a ticket? How much did the most expensive ticket cost?
- How old was the oldest survivor? How young was the youngest survivor? What about
non-survivors?

