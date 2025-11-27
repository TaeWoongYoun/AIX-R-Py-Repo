x <- c(1, 2, 3, 4, 5)-3
# ifelse -> inline if statement 
ifelse(x %% 2 == 0, "even", "odd")
ifelse(x>0,"positive",ifelse(x==0,"zero","negative"))


d <- data.frame(x=c(1, 2, 3, 4, 5), y=c("a", "b", "c", "d", "e"))
d[c(TRUE, FALSE, TRUE, FALSE, TRUE), ]


# NA 연산 
NA & TRUE
NA + 1
sum(c(1, 2, 3, NA)) # na에 무엇인가 연산이 있으면 대다수의 경우에는 NA를 return
sum(c(1, 2, 3, NA), na.rm=TRUE) #표준적인 문법 


(x <- data.frame(a=c(1, 2, 3), b=c("a", NA , "c"), c=c("a", "b", NA)))

x
na.fail(x)     # NA가 포함되어 있으므로 실패
na.omit(x)     # NA가 포함된 행을 제외
na.exclude(x)  # NA가 포함된 행을 제외
na.pass(x)     # NA의 여부에 상관없이 통과

x=c(1,2,3) 
y=c(-1,3,2)

max(x,y) # 다모아서 가장큰에 -> 벡터화된 연산 안함 
pmax(x,y) # 벡터화된 최대치 연산 

cumsum(x)
cummax(y)
cumprod(x)

# R의 연산들 
a <- 1:5
sqrt(a)
exp(a)

out <- (a + sqrt(a))/(exp(2)+1)
out

x1 <- seq(-2, 4, by = .5)
x1
floor(x1)
a <- c(1,-2,3,-4)
b <- c(-1,2,-3,4)
min(a,b)
pmin(a,b)

# if-elseif 

height=151
# 블록 지정은 중괄호-> Python :, 들여쓰기 
# 괄호로 조건임을 표시 
# Python은 elif -> elseif 
if (height>170) {
print("Tall")
  print("name")
} else if (height> 160) { 
  print("Medicore 1")
}else {
  print("Medicore 2")
}


# Create vector quantity
quantity <-  25
# Set the is-else statement
if (quantity > 20) {
  print('You sold a lot!')
} else {
  print('Not enough for today')  
}


# Create vector quantiy
quantity <-  25
# Create multiple condition statement
if (quantity <20) {
  print('Not enough for today')
} else if (quantity > 20  &quantity <= 30) {
  print('Average day')
} else {
  print('What a great day!')
}

# Create fruit vector
fruit <- c('Apple', 'Orange', 'Passion fruit', 'Banana')
# Create the for statement
# Enumerate는 없다, Zip 기능 없음 
for ( i in fruit){ 
  print(i)
}

for ( i in seq(1,4)){ 
  print(fruit[i])
}

x<-matrix(1:6,2,3)
x
for ( i in 1:2){
  for (j in 1:3) {
    print(x[i,j])
  }
}


# Create a list with three vectors
fruit <- list(Basket = c('Apple', 'Orange', 'Passion fruit', 'Banana'), 
              Money = c(10, 12, 15), purchase = FALSE)
ii=0
# Python에서는 안되나 R에서는 허용 
for (p  in fruit){ 
              print(p)
  print(ii)
  ii=ii+1
}


z<-1 # initial value 
# 조건에 대해서는 반드시괄호 표시 
while(z>=3 & z<=10){
  print(z)
  coin<-rbinom(1,1,0.5) # draw 0 or 1 with 50% chance
  
  if(coin==1){
    z<-z+1
  } else {
    z<-z-1
  }
}


z<-5 # initial value 

repeat {
  print(z)
  coin<-rbinom(1,1,0.5) # draw 0 or 1 with 50% chance
  if(coin==1){
    z<-z+1
  } else {
    z<-z-1
  }
  if (!(z>=3 && z<=10)) {
    break
  }
}


z=5
for (ii in seq(100)) {
  print(z)
  coin<-rbinom(1,1,0.5) # draw 0 or 1 with 50% chance
  if(coin==1){
    z<-z+1
  } else {
    z<-z-1
  }
  if (!(z>=3 && z<=10)) {
    break
  }
}

# next는 continue 
# colon operation이 좀 다르다: R은 마지막 포함, python은 미포함 
for (i in 1:22) {
  if(i<=20){
    next
    ## Skip initial 20 iterations
  }
  print(i)
  
}

# 오류코드 
pm<-function(a,b){
  p=a+b
  m=a-b
  return(p,m)
  
}

pm(3,5)

# list로 return 값을 모아 반환 -> 대체불가특징 
pm<-function(a,b){
  p=a+b
  m=a-b
  result= list(p=p,m=m)
  return(result)
  
}
result=pm(3,5)
str(result)
result$p


iris
result_lm=lm("Sepal.Length~ Petal.Length",data=iris)
str(result_lm)
result_lm$qr


f1 <- function(num) {
  for(i in seq_len(num)) {
    cat("Hello, world!\n")
  }
}
f1(2)
f1(10)
# 디폴트 값 
f1 <- function(num=3) {
  for(i in seq_len(num)) {
    cat("Hello, world!\n")
  }
}
f1()


add2<-function(a,b){
  print(a+b)
  a-b
}
mi=add2(3,2)
mi=add2(3,2)
mi

# Explicit 하게 Return값을 써주는 것이 바람직함 
add2<-function(a,b){
  print(a+b)
  return(a-b)
}

mi=add2(3,2)
mi



add4<-function(a,b) {
  print(2*a-b)
}  


add4(2,1)

add4(1,2)

add4(b=1,a=2)


n <- 1
f <- function() {
  print(n)
}

n <- 1
f <- function() {
  print(n)
  n=n+1 # 파이썬에서는 불가, R에서는 고칠수는 있으나 local 변수
  # 즉 밖에 Global 환경 변수값에 영향을 미치지는 않는다. 
  print(n)
}
f()
n

rm(list=ls()) # 다지우기 

f <- function() {
  n <- 1 #함수안에 변수는 로컬 
}
n

n <- 100
f <- function() {
  n <- 1
  print(n)
}
f()
n



# 전역 변수 정의
global_var <- 5

# 함수에서 전역 변수 수정
# 바꾸는게 좋으냐? 아니요 
# 바꿀수 있느냐? YES 
modify_global_var <- function() {
  global_var <<- 10  # 전역 변수의 값을 10으로 변경
}
modify_global_var()
global_var

# 변수명을 새로이 지정하며 바꾸기 
# 좋은 기능 
names=c("영희","철호","민호")

for (ii in names){
  z=ii
  print(ii)
}
rm(list=ls())
vars=c("var1","var2","var3")
var1
for (ii in vars){
assign(ii, rnorm(1)) 
}
var1
var2

