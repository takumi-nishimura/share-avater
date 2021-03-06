library(openxlsx)
library(ggpubr)
library(rstatix)
library(ggplot2)
library(gridExtra)
library(outliers)

setwd('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Test')
source('/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/Test/anovakun_450.txt')

filename <- '/Users/sprout/OneDrive - 名古屋工業大学/学校/研究室/code/ExData/Processing/graduated/Mean_Q4.xlsx'
str(filename)
dat <- read.xlsx(filename)
shapiro <- tapply(dat$Score,dat$Condition,shapiro.test)
print(shapiro)

woFB <- dat[dat$Condition=='without feedback',]$Score
pV <- dat[dat$Condition=='partner velocity',]$Score
rV <- dat[dat$Condition=='robot velocity',]$Score

data <- matrix(c(woFB,pV,rV),ncol=3)
print(data)
columns = c('without', 'partner_vel', 'robot_vel')

if (shapiro[["partner velocity"]][["p.value"]]<0.05
  |shapiro[["robot velocity"]][["p.value"]]<0.05
  |shapiro[["without feedback"]][["p.value"]]<0.05){

friedman.test(data)
} else {
  layout(t(1:3))
  qq <- tapply(dat$Score,dat$Condition,qqnorm)

  bartlett <- bartlett.test(dat$Score ~ dat$Condition)
  print(bartlett)

  result_anovakun = anovakun(data, "sA", A=columns, holm=T, peta=T)
}