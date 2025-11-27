x <- 1:6                      # 가능한 값
pmf <- rep(1/6, 6)            # 각 값의 확률
pmf
barplot(pmf, names.arg = x,
        main = "주사위 확률밀도함수 (PMF)",
        xlab = "주사위 눈",
        ylab = "P(X = x)",
        col = "skyblue")

cdf <- cumsum(pmf)            # 누적합
cdf



# 1. 표준정규분포의 값 생성 (z 값 범위)
z <- seq(-4, 4, length = 200)  # -4부터 4까지의 구간을 200개 값으로 나눔

# 2. 확률밀도함수(PDF) 계산
pdf_values <- dnorm(z)  # PDF 값 계산

# 3. 누적분포함수(CDF) 계산
cdf_values <- pnorm(z)  # CDF 값 계산

# 4. PDF와 CDF 그래프 동시에 그리기
par(mfrow = c(1, 2))  # 두 개의 그래프를 가로로 배치

# PDF 그래프
plot(z, pdf_values, type = "l", col = "blue", lwd = 2,
     main = "표준정규분포 확률밀도함수 (PDF)",
     xlab = "z", ylab = "f(z)")

# CDF 그래프
plot(z, cdf_values, type = "l", col = "red", lwd = 2,
     main = "표준정규분포 누적분포함수 (CDF)",
     xlab = "z", ylab = "F(z)")

# 5. 임의의 z 값에서 PDF, CDF 값 계산
z_value <- 1.96  # 예시로 z = 1.96을 선택
pdf_at_z <- dnorm(z_value)  # z = 1.96에서의 PDF
cdf_at_z <- pnorm(z_value)  # z = 1.96에서의 CDF

# 출력
cat("z =", z_value, "에서 PDF =", pdf_at_z, "\n")
cat("z =", z_value, "에서 CDF =", cdf_at_z, "\n")


plot(x, cdf, type = "s",
     main = "주사위 누적분포함수 (CDF)",
     xlab = "주사위 눈",
     ylab = "P(X ≤ x)",
     col = "red", lwd = 2)
points(x, cdf, pch = 16, col = "red")







# 1. 표준정규분포로부터 난수 생성 (n = 10000개 샘플)
n <- 10000
simulated_data <- rnorm(n)  # 평균 0, 표준편차 1인 표준정규분포에서 10000개 샘플 생성

# 2. 히스토그램으로 샘플 분포 확인
hist(simulated_data, probability = TRUE, col = "skyblue", border = "white",
     main = "표준정규분포 근사 (rnorm 시뮬레이션)",
     xlab = "z", ylab = "밀도", breaks = 30)

# 3. 이론적인 PDF와 비교
z <- seq(-4, 4, length = 200)
lines(z, dnorm(z), col = "red", lwd = 2)  # 표준정규분포의 이론적인 PDF

# 4. 이론적인 CDF와 비교
# 시뮬레이션된 데이터에 대한 CDF 계산
simulated_cdf <- ecdf(simulated_data)

# 5. CDF 그래프 그리기
plot(simulated_cdf, main = "표준정규분포 CDF와 시뮬레이션 CDF 비교",
     xlab = "z", ylab = "F(z)", col = "blue", lwd = 2)
lines(z, pnorm(z), col = "red", lwd = 2)  # 이론적인 CDF

# 6. 평균과 표준편차 계산 (시뮬레이션 데이터)
mean_sim <- mean(simulated_data)
sd_sim <- sd(simulated_data)

cat("시뮬레이션된 데이터의 평균: ", mean_sim, "\n")
cat("시뮬레이션된 데이터의 표준편차: ", sd_sim, "\n")



rnorm(1, 100, 16) # 평균이 100이고 표준편차가 16인 정규분포에서 1개 난수 발생
rnorm(5, mean = 280, sd = 10) # 평균이 280이고 표준편차가 10인 정규분포에서 5개 난수 발생

pnorm(265.5393, mean = 280, sd = 10) 
# 평균이 280이고 표준편차가 10인 분포에서 X <= 295.5393의 확률

