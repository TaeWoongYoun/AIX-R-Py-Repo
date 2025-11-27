install.packages("dplyr")
library(dplyr)
high_mpg <- mtcars[mtcars$mpg >= 15, ]
low_mpg <- mtcars[mtcars$mpg < 15, ]
summary(mtcars)
summary(high_mpg)
summary(low_mpg)
model1 <- lm(mpg ~ cyl, data = mtcars)
summary(model1)
model2_high <- lm(mpg ~ cyl, data = high_mpg)
summary(model2_high)
model2_low <- lm(mpg ~ cyl, data = low_mpg)
summary(model2_low)
summary(model1)$r.squared
summary(model2_high)$r.squared
summary(model2_low)$r.squared
model3 <- lm(mpg ~ cyl + gear, data = mtcars)
summary(model3)
mtcars$gear_factor <- as.factor(mtcars$gear)
str(mtcars)
model4 <- lm(mpg ~ cyl + gear_factor, data = mtcars)
summary(model4)
# =============================================================================
# 1-2 제출자료 출력
# =============================================================================
summary(mtcars)
summary(high_mpg)
summary(low_mpg)
# =============================================================================
# 1-3 제출자료 출력
# =============================================================================
apply(mtcars[, 1:11], 2, mean)
apply(mtcars, 2, sd)
apply(high_mpg, 2, mean)
apply(high_mpg, 2, sd)
apply(low_mpg, 2, mean)
apply(low_mpg, 2, sd)
# =============================================================================
# 1-4 제출자료 출력
# =============================================================================
summary(model1)
# =============================================================================
# 1-5 제출자료 출력
# =============================================================================
summary(model2_high)
summary(model2_low)
summary(model1)$r.squared
summary(model2_high)$r.squared
summary(model2_low)$r.squared
# =============================================================================
# 1-6 제출자료 출력
# =============================================================================
summary(model3)
# =============================================================================
# 1-7 제출자료 출력
# =============================================================================
str(mtcars)
# =============================================================================
# 1-8 제출자료 출력
# =============================================================================
summary(model4)
# =============================================================================
# 과제2 시작
# =============================================================================
set.seed(123)
S0 <- 100
days <- 30
sigma <- 0.1
rf <- 0.04
N <- 10000
dt <- 1/250
result <- numeric(N)
for (i in 1:N) { S <- S0; for (j in 1:days) { eps <- rnorm(1); S <- S * exp((rf - 0.5 * sigma^2) * dt + sigma * sqrt(dt) * eps) }; result[i] <- S }
mean(result)
var(result)
hist(result, breaks = 50, main = "ST Distribution (T=30, N=10000)", xlab = "Stock Price", col = "lightblue")
