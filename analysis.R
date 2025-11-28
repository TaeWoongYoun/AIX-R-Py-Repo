# ==========================================
# AI 시대 개발자 생태계 변화 분석 - R 회귀분석
# 작성자: 윤태웅
# 학번: 2022002288
# ==========================================

# 패키지 로드
library(tidyverse)

cat("=" , rep("=", 79), "\n", sep="")
cat("다중회귀분석 (R)\n")
cat(rep("=", 80), "\n\n", sep="")

# ==========================================
# 1. 데이터 로드
# ==========================================
cat("[1단계] 데이터 로딩...\n")

# Python에서 전처리한 데이터 로드
merged_data <- read_csv("data/merged_monthly.csv", show_col_types = FALSE)

cat("✓ 데이터 로드 완료:", nrow(merged_data), "개월\n\n")

# ==========================================
# 2. 다중회귀분석
# ==========================================
cat("[2단계] 다중회귀분석 수행...\n\n")

# 회귀모형 구축
# 종속변수: Stack Overflow 질문 수
# 독립변수: GitHub 활동 지표 + Period + AI 비율
model <- lm(question_count ~ repo_count + total_issues + total_forks +
              period_dummy + ai_ratio,
            data = merged_data)

# 회귀분석 결과 출력
cat(rep("=", 80), "\n", sep="")
cat("다중회귀분석 결과\n")
cat(rep("=", 80), "\n\n", sep="")
print(summary(model))

# ==========================================
# 3. 회귀계수 해석
# ==========================================
cat("\n", rep("=", 80), "\n", sep="")
cat("회귀계수 해석\n")
cat(rep("=", 80), "\n\n", sep="")

coef_summary <- summary(model)$coefficients
coefs <- coef(model)

cat(sprintf("1. 상수항: %.2f (p=%.4f)\n\n",
            coefs["(Intercept)"],
            coef_summary["(Intercept)", "Pr(>|t|)"]))

cat(sprintf("2. GitHub 레포지토리 수: %.4f\n", coefs["repo_count"]))
cat(sprintf("   → 레포가 1개 증가 → SO 질문 %.4f개 %s\n",
            abs(coefs["repo_count"]),
            ifelse(coefs["repo_count"] > 0, "증가", "감소")))
cat(sprintf("   p-value: %.4f (%s)\n\n",
            coef_summary["repo_count", "Pr(>|t|)"],
            ifelse(coef_summary["repo_count", "Pr(>|t|)"] < 0.05, "유의함 *", "유의하지 않음")))

cat(sprintf("3. GitHub Issues: %.4f\n", coefs["total_issues"]))
cat(sprintf("   → Issues가 1개 증가 → SO 질문 %.4f개 %s\n",
            abs(coefs["total_issues"]),
            ifelse(coefs["total_issues"] > 0, "증가", "감소")))
cat(sprintf("   p-value: %.4f (%s)\n\n",
            coef_summary["total_issues", "Pr(>|t|)"],
            ifelse(coef_summary["total_issues", "Pr(>|t|)"] < 0.05, "유의함 *", "유의하지 않음")))

cat(sprintf("4. GitHub Forks: %.4f\n", coefs["total_forks"]))
cat(sprintf("   → Forks가 1개 증가 → SO 질문 %.4f개 %s\n",
            abs(coefs["total_forks"]),
            ifelse(coefs["total_forks"] > 0, "증가", "감소")))
cat(sprintf("   p-value: %.4f (%s)\n\n",
            coef_summary["total_forks", "Pr(>|t|)"],
            ifelse(coef_summary["total_forks", "Pr(>|t|)"] < 0.05, "유의함 *", "유의하지 않음")))

cat(sprintf("5. Period (ChatGPT 출시 후): %.2f\n", coefs["period_dummy"]))
cat(sprintf("   → ChatGPT 출시 후 SO 질문 %.2f개 %s\n",
            abs(coefs["period_dummy"]),
            ifelse(coefs["period_dummy"] > 0, "증가", "감소")))
