library(tidyr)
data.matrix = matrix(nrow = 100,ncol = 10)
colnames(data.matrix) = c(paste("wt",1:5,sep=""),paste("ko",1:5,sep=""))
for (i in 1:100) {
    wt.values = rpois(5,lambda=sample(10:1000, 1))
    ko.values = rpois(5,lambda=sample(10:1000, 1))
    data.matrix[i,] = c(wt.values,ko.values)
}
data.matrix %>% head(10)

pca = prcomp(t(data.matrix),scale=T)

plot(pca$x[,1],pca$x[,2])
pca.var = pca$sdev^2
plot.var.per = round(pca.var/sum(pca.var)*100,2)
barplot(plot.var.per,col=c("red","blue"))
library(ggplot2)
scores = abs(pca$rotation[,1] )
scores_rank = order(scores,decreasing=T)
top_10_scores = names(scores_rank[1:10])
