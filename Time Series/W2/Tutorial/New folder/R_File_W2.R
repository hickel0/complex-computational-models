install.packages('fpp2') # this is for autoplot
library(fpp2)
retaildata <- read.csv('retail.csv') # don’t forget to fix path!
mytimeseries <- ts(retaildata[,4], frequency=12, start=c(1982,4)) # here                            column 4 was chosen but any one can be chosen
autoplot(mytimeseries)

