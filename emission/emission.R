require(signal)
setwd("~/Documents/GitHub/vizphiz/emission")

#Use dual Gaussian fit, creating a function that passes in two parameters:
#First parameter: an entire data frame (e.g. from a plate reader plate)
#Second parameter: The name of the well of interest, in quotes

gaussFit3 <- function(df) {
	data.frame(df) -> values
	#normalize to 1
	values$counts<-values$counts/max(values$counts)
	
	#uses least squares to find mean and variance of two Gaussian distributions
	#start is the initial parameter estimates, which sometimes need to change
	#values C1 and C2 are the "height", so normalized to 1 above
	#If "Error in convergence" may need to change the starting values
	fit <- nls(counts ~ (C1 * exp(-(wavelength-mean1)**2/(2 * sigma1**2)) +
	                  C2 * exp(-(wavelength-mean2)**2/(2 * sigma2**2)) + 
	                  C3 * exp(-(wavelength-mean3)**2/(2 * sigma3**2))
	                  ), data=values,
					   start=list(C1=.7, 	mean1=480, sigma1=30,
					   	   C2=.7, mean2=490, sigma2=40, 
					   	   C3=.7, mean3=500, sigma3=30 
					   	   ), 
					   	   algorithm="port")

	plot(counts~wavelength, data= values, xlim=c(400,600), ylim=c(0,1.1) )
	v <- summary(fit)$parameters[,"Estimate"]
	F1v <- v
	
    sum <- function(x) F1v[1]*exp(-1/2*(x-F1v [2])^2/F1v[3]^2) + F1v[4]*exp(-1/2*(x-F1v[5])^2/F1v[6]^2) + F1v[7]*exp(-1/2*(x-F1v [8])^2/F1v[9]^2) 
	emission <- function(x) F1v[1]*exp(-1/2*(x-F1v [2])^2/F1v[3]^2) + F1v[4]*exp(-1/2*(x-F1v[5])^2/F1v[6]^2)
	emission2 <- function(x) F1v[7]*exp(-1/2*(x-F1v [8])^2/F1v[9]^2) 
	optimize(emission, interval=c(430,550), maximum=TRUE)->lmax1
	optimize(emission2, interval=c(430,550), maximum=TRUE)->lmax2

    plot(sum, col="green",xlim=c(400,600), add=TRUE )
	plot(emission, col=2,xlim=c(400,600), abline(v=lmax1$maximum, col="blue"), add=TRUE )
	plot(emission2, col=2,xlim=c(400,600), abline(v=lmax2$maximum, col="blue"), add=TRUE )
    maxes <- c(lmax1$maximum,lmax2$maximum)
	#text(x=300,y=300,"lambda max = lmax$maximum")
	return(maxes)
	
}




gaussFit4 <- function(df) {
	data.frame(df) -> values
	#normalize to 1
	values$counts<-values$counts/max(values$counts)
	
	#uses least squares to find mean and variance of two Gaussian distributions
	#start is the initial parameter estimates, which sometimes need to change
	#values C1 and C2 are the "height", so normalized to 1 above
	#If "Error in convergence" may need to change the starting values
	fit <- nls(counts ~ (C1 * exp(-(wavelength-mean1)**2/(2 * sigma1**2)) +
	                  C2 * exp(-(wavelength-mean2)**2/(2 * sigma2**2)) + 
	                  C3 * exp(-(wavelength-mean3)**2/(2 * sigma3**2)) +
	                  C4 * exp(-(wavelength-mean4)**2/(2 * sigma4**2))
	                  ), data=values,
					   start=list(C1=.7, 	mean1=480, sigma1=30,
					   	   C2=.5, mean2=490, sigma2=40, 
					   	   C3=.5, mean3=500, sigma3=30, 
					   	   C4=.7, mean4=510, sigma4=40), 
					   	   algorithm="port")

	plot(counts~wavelength, data= values, xlim=c(400,600), ylim=c(0,1.1) )
	v <- summary(fit)$parameters[,"Estimate"]
	F1v <- v
	
    sum <- function(x) F1v[1]*exp(-1/2*(x-F1v [2])^2/F1v[3]^2) + F1v[4]*exp(-1/2*(x-F1v[5])^2/F1v[6]^2) + F1v[7]*exp(-1/2*(x-F1v [8])^2/F1v[9]^2) + F1v[10]*exp(-1/2*(x-F1v[11])^2/F1v[12]^2)
    g1 <- function(x) F1v[1]*exp(-1/2*(x-F1v [2])^2/F1v[3]^2)
    g2 <- function(x) F1v[4]*exp(-1/2*(x-F1v[5])^2/F1v[6]^2)
    g3 <- function(x) F1v[7]*exp(-1/2*(x-F1v [8])^2/F1v[9]^2)
    g4 <- function(x) F1v[10]*exp(-1/2*(x-F1v[11])^2/F1v[12]^2)
    
    #used to combine some but not all gaussians
	#emission <- function(x) F1v[1]*exp(-1/2*(x-F1v [2])^2/F1v[3]^2) + F1v[4]*exp(-1/2*(x-F1v[5])^2/F1v[6]^2)
	#emission2 <- function(x) F1v[7]*exp(-1/2*(x-F1v [8])^2/F1v[9]^2) + F1v[10]*exp(-1/2*(x-F1v[11])^2/F1v[12]^2)
	
	optimize(g1, interval=c(430,550), maximum=TRUE)->lmax1
	optimize(g2, interval=c(430,550), maximum=TRUE)->lmax2
    optimize(g3, interval=c(430,550), maximum=TRUE)->lmax3
    optimize(g4, interval=c(430,550), maximum=TRUE)->lmax4


    plot(sum, col="green",xlim=c(400,600), lwd=5, add=TRUE )
	plot(g1, col=2,xlim=c(400,600), abline(v=lmax1$maximum, col="blue"), add=TRUE )
	plot(g2, col=2,xlim=c(400,600), abline(v=lmax2$maximum, col="blue"), add=TRUE )
	plot(g3, col=2,xlim=c(400,600), abline(v=lmax3$maximum, col="blue"), add=TRUE )
	plot(g4, col=2,xlim=c(400,600), abline(v=lmax4$maximum, col="blue"), add=TRUE )
	
    maxes <- c(lmax1$maximum,lmax2$maximum, lmax3$maximum, lmax4$maximum)
	#text(x=300,y=300,"lambda max = lmax$maximum")
	return(maxes)
	
}

