#ctrl + enter
a<-c(1,2,3,4)
b<-c(2,3,4,5)
a+b
c=matrix(c(1,2,3,4),nrow=2,ncol=2)
c
t(c)
sin(c)

#ctrl + enter
a<-c(1,2,3,4)
b<-c(2,3,4,5)
d<-c("영희","철수","영수","민희")
# 데이터 프레임이 기본 
df=data.frame(a=a,b=b,이름=d)
df["이름"]
df$이름
# 이름과 숫자인덱스 혼용이 가능 
rownames(df)=c("관측1","관측2","관측3","관측4")
df["관측1", c(2,3)]
df[c(2,3),c("b","이름")]

# 벡터 및 행렬 이름 부가 가능 
names(a)=c("관측1","관측2","관측3","관측4")
a
c=matrix(c(1,2,3,4),nrow=2,ncol=2)
c
t(c)
sin(c)

# 인덱스는 1부터 시작 
c
c[c(1,2),2]

# reverse indexing 안됨 
df
df[-3,] # 3번행행 전체 제외 

# linear Regression 
lm("Sepal.Length~Petal.Length+Sepal.Width+Species",data=iris)

b_vec=c(T,F,F,T)
v_vec<-c(2,3)
v_vec
v_vec=c(3,4)
v_vec

c(5,4) -> v_vec
v_vec

apple <- c('red','green',"yellow")
print(apple)

class(apple)
class(a)
class(df)
list1 <- list(c(2,5,3), 21.3,sin)
M = matrix(c('a','a','b','c','b','a'),nrow = 2, ncol = 3,byrow = TRUE )
M = matrix(c('a','a','b','c','b','a'),nrow = 2, ncol = 3)
M


x <- array(1:12, dim=c(2, 2, 3))
x
x[1, 1, 1]
x[1, 2, 3]
x[, , 3]
dim(x)


# 벡터 만들기
apple_colors <- c('green', 'green', 'yellow', 'red', 'red', 'red', 'green')

# 팩터 객체 만들기
factor_apple <- factor(apple_colors)

# 팩터 출력하기
print(factor_apple)

# nlevels 함수를 사용하여 서로 다른 값의 개수를 알 수 있음
print(nlevels(factor_apple))

# 데이터 프레임 만들기
BMI <- data.frame(
  gender = c("Male", "Male","Female"),  height = c(152, 171.5, 165), 
  weight = c(81,93, 78), Age = c(42,38,26) )
print(BMI)




# -----------------------------
# (1) 팩터(Factor) 예제
# -----------------------------

# 결측치가 포함된 벡터 생성
x <- c(1, 2, NA, 3)
y <- c(1, NA, 3, 4)

# 결측치가 없는 위치(TRUE/FALSE)
good <- complete.cases(x, y)
print(good)

# 결측치가 없는 값만 추출
print(x[good])
print(y[good])

# -----------------------------
# (3) 데이터 프레임 예제
# -----------------------------

# 데이터 프레임 생성
df <- data.frame(x = x, y = y)

# 결측치가 없는 행만 선택
clean_df <- df[complete.cases(df), ]
print(clean_df)

seq(1,5,2)

df
df[1:3,]

rep(1:2, times=5)
rep(1:2, each=5)
rep(1:2, each=5,times=5)
rep(1:2,times=5,  each=5)
str(iris) # pandas로 본다면 info 

x<-c("a","b","c")
x[1]
x[1:2]
x<-list(foo=1:4, bar=0.6, bax="hello")
# 동일형태 반환 
x[1]
x[2]
x[3]
class(x["foo"])
class(x[1])
x[c(1,3)]

# 벡터형태로 반환
x[[1]]
x$foo # 이쪽이 선호

class(x$foo)
class(x[[1]])
x[[c(1,4)]]
x[[1]][[3]]
x<-matrix(1:12,4,3)
x[4,3]
x[,2] #칼럼벡터 안ㅁ
x[,2,drop=F] # 칼럼벡터

x<-c(1,2,3,4)
y=c(3,4,5,6) # 혼용 가능
x*y
x/y
x>=2
identical(c(1, 2, 3), c(1, 2, 3))
identical(c(1, 2, 3), c(1, 2, 4))
"a" %in% c("a", "b", "c") # in 연산의 모양이 다름 
"d" %in% c("a", "b", "c")

a=matrix(c(1,2,3,4),2,2)
b=matrix(c(5,6,7,8),2,2)
a
b
a*b # element wise 곱
a%*%b

x^2 # 제곱항은 파이썬과 차이, 그러나 element-wise 연산이란것은 변함없다

x <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow=3)
x * 2
x/2
x + x
x - x
x*x
x%*%x # 행렬곱, 내적
t(x)

#특징적 측면:propagation 
x=c(1,2,3,4)
y=c(3,4)
x+y # 수리적으로는 안되야 되나-> 차원이 안맞으니 
    # 실제로는 된다 -> 연산때 주의해야 한다 


# 연산이 직관적인 측면이 있다. 
log(x)
exp(x)
cos(x)

iris
write.csv(iris,"iris.csv",row.names=F)
getwd()
rm(list=ls())

df=read.csv("iris.csv")
df
dfs=df[df$Sepal.Length>5,1:2]*3
write.csv(dfs,"iris_sub.csv",row.names=F)
#추가적인 내용 
install.packages("dplyr") # python pip install
library(dplyr) # python import 
df %>% filter(Sepal.Length<10) %>% group_by(Species) %>% 
  summarize(mean_sepal=mean(Sepal.Length)) 