qnorm(0.05, mean = 0, sd = 1) # 평균이 0이고, 표준편차가 1인 분포에서 누적확률이 0.05인 x
qnorm(0.95, mean = 0, sd = 1) # 평균이 0이고, 표준편차가 1인 분포에서 누적확률이 0.95인 x
qnorm(0.975, mean = 0, sd = 1) # 평균이 0이고, 표준편차가 1인 분포에서 누적확률이 0.975인 x

dnorm(0, mean = 0, sd = 1) # 평균이 0이고, 표준편차가 1인 분포에서 x = 0의 확률


dunif(0.5, min = 0, max = 2) # 최소값 0, 최대값 2인 균일분포에서 x = 0.5의 확률
punif(0.5, min = 0, max = 2) # 최소값 0, 최대값 2인 균일분포에서 x <= 0.5의 누적확률분포
punif(0.5, min = 0, max = 2, lower.tail = TRUE) 
qunif(0.5, min = 0, max = 2) # 최소값 0, 최대값 2인 균일분포에서 누적확률이 0.5인 x값



rnorm(3,0,1)
rnorm(3,0,1)

set.seed(10)   # 정수값 설정
rnorm(3,0,1)
rnorm(3,0,1)

set.seed(10) #  같은 정수값 설정
rnorm(3,0,1)
rnorm(3,0,1)

set.seed(10) #  같은 정수값 설정
mean(rnorm(100,0,1))
mean(rnorm(100,0,1))


sample(5, replace=TRUE) # 복원 추출
sample(5, replace=F) # 비복원 
# 시드값의 역할 
set.seed(10) 
sample(5, replace=TRUE) # 복원 추출
sample(5, replace=F) # 비복원 

set.seed(10) 
sample(5, replace=TRUE) # 복원 추출
sample(5, replace=F) # 비복원 



x <- (1:10) * 10
x[sample(length(x))]
sample(x,5)
sample(x,5,replace=T)
sample(x,5,replace=T)
y=seq(5)
 table(sample(y, 10000, replace=TRUE, prob=c(0.1, 0, 0.3, 0.6, 0)))

 
 # Random Number Generation
 x<-rnorm(100)
 e<-rnorm(100,0,2)
 
 # b values
 b0<-0.5
 b1<-2
 
 y<-b0+b1*x+e
 plot(x,y)
 summary(y)
 
getwd()
read.csv("iris_sub.csv")
read.csv("iris_sub2.csv")
read.csv("./new/iris_sub2.csv")



install.packages("ggplot2")
library(ggplot2)

iris
ggplot(data=iris,aes(x=Sepal.Length,y=Sepal.Width,pch=Species,color=Species))+
  geom_point(size=4)+ggtitle("IRIS: 산포도")+xlab("꽃받침의 길이")+ylab("꽃받침의 너비")

library(ggplot2)

# ggplot 코드: 세련된 산포도 만들기
ggplot(data = iris, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  geom_point(aes(shape = Species), size = 4, alpha = 0.7) +  # 점 크기, 투명도 설정
  scale_shape_manual(values = c(16, 17, 18)) +  # 서로 다른 모양으로 표시
  scale_color_manual(values = c("royalblue", "darkorange", "forestgreen")) +  # 색상 지정
  theme_minimal() +  # 미니멀한 배경
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),  # 제목 설정
    axis.title = element_text(size = 12, face = "bold"),  # 축 제목 설정
    axis.text = element_text(size = 10),  # 축 레이블 설정
    legend.title = element_text(size = 12, face = "bold"),  # 범례 제목 설정
    legend.text = element_text(size = 10)  # 범례 항목 설정
  ) +
  ggtitle("IRIS: 꽃받침의 길이와 너비 산포도") +  # 제목 추가
  xlab("꽃받침의 길이 (Sepal Length)") +  # x축 제목
  ylab("꽃받침의 너비 (Sepal Width)")  # y축 제목

library(ggplot2)
library(RColorBrewer)  # RColorBrewer 패키지 사용

