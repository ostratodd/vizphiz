library(phytools)
library(phangorn)

setwd("~/Documents/GitHub/vizphiz/")
read.csv(file="trees/het_ymax.csv", row.names=1, header=FALSE) -> ymax
read.tree(file="trees/het_ALN.fas.treefile") -> tree
read.nexus(file="trees/rooted.tre") -> tree

x <-svl<-as.matrix(ymax)[,1]

#x<-fastBM(tree, a=100, sig2=50)

leaveout <- 1
all <- c() # initialize for imputed results
for(i in 1:2) {
    xp <- as.matrix(x)
    xp[cbind(sample(1:nrow(as.matrix(xp)), leaveout), sample(1,leaveout,replace=TRUE))]<-NA
    xp
    xpt <- as.matrix(xp)[,1]
    xpt
    
    fit<-anc.ML(tree,na.omit(xpt))
    fit

    impute <- as.matrix(fit$missing.x)
    #find row for missing data to obtain actual data
    as.matrix(x[which(is.na(xp))]) -> actual
    cbind(actual[,1], impute[,1])->rep
    print(rep)
    all <- rbind(all,rep)
}


plot(all[,1], all[,2], ,pch=21,bg="grey",cex=1.5,
    xlab="true values of rod lambda max",ylab="imputed values using phylo.impute",asp=1)



phenogram(tree,x,fsize=0.3)
nodelabels(node=tips,pie=rep(1,length(fit$missing.x)),
    cex=0.5)   

contMap(tree,x,plot=TRUE, plot.tip.labels=FALSE,fsize=.5)