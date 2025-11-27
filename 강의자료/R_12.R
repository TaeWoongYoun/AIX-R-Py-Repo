d <- data.frame(x=c(1, 2, 3, 4, 5),
                y=c(2, 4, 6, 8, 10),
                z=c('M', 'F', 'M', 'F', 'M'))
d$x
# 새로 변수를 Assign 하는 방법 
d$x <- 6:10
#변수 내용을 바꾸는 것 
d[3,1]=100
d[3,"y"]=100  
d
d$w <- c("A", "B", "C", "D", "E")

str(d) # python info

colnames(d)=c("영희","철수","민수")
d[,"영희"]
rownames(d)


d <- data.frame(x=c(1, 2, 3, 4, 5), y=c(2, 4, 6, 8, 10))
d$x
d[1, ]
d[1, 2]

d[c(1, 3), 2]
d[-1, -2]
d[, c("x")]


data(USArrests)
help(USArrests)

USArrests
head(USArrests,3)
head(USArrests,-1) # 마지막 1빠짐
tail(USArrests,-1) # 최초행 빠짐 
tail(USArrests,-c(1,2)) # 쵱초 두행 빠짐 

# 정렬

nidx <- order(USArrests$Murder, decreasing=T)[1:5]
nidx

USArrests[nidx,]

lidx <- (USArrests$Murder < quantile(USArrests$Murder, 0.1))

head(lidx, 10)
USArrests[ lidx,]
quantile(USArrests$Murder)
fivenum(USArrests$Murder)

x <- data.frame(id=c(1, 2), name=c("a", "b"), stringsAsFactors=F)
x
z<- data.frame(id=c(3), name=c("c"), stringsAsFactors=F)
z1<- data.frame(ids=c(3), name=c("c"), stringsAsFactors=F)

y<-rbind(x,z) # 이름이 같으니 되고 
y<-rbind(x,z1) # 이름이 다르니 안되고 
y
y <- rbind(x, c(3, "c"))
y
# 데이터 프레임 쪼개기-> 그룹별로 쪼갠다. 
iris
str(iris)
split(iris,iris$Species)

lapply(split(iris$Sepal.Length, iris$Species), mean)
# filter하고Select 하는 명령어 
subset(USArrests, UrbanPop > 85)
subset(USArrests, UrbanPop > 85,Murder)

subset(USArrests, UrbanPop < 40 &  Murder < 10, select = c(Assault, Rape))



authors <- data.frame(
  surname = c("Tukey", "Venables", "Tierney", "Ripley", "McNeil"),
  nationality = c("US", "Australia", "US", "UK", "Australia")   )
books <- data.frame(
  name = c("Tukey", "Venables", "Tierney",
           "Ripley", "Ripley", "McNeil", "R Core"),
  title = c("Exploratory Data Analysis",
            "Modern Applied Statistics ...",
            "LISP-STAT",
            "Spatial Statistics", "Stochastic Simulation",
            "Interactive Data Analysis",
            "An Introduction to R"))

authors
books
m1 <- merge(authors, books, by.x = "surname", by.y = "name")
m1
m1 <- merge(books, authors, by.x = "name", by.y = "surname")
m1

m1 <- merge(authors, books, by.x = "surname", by.y = "name")
m1 <- merge(authors, books, by.x = "surname", by.y = "name",all.y=T)
m1
authors

# 변수 생성 
# 변수 정렬
# 필터 
# 고르기 
# 피버팅
# 머징 

install.packages("dplyr")
library(dplyr) # x특수기호 control+shift+M
iris_sub=iris %>% mutate(Sepal.LW=Sepal.Length+Sepal.Width) %>% 
  arrange(Sepal.Length, Petal.Length)  %>% 
  filter(Sepal.Length>6)%>% 
  select(Species,Sepal.LW)

iris_pivot <- iris %>%
  group_by(Species) %>%
  summarise(
    Count = n(),                      # 데이터 개수
    Mean = mean(Sepal.Length),         # 평균
    Median = median(Sepal.Length),     # 중앙값
    SD = sd(Sepal.Length),             # 표준편차
    Min = min(Sepal.Length),           # 최소값
    Max = max(Sepal.Length),           # 최대값
    Range = Max - Min,                 # 범위
    IQR = IQR(Sepal.Length)            # 사분위 범위
  )


iris_pivot

iris[which(iris$Species == "setosa"),]
iris[which.min(iris$Sepal.Length),]
which.max(iris$Sepal.Length)
aggregate(Sepal.Length~Species, data=iris, FUN=mean)


attach(iris)
Sepal.Length
Sepal.Width
detach(iris)
Sepal.Length

iris[,1:4]
apply(iris[,1:4],1,sum)
apply(iris[,1:4],2,sum)
apply(iris,2,sum)

iris %>%
  select_if(is.numeric) %>%  # 숫자형 칼럼만 선택
  apply(2, sum)        
iris %>%
  mutate(Row_Sum = apply(select_if(., is.numeric), 1, sum))


d <- matrix(1:9, ncol=3, nrow=3)
d
apply(d, 1, sum)
apply(d, 2, sum)
apply(iris, 2, mean,na.rm=T)
x <- list(a=1:3, b=4:8)
lapply(x, mean)

lapply(iris[, 1:4], mean)


f <-function(c,d){
  z=mean(c)
  z=z+d
}

unlist(lapply(iris[, 1:4],f,d=1))
sapply(iris[, 1:4], mean)
y <- sapply(iris[, 1:4], function(x) { x > 3 })
iris4=iris[,1:4]
iris4[y]
tapply(iris$Sepal.Length, iris$Species, mean)
m <- matrix(1:8,ncol=2,nrow=4,dimnames=list(c("spring", "summer", "fall", "winter"),c("male", "female")))

# 인덱싱 2차원 가능 
tapply(m, list(c(1, 1, 2, 2, 1, 1, 2, 2), c(1, 1, 1, 1, 2, 2, 2, 2)), sum)


mapply(rnorm,
       c(1, 2, 3),     # n
       c(0, 10, 100),  # mean
       c(1, 1, 1))     # sd


for (ii in 1:3){
  
  A=c(1, 2, 3)     # n
  B=c(0, 10, 100)  # mean
  C=c(1, 1, 1)
  print(rnorm(A[ii],B[ii],C[ii]))

}

df=data.frame(mean=c(1,100,200),sd=c(1,1,1))

rNum<-function(mean,sd){
  rnums=rnorm(2,mean,sd)
  rnum=list()
  rnum$r1=rnums[1]
  rnum$r2=rnums[2]
  return(rnum)
}
temp=mapply(rNum,df$mean,df$sd)

temp
cbind(df,t(temp))