# ggplot 코드: 세련된 산포도 만들기
ggplot(data = iris, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  geom_point(aes(shape = Species), size = 4, alpha = 0.9) +  # 점 크기, 투명도 설정
  scale_shape_manual(values = c(16, 17, 18)) +  # 서로 다른 모양으로 표시
  scale_color_manual(values = c("#1f77b4", "#ff7f0e", "#2ca02c")) +  # 선명한 색상 사용
  theme_minimal() +  # 미니멀한 배경
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),  # 제목 설정
    axis.title = element_text(size = 12, face = "bold"),  # 축 제목 설정
    axis.text = element_text(size = 10),  # 축 레이블 설정
    legend.title = element_text(size = 12, face = "bold"),  # 범례 제목 설정
    legend.text = element_text(size = 10)  # 범례 항목 설정
  ) +
  ggtitle("IRIS: 꽃받침의 길이와 너비 산포도") +  # 제목 추가
  xlab("꽃받침의 길이 (Sepal Length)") +  # x축 제목
  ylab("꽃받침의 너비 (Sepal Width)")  # y축 제목


library(ggplot2)
library(RColorBrewer)  # RColorBrewer 패키지 사용

# ggplot 코드: 세련된 산포도 만들기
ggplot(data = iris, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  geom_point(aes(shape = Species), size = 4, alpha = 0.9) +  # 점 크기, 투명도 설정
  scale_shape_manual(values = c(16, 17, 18)) +  # 서로 다른 모양으로 표시
  scale_color_manual(values = c("#1f77b4", "#ff7f0e", "#2ca02c")) +  # 선명한 색상 사용
  theme_minimal() +  # 미니멀한 배경
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),  # 제목 설정
    axis.title = element_text(size = 12, face = "bold"),  # 축 제목 설정
    axis.text = element_text(size = 10),  # 축 레이블 설정
    legend.title = element_text(size = 14, face = "bold"),  # 범례 제목 크기 조정
    legend.text = element_text(size = 12),  # 범례 항목 텍스트 크기 조정
    legend.key.size = unit(1.5, "cm"),  # 범례 키(색상 박스) 크기 조정
    legend.key.width = unit(1, "cm")  # 범례 키의 가로 크기 조정
  ) +
  ggtitle("IRIS: 꽃받침의 길이와 너비 산포도") +  # 제목 추가
  xlab("꽃받침의 길이 (Sepal Length)") +  # x축 제목
  ylab("꽃받침의 너비 (Sepal Width)")  # y축 제목


library(ggplot2)

# ggplot 코드: 붉은 계열 색상으로 세련된 산포도 만들기
ggplot(data = iris, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  geom_point(aes(shape = Species), size = 4, alpha = 0.9) +  # 점 크기, 투명도 설정
  scale_shape_manual(values = c(16, 17, 18)) +  # 서로 다른 모양으로 표시
  scale_color_manual(values = c("#d62728", "#ff6347", "#ff4500")) +  # 붉은 계열 색상 사용
  theme_minimal() +  # 미니멀한 배경
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),  # 제목 설정
    axis.title = element_text(size = 12, face = "bold"),  # 축 제목 설정
    axis.text = element_text(size = 10),  # 축 레이블 설정
    legend.title = element_text(size = 14, face = "bold"),  # 범례 제목 크기 조정
    legend.text = element_text(size = 12),  # 범례 항목 텍스트 크기 조정
    legend.key.size = unit(1.5, "cm"),  # 범례 키(색상 박스) 크기 조정
    legend.key.width = unit(1, "cm")  # 범례 키의 가로 크기 조정
  ) +
  ggtitle("IRIS: 꽃받침의 길이와 너비 산포도") +  # 제목 추가
  xlab("꽃받침의 길이 (Sepal Length)") +  # x축 제목
  ylab("꽃받침의 너비 (Sepal Width)")  # y축 제목


library(ggplot2)

