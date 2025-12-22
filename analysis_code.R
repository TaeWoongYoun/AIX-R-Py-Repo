# AI 도구가 개발자 생태계에 미치는 영향 분석
# 핵심 통계 검정 (t-test, 상관분석)

library(jsonlite)

# 데이터 로드
gh <- fromJSON("github2021_2025_monthly.json")$monthly_summary
so <- fromJSON("stackoverflow_monthly_data_full.json")$monthly_questions

# 병합 (2021-01 ~ 2024-12)
gh$date <- as.Date(paste0(gh$period, "-01"))
so$date <- as.Date(paste0(so$period, "-01"))
df <- merge(gh[,c("period","date","repo_count")], so[,c("period","questions")], by="period")

# Before/After 분리 (ChatGPT: 2022-11-01)
before_so <- df$questions[df$date < "2022-11-01"]
after_so <- df$questions[df$date >= "2022-11-01"]
before_gh <- df$repo_count[df$date < "2022-11-01"]
after_gh <- df$repo_count[df$date >= "2022-11-01"]

# 1. Stack Overflow t-test
t.test(before_so, after_so)

# 2. GitHub t-test
t.test(before_gh, after_gh)

# 3. 상관관계 검정
cor.test(df$questions, df$repo_count)