cat(sprintf("   p-value: %.4f (%s)\n\n",
            coef_summary["period_dummy", "Pr(>|t|)"],
            ifelse(coef_summary["period_dummy", "Pr(>|t|)"] < 0.05, "유의함 **", "유의하지 않음")))

cat(sprintf("6. AI 프로젝트 비율: %.2f\n", coefs["ai_ratio"]))
cat(sprintf("   → AI 비율 1%% 증가 → SO 질문 %.2f개 %s\n",
            abs(coefs["ai_ratio"]),
            ifelse(coefs["ai_ratio"] > 0, "증가", "감소")))
cat(sprintf("   p-value: %.4f (%s)\n\n",
            coef_summary["ai_ratio", "Pr(>|t|)"],
            ifelse(coef_summary["ai_ratio", "Pr(>|t|)"] < 0.05, "유의함 *", "유의하지 않음")))

# ==========================================
# 4. 모델 적합도
# ==========================================
cat(rep("=", 80), "\n", sep="")
cat("모델 적합도\n")
cat(rep("=", 80), "\n\n", sep="")

model_summary <- summary(model)
cat(sprintf("R-squared: %.4f\n", model_summary$r.squared))
cat(sprintf("Adjusted R-squared: %.4f\n", model_summary$adj.r.squared))
cat(sprintf("F-statistic: %.2f\n", model_summary$fstatistic[1]))
cat(sprintf("p-value: %.4e\n",
            pf(model_summary$fstatistic[1],
               model_summary$fstatistic[2],
               model_summary$fstatistic[3],
               lower.tail = FALSE)))

# ==========================================
# 5. 회귀진단 그래프
# ==========================================
cat("\n[3단계] 회귀진단 그래프 생성...\n")

png("images/r_regression_diagnostics.png", width = 1200, height = 1200, res = 100)
par(mfrow = c(2, 2))
plot(model, which = 1:4)
dev.off()
cat("✓ images/r_regression_diagnostics.png\n")

# ==========================================
# 6. 주요 인사이트
# ==========================================
cat("\n", rep("=", 80), "\n", sep="")
cat("주요 인사이트\n")
cat(rep("=", 80), "\n\n", sep="")

period_coef <- coefs["period_dummy"]
period_pval <- coef_summary["period_dummy", "Pr(>|t|)"]

cat(sprintf("Period 효과: %.2f (%s)\n",
            period_coef,
            ifelse(period_coef < 0, "감소", "증가")))
cat(sprintf("통계적 유의성: %s (p=%.4f)\n\n",
            ifelse(period_pval < 0.05, "유의함", "유의하지 않음"),
            period_pval))

if (period_coef < 0 && period_pval < 0.05) {
  cat("✓ ChatGPT 출시 후 Stack Overflow 질문이 통계적으로 유의하게 감소\n")
  cat("✓ AI 도구가 Stack Overflow를 대체하는 경향 확인\n")
} else if (period_coef > 0 && period_pval < 0.05) {
  cat("✓ ChatGPT 출시 후에도 Stack Overflow 질문 증가\n")
  cat("✓ AI와 커뮤니티가 상호보완적 역할\n")
} else {
  cat("✓ Period 효과가 통계적으로 유의하지 않음\n")
  cat("✓ ChatGPT 출시가 SO 질문량에 명확한 영향을 미치지 않음\n")
}

# 상관관계 추가 분석
issues_coef <- coefs["total_issues"]
if (issues_coef < 0 && coef_summary["total_issues", "Pr(>|t|)"] < 0.05) {
  cat("\n✓ GitHub Issues와 SO 질문 간 음의 상관관계\n")
  cat("✓ 개발자 소통이 GitHub 내부로 이동하는 경향\n")
}

cat("\n", rep("=", 80), "\n", sep="")
cat("R 분석 완료!\n")
cat(rep("=", 80), "\n", sep="")