# ggplot 코드: 그룹별 Sepal.Length 히스토그램
ggplot(iris, aes(x = Sepal.Length, fill = Species)) +
  geom_histogram(position = "dodge", bins = 20, alpha = 0.7, color = "black") +  # 히스토그램 설정
  scale_fill_manual(values = c("#d62728", "#ff6347", "#ff4500")) +  # 붉은 계열 색상
  theme_minimal() +  # 미니멀한 배경
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),  # 제목 설정
    axis.title = element_text(size = 12, face = "bold"),  # 축 제목 설정
    axis.text = element_text(size = 10),  # 축 레이블 설정
    legend.title = element_text(size = 14, face = "bold"),  # 범례 제목 크기 조정
    legend.text = element_text(size = 12),  # 범례 항목 텍스트 크기 조정
    legend.key.size = unit(1.5, "cm")  # 범례 키 크기 조정
  ) +
  ggtitle("IRIS: Sepal Length의 그룹별 히스토그램") +  # 제목 추가
  xlab("꽃받침의 길이 (Sepal Length)") +  # x축 제목
  ylab("빈도 (Frequency)")  # y축 제목


library(ggplot2)
library(RColorBrewer)  # RColorBrewer 패키지 사용

# ggplot 코드: 그룹별 Sepal.Length 히스토그램
ggplot(iris, aes(x = Sepal.Length, fill = Species)) +
  geom_histogram(position = "dodge", bins = 20, alpha = 0.8, color = "black") +  # 히스토그램 설정
  scale_fill_brewer(palette = "Set2") +  # Set2 팔레트 사용 (더 뚜렷한 색상)
  theme_minimal() +  # 미니멀한 배경
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),  # 제목 설정
    axis.title = element_text(size = 12, face = "bold"),  # 축 제목 설정
    axis.text = element_text(size = 10),  # 축 레이블 설정
    legend.title = element_text(size = 14, face = "bold"),  # 범례 제목 크기 조정
    legend.text = element_text(size = 12),  # 범례 항목 텍스트 크기 조정
    legend.key.size = unit(1.5, "cm")  # 범례 키 크기 조정
  ) +
  ggtitle("IRIS: Sepal Length의 그룹별 히스토그램") +  # 제목 추가
  xlab("꽃받침의 길이 (Sepal Length)") +  # x축 제목
  ylab("빈도 (Frequency)")  # y축 제목


library(ggplot2)

# ggplot 코드: Sepal.Length의 그룹별 stacked bar chart 히스토그램
ggplot(iris, aes(x = Sepal.Length, fill = Species)) +
  geom_histogram(position = "stack", bins = 20, alpha = 0.8, color = "black") +  # 히스토그램 설정
  scale_fill_brewer(palette = "Set2") +  # Set2 팔레트 사용 (구분이 잘 되는 색상)
  theme_minimal() +  # 미니멀한 배경
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),  # 제목 설정
    axis.title = element_text(size = 12, face = "bold"),  # 축 제목 설정
    axis.text = element_text(size = 10),  # 축 레이블 설정
    legend.title = element_text(size = 14, face = "bold"),  # 범례 제목 크기 조정
    legend.text = element_text(size = 12),  # 범례 항목 텍스트 크기 조정
    legend.key.size = unit(1.5, "cm")  # 범례 키 크기 조정
  ) +
  ggtitle("IRIS: Sepal Length의 그룹별 Stacked Bar Chart") +  # 제목 추가
  xlab("꽃받침의 길이 (Sepal Length)") +  # x축 제목
  ylab("빈도 (Frequency)")  # y축 제목

library(ggplot2)

library(ggplot2)

# ggplot 코드: Sepal.Length의 그룹별 Stacked Bar Chart (히스토그램 간 막대 간격 설정)
ggplot(iris, aes(x = Sepal.Length, fill = Species)) +
  geom_histogram(position = "stack", binwidth = 0.3, alpha = 0.8, color = "black", width = 0.7) +  # bin 간격과 막대 너비 설정
  scale_fill_brewer(palette = "Set2") +  # Set2 팔레트 사용 (구분이 잘 되는 색상)
  theme_minimal() +  # 미니멀한 배경
  theme(
    plot.title = element_text(size = 16, face = "bold", hjust = 0.5),  # 제목 설정
    axis.title = element_text(size = 12, face = "bold"),  # 축 제목 설정
    axis.text = element_text(size = 10),  # 축 레이블 설정
    legend.title = element_text(size = 20, face = "bold"),  # 범례 제목 크기 조정
    legend.text = element_text(size = 12),  # 범례 항목 텍스트 크기 조정
    legend.key.size = unit(1.5, "cm")  # 범례 키 크기 조정
  ) +
  ggtitle("IRIS: Sepal Length의 그룹별 Stacked Bar Chart (막대 간 간격)") +  # 제목 추가
  xlab("꽃받침의 길이 (Sepal Length)") +  # x축 제목
  ylab("빈도 (Frequency)")  # y축 제목


ggplot(data = iris, mapping = aes(x = Sepal.Length, y = Sepal.Width)) + 
  geom_point( color='red', pch=2, size=2 )

ggplot(data = iris, mapping = aes(x = Sepal.Length,
                                  y = Sepal.Width))+ 
  geom_point(color = c("purple", "blue", "green")[iris$Species],
                                                               pch = c(0, 2, 20)[iris$Species],size = c(3, 3.5, 4)[iris$Species])





g=ggplot(data = iris, mapping = aes(x = Sepal.Length, y = Sepal.Width, 
                                  color = Species, shape = Species, size = Species)) +
  geom_point() +
  scale_color_manual(values = c("purple", "blue", "green")) +  # 색상 수동 설정
  scale_shape_manual(values = c(0, 2, 20)) +  # 모양 수동 설정
  scale_size_manual(values = c(3, 3.5, 4)) +  # 크기 수동 설정
  theme_minimal() +  # 미니멀한 배경
  ggtitle("IRIS: Sepal Length와 Sepal Width 산포도") + 
  xlab("꽃받침의 길이 (Sepal Length)") + 
  ylab("꽃받침의 너비 (Sepal Width)")
g+ coord_cartesian(xlim = c(5, 7),ylim = c(2, 4))


box <- ggplot(data=iris, aes(x=Species, y=Sepal.Length, fill=Species))
box + geom_boxplot() + xlab("Species")+ylab("Sepal Length") + ggtitle("Iris Boxplot") 



p = ggplot(diamonds, aes(carat, price, color=cut))
p + geom_point()                                                # point 추가 

# -- geom_line() 레이어 추가 
p = ggplot(mtcars, aes(mpg,wt,color=factor(cyl)))
p + geom_line()                                                 # line 추가

# -- geom_point()함수  레이어 추가
p = ggplot(mtcars, aes(mpg,wt,color=factor(cyl)))
p + geom_point()                                                # point 추가

# -- geom_step() 레이어 추가
p = ggplot(mtcars, aes(mpg,wt,color=factor(cyl)))
p + geom_step()                                                 # step 추가

# -- geom_bar() 레이어 추가
p = ggplot(diamonds, aes(clarity))
p + geom_bar(aes(fill=cut), position="fill")                    


library(ggplot2)

# 기본 그래프library(ggplot2)

# 기본 그래프
p <- ggplot(diamonds, aes(x = clarity)) +
  geom_bar(aes(fill = cut), position = "fill", width = 0.7) +  # 막대의 너비 조정
  scale_fill_brewer(palette = "Blues") +  # 세련된 단일 색상 계열 사용 (예: Blues)
  theme_minimal() +  # 미니멀한 배경 설정
  theme(
    plot.title = element_text(size = 18, face = "bold", hjust = 0.5),  # 제목 설정
    axis.title = element_text(size = 14, face = "bold"),  # 축 제목 설정
    axis.text = element_text(size = 12),  # 축 레이블 설정
    legend.title = element_text(size = 14, face = "bold"),  # 범례 제목 설정
    legend.text = element_text(size = 12),  # 범례 항목 텍스트 크기 설정
    legend.key.size = unit(1.5, "cm")  # 범례 키 크기 조정
  ) +
  ggtitle("Clarity와 Cut의 상대 비율") +  # 그래프 제목
  xlab("Clarity") +  # x축 제목
  ylab("비율 (Relative Proportion)")  # y축 제목

# 출력
p