gaussFit <- function(df) {
	data.frame(df) -> values
	#normalize to 1
	values$counts<-values$counts/max(values$counts)
	
	#uses least squares to find mean and variance of two Gaussian distributions
	#start is the initial parameter estimates, which sometimes need to change
	#values C1 and C2 are the "height", so normalized to 1 above
	#If "Error in convergence" may need to change the starting values
	fit <- nls(counts ~ (C1 * exp(-(wavelength-mean1)**2/(2 * sigma1**2)) +
	                  C2 * exp(-(wavelength-mean2)**2/(2 * sigma2**2))), data=values,
					   start=list(C1=.7, 	mean1=480, sigma1=30,
					   	   C2=.5, mean2=490, sigma2=41), algorithm="port")

	plot(counts~wavelength, data= values, xlim=c(400,600), ylim=c(0,1.1) )
	v <- summary(fit)$parameters[,"Estimate"]
	F1v <- v

	emission <- function(x) F1v[1]*exp(-1/2*(x-F1v [2])^2/F1v[3]^2) + F1v[4]*exp(-1/2*(x-F1v[5])^2/F1v[6]^2)
	optimize(emission, interval=c(430,550), maximum=TRUE)->lmax
	plot(emission, col=2,xlim=c(400,600), abline(v=lmax$maximum, col="blue"), add=TRUE )
	text(x=300,y=300,"lambda max = lmax$maximum")
	return(lmax$maximum)
	
}



gaussFitWell <- function(df, well) {
	data.frame(df[df$well==well,3:4]) -> values
	#normalize to 1
	values$counts<-values$counts/max(values$counts)
	
	#uses least squares to find mean and variance of two Gaussian distributions
	#start is the initial parameter estimates, which sometimes need to change
	#values C1 and C2 are the "height", so normalized to 1 above
	#If "Error in convergence" may need to change the starting values
	fit <- nls(counts ~ (C1 * exp(-(wavelength-mean1)**2/(2 * sigma1**2)) +
	                  C2 * exp(-(wavelength-mean2)**2/(2 * sigma2**2))), data=values,
					   start=list(C1=.7, 	mean1=480, sigma1=30,
					   	   C2=.5, mean2=490, sigma2=41), algorithm="port")

	plot(counts~wavelength, data= values, xlim=c(400,600), ylim=c(0,1.1) )
	v <- summary(fit)$parameters[,"Estimate"]
	F1v <- v

   	emission <- function(x) F1v[1]*exp(-1/2*(x-F1v [2])^2/F1v[3]^2) + F1v[4]*exp(-1/2*(x-F1v[5])^2/F1v[6]^2)
	optimize(emission, interval=c(430,550), maximum=TRUE)->lmax
	plot(emission, col=2,xlim=c(400,600),main=well, abline(v=lmax$maximum, col="blue"), add=TRUE )
	text(x=300,y=300,"lambda max = lmax$maximum")
	return(lmax$maximum)
	
}
#convert from wavelengths to energy (frequency)
lam2freq <- function(df) {
	data.frame(df) -> values
	lightspeed = 299792458
	values$wavelength <- lightspeed/(values$wavelength/1000)
	return(values)
}
#Function to simply plot the data from a well
plotWell <- function(df, well) {
	data.frame(df[df$well==well,3:4]) -> values
	#normalize to 1
	values$counts<-values$counts/max(values$counts)
	plot(counts~wavelength, data= values, xlim=c(400,600), ylim=c(0,1.1), main=well )	
}
#**********************************************************
#Main 
#Read QEPro file
read.table(file="P11-Ppg_AbsoluteIrradiance_20-29-54-361.txt", sep="\t") -> P11
colnames(P11) <- c("wavelength", "counts")
lam2freq(P11) -> fP11
head(fP11)

gaussFit4(P11)


#Read all the C. noctiluca data and analyze each well
read.csv(file="Cnoc_emission_12302021.csv") -> allcnoc
gaussFitWell(allcnoc,"F1")
gaussFitWell(allcnoc,"F2")
gaussFitWell(allcnoc,"F3")

read.csv(file="12302021_WLUOP_emission.csv") -> allwlu
#First the paralog data
gaussFitWell(allwlu,"A12")
gaussFitWell(allwlu,"B12")
gaussFitWell(allwlu,"C12")

#Next the ortholog data
plotWell(allwlu,"F12") #This doesn't converge. I think there is mainly noise due to the small amount of light
gaussFitWell(allwlu,"G12")
gaussFitWell(allwlu,"H12")





