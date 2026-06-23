# Example 2.3 Part of the Ausbeer dataset
library(fpp)
data(ausbeer)
plot(ausbeer,xlim=c(1955,1970),ylim=c(220,450)) # Plot between the limits given

# Example 2.5  Electrical Equipment Orders 1995-2015
library(forecast)
plot(elec)


# Example 2.7 Decomposing a multiplicative series in R: Air Passenger dataset
library(ggfortify) 
library(tseries)
library(forecast)
data(AirPassengers) # this is where air pax data are stored
AP <- AirPassengers # load data
plot(AP)      		# have a look to confirm it needs a multiplicative decomposition
plot(log(AP))		# have a look at the log transform of the data
APdecomp <- decompose(log(AP)) # store the decomposed parts
plot(APdecomp)		# plot them!

library(stats)
elecequip %>%
  stl(t.window=13, s.window="periodic", robust=TRUE) %>%
  autoplot()

library(ggplot2)
autoplot(elecequip, series="Data") +
  autolayer(ma(elecequip, 12), series="12-MA") +
  xlab("Year") + ylab("New orders index") +
  ggtitle("Electrical equipment manufacturing (Euro area)") +
  scale_colour_manual(values=c("Data"="grey","12-MA"="red"),
                      breaks=c("Data","12-MA"))