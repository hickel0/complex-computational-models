# R uses  xts and zoo for manipulating time series data
# an xts object a matrix of observations combined with an index of corresponding dates and times
# something like xts object = matrix object + times
install.packages("zoo")
install.packages("xts")
install.packages("pacman")
install.packages("tidyverse")
install.packages("readr") 	# For reading data
install.packages("dplyr") 	# For data manipulation
install.packages("lubridate") 	# For working with dates and time
install.packages("forecast")

library(zoo)
library(xts)
library(pacman)
library(tidyverse)
library(readr)      
library(dplyr)     
library(lubridate)  
library(forecast)

data <- read_csv("D:/Final Year/Complex Comp Models/W2/Tutorial/Tutorial_1_Data.csv/Tutorial_1_Q1_Data.csv") # take in the data file in date, value format
# What we have is a dataframe object, need to convert dataframe to xts (time series) object
dates <- seq(as.Date("2010-01-31"), length = 16, by = "quarters") # xts needs start, length, granularity of date
data_xts <- xts(data$'Sales_M€', order.by = dates)


# Calculate the 4pt WMA with ma() from forecast package
rolling_avg_4pt<-ma(data$'Sales_M€',order=4,centre=TRUE)  
# Note: with ma(), setting centre=TRUE with even order gives a weighted moving average

# Now we have everything necessary to calculate and plot the data
plot(data,type='l')
lines(dates,rolling_avg_4pt,col="red") # there is 'NA' for first 2 and last 2 points in series for CMA

# Now we have our plots

ggseasonplot # All the seasonal plots for all the years
ggsubseriesplot # All the months as series shown separately

