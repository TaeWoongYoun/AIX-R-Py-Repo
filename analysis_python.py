"""
AI 시대 개발자 생태계 변화 분석 - Python 스크립트
작성자: 윤태웅
학번: 2022002288
날짜: 2025-11-28
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import os
warnings.filterwarnings('ignore')

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

print("=" * 80)
print("AI 시대 개발자 생태계 변화 분석")
print("=" * 80)

# ==========================================
# 1. 데이터 로드
# ==========================================
print("\n[1단계] 데이터 로딩 중...")

github_df = pd.read_csv('Dataset/github2021~2025.csv')
stackoverflow_df = pd.read_csv('Dataset/stackoverflow2021~2025.csv')

print(f"✓ GitHub 데이터: {len(github_df):,} 행")
print(f"✓ Stack Overflow 데이터: {len(stackoverflow_df):,} 행")

# ==========================================
# 2. 데이터 전처리
# ==========================================
print("\n[2단계] 데이터 전처리 중...")

# 날짜 컬럼 변환 (여러 형식 대응)
github_df['created_at'] = pd.to_datetime(github_df['created_at'], format='ISO8601', errors='coerce')
stackoverflow_df['creation_date'] = pd.to_datetime(stackoverflow_df['creation_date'], format='ISO8601', errors='coerce')

# 연도-월 컬럼 추가
github_df['year_month'] = github_df['created_at'].dt.to_period('M')
stackoverflow_df['year_month'] = stackoverflow_df['creation_date'].dt.to_period('M')

print("✓ 날짜 전처리 완료")

# Period별 데이터 개수
print(f"\nGitHub - Before: {(github_df['period'] == 'Before').sum():,} / After: {(github_df['period'] == 'After').sum():,}")
print(f"Stack Overflow - Before: {(stackoverflow_df['period'] == 'Before').sum():,} / After: {(stackoverflow_df['period'] == 'After').sum():,}")

# ==========================================
# 3. 월별 집계
# ==========================================
print("\n[3단계] 월별 집계 중...")

# GitHub 월별 통계
github_monthly = github_df.groupby(['year_month', 'period']).agg({
    'id': 'count',
    'stars': 'sum',
    'forks': 'sum',
    'open_issues': 'sum'
}).reset_index()
github_monthly.columns = ['year_month', 'period', 'repo_count', 'total_stars', 'total_forks', 'total_issues']

# Stack Overflow 월별 통계
so_monthly = stackoverflow_df.groupby(['year_month', 'period']).agg({
    'id': 'count'
}).reset_index()
so_monthly.columns = ['year_month', 'period', 'question_count']

print(f"✓ GitHub 월별 데이터: {len(github_monthly)} 개월")
print(f"✓ Stack Overflow 월별 데이터: {len(so_monthly)} 개월")

# ==========================================
# 4. 기술통계 분석
# ==========================================
print("\n[4단계] 기술통계 분석 중...")
print("\n" + "=" * 60)
print("GitHub - Before vs After 비교")
print("=" * 60)

before_github = github_monthly[github_monthly['period'] == 'Before']
after_github = github_monthly[github_monthly['period'] == 'After']

print(f"\n[Before 기간 평균]")
print(f"  월평균 레포지토리 생성: {before_github['repo_count'].mean():,.0f}")
print(f"  월평균 총 Stars: {before_github['total_stars'].mean():,.0f}")
print(f"  월평균 총 Forks: {before_github['total_forks'].mean():,.0f}")
print(f"  월평균 총 Issues: {before_github['total_issues'].mean():,.0f}")

print(f"\n[After 기간 평균]")
print(f"  월평균 레포지토리 생성: {after_github['repo_count'].mean():,.0f}")
print(f"  월평균 총 Stars: {after_github['total_stars'].mean():,.0f}")
print(f"  월평균 총 Forks: {after_github['total_forks'].mean():,.0f}")
print(f"  월평균 총 Issues: {after_github['total_issues'].mean():,.0f}")

print(f"\n[변화율]")
print(f"  레포지토리 생성: {(after_github['repo_count'].mean() / before_github['repo_count'].mean() - 1) * 100:+.1f}%")
print(f"  Stars: {(after_github['total_stars'].mean() / before_github['total_stars'].mean() - 1) * 100:+.1f}%")
print(f"  Forks: {(after_github['total_forks'].mean() / before_github['total_forks'].mean() - 1) * 100:+.1f}%")
print(f"  Issues: {(after_github['total_issues'].mean() / before_github['total_issues'].mean() - 1) * 100:+.1f}%")

print("\n" + "=" * 60)
print("Stack Overflow - Before vs After 비교")
print("=" * 60)

before_so = so_monthly[so_monthly['period'] == 'Before']
after_so = so_monthly[so_monthly['period'] == 'After']

print(f"\n[Before 기간 평균]")
print(f"  월평균 질문 수: {before_so['question_count'].mean():,.0f}")

print(f"\n[After 기간 평균]")
print(f"  월평균 질문 수: {after_so['question_count'].mean():,.0f}")

print(f"\n[변화율]")
print(f"  질문 수: {(after_so['question_count'].mean() / before_so['question_count'].mean() - 1) * 100:+.1f}%")

# ==========================================
# 5. 시각화
# ==========================================
print("\n[5단계] 시각화 생성 중...")

# 폴더 생성
os.makedirs('images', exist_ok=True)

# 그래프 1: GitHub 월별 레포지토리 생성 추이
print("  - GitHub 월별 추이 그래프...")
fig, ax = plt.subplots(figsize=(14, 6))

github_monthly_sorted = github_monthly.sort_values('year_month')
x_values = range(len(github_monthly_sorted))

ax.plot(x_values, github_monthly_sorted['repo_count'], marker='o', linewidth=2, markersize=4, color='steelblue')

# ChatGPT 출시 시점 표시
try:
    chatgpt_idx = github_monthly_sorted[github_monthly_sorted['year_month'].astype(str) == '2022-11'].index[0]
    chatgpt_x = list(github_monthly_sorted.index).index(chatgpt_idx)
    ax.axvline(x=chatgpt_x, color='red', linestyle='--', linewidth=2, label='ChatGPT 출시 (2022.11)')
    ax.axvspan(0, chatgpt_x, alpha=0.1, color='blue', label='Before')
    ax.axvspan(chatgpt_x, len(x_values)-1, alpha=0.1, color='green', label='After')
except:
    pass

ax.set_xlabel('기간', fontsize=12)
ax.set_ylabel('월별 레포지토리 생성 수', fontsize=12)
ax.set_title('GitHub 월별 레포지토리 생성 추이 (2021-2025)', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

tick_positions = range(0, len(x_values), 3)
tick_labels = [str(github_monthly_sorted.iloc[i]['year_month']) for i in tick_positions]
ax.set_xticks(tick_positions)
ax.set_xticklabels(tick_labels, rotation=45, ha='right')

plt.tight_layout()
plt.savefig('images/github_monthly_trend.png', dpi=300, bbox_inches='tight')
plt.close()

# 그래프 2: Stack Overflow 월별 질문 수 추이
print("  - Stack Overflow 월별 추이 그래프...")
fig, ax = plt.subplots(figsize=(14, 6))

so_monthly_sorted = so_monthly.sort_values('year_month')
x_values = range(len(so_monthly_sorted))

ax.plot(x_values, so_monthly_sorted['question_count'], marker='o', linewidth=2, markersize=4, color='orange')

try:
    chatgpt_idx = so_monthly_sorted[so_monthly_sorted['year_month'].astype(str) == '2022-11'].index[0]
    chatgpt_x = list(so_monthly_sorted.index).index(chatgpt_idx)
    ax.axvline(x=chatgpt_x, color='red', linestyle='--', linewidth=2, label='ChatGPT 출시 (2022.11)')
    ax.axvspan(0, chatgpt_x, alpha=0.1, color='blue', label='Before')
    ax.axvspan(chatgpt_x, len(x_values)-1, alpha=0.1, color='green', label='After')
except:
    pass

ax.set_xlabel('기간', fontsize=12)
ax.set_ylabel('월별 질문 수', fontsize=12)
ax.set_title('Stack Overflow 월별 질문 수 추이 (2021-2025)', fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)

tick_positions = range(0, len(x_values), 3)
tick_labels = [str(so_monthly_sorted.iloc[i]['year_month']) for i in tick_positions]
ax.set_xticks(tick_positions)
ax.set_xticklabels(tick_labels, rotation=45, ha='right')

plt.tight_layout()
plt.savefig('images/stackoverflow_monthly_trend.png', dpi=300, bbox_inches='tight')
plt.close()

# 그래프 3: Before vs After 비교 막대그래프
print("  - Before vs After 비교 그래프...")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

categories = ['레포지토리\n생성', 'Stars', 'Forks', 'Issues']
before_values = [
    before_github['repo_count'].mean(),
    before_github['total_stars'].mean(),
    before_github['total_forks'].mean(),
    before_github['total_issues'].mean()
]
after_values = [
    after_github['repo_count'].mean(),
    after_github['total_stars'].mean(),
    after_github['total_forks'].mean(),
    after_github['total_issues'].mean()
]

x = np.arange(len(categories))
width = 0.35

axes[0].bar(x - width/2, before_values, width, label='Before', color='skyblue')
axes[0].bar(x + width/2, after_values, width, label='After', color='lightgreen')
axes[0].set_ylabel('월평균 값', fontsize=11)
axes[0].set_title('GitHub 활동량 Before vs After', fontsize=12, fontweight='bold')
axes[0].set_xticks(x)
axes[0].set_xticklabels(categories)
axes[0].legend()
axes[0].grid(True, alpha=0.3, axis='y')

so_categories = ['질문 수']
so_before = [before_so['question_count'].mean()]
so_after = [after_so['question_count'].mean()]

x2 = np.arange(len(so_categories))
axes[1].bar(x2 - width/2, so_before, width, label='Before', color='skyblue')
axes[1].bar(x2 + width/2, so_after, width, label='After', color='lightgreen')
axes[1].set_ylabel('월평균 질문 수', fontsize=11)
axes[1].set_title('Stack Overflow 활동량 Before vs After', fontsize=12, fontweight='bold')
axes[1].set_xticks(x2)
axes[1].set_xticklabels(so_categories)
axes[1].legend()
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('images/before_after_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

# ==========================================
# 6. 상관관계 분석
# ==========================================
print("\n[6단계] 상관관계 분석 중...")

# 월별 데이터 통합
merged_monthly = pd.merge(
    github_monthly[['year_month', 'repo_count', 'total_stars', 'total_forks', 'total_issues']],
    so_monthly[['year_month', 'question_count']],
    on='year_month',
    how='inner'
)

# 상관계수 계산
correlation_matrix = merged_monthly[['repo_count', 'total_stars', 'total_forks', 'total_issues', 'question_count']].corr()

print("\n상관계수 행렬:")
print(correlation_matrix)

print(f"\n주요 상관관계:")
print(f"  GitHub 레포지토리 vs SO 질문: {correlation_matrix.loc['repo_count', 'question_count']:.3f}")
print(f"  GitHub Issues vs SO 질문: {correlation_matrix.loc['total_issues', 'question_count']:.3f}")
print(f"  GitHub Forks vs SO 질문: {correlation_matrix.loc['total_forks', 'question_count']:.3f}")

# 그래프 4: 상관계수 히트맵
print("  - 상관계수 히트맵...")
fig, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(correlation_matrix, annot=True, fmt='.3f', cmap='coolwarm', center=0,
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})

ax.set_title('GitHub vs Stack Overflow 상관관계 분석', fontsize=14, fontweight='bold', pad=20)

labels = ['GitHub\n레포지토리', 'GitHub\nStars', 'GitHub\nForks', 'GitHub\nIssues', 'Stack Overflow\n질문']
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.set_yticklabels(labels, rotation=0)

plt.tight_layout()
plt.savefig('images/correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# 그래프 5: 산점도
print("  - 산점도 그래프...")
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

axes[0, 0].scatter(merged_monthly['repo_count'], merged_monthly['question_count'], alpha=0.6)
axes[0, 0].set_xlabel('GitHub 레포지토리 생성 수')
axes[0, 0].set_ylabel('Stack Overflow 질문 수')
axes[0, 0].set_title(f'상관계수: {correlation_matrix.loc["repo_count", "question_count"]:.3f}')
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].scatter(merged_monthly['total_issues'], merged_monthly['question_count'], alpha=0.6, color='orange')
axes[0, 1].set_xlabel('GitHub 총 Issues')
axes[0, 1].set_ylabel('Stack Overflow 질문 수')
axes[0, 1].set_title(f'상관계수: {correlation_matrix.loc["total_issues", "question_count"]:.3f}')
axes[0, 1].grid(True, alpha=0.3)

axes[1, 0].scatter(merged_monthly['total_forks'], merged_monthly['question_count'], alpha=0.6, color='green')
axes[1, 0].set_xlabel('GitHub 총 Forks')
axes[1, 0].set_ylabel('Stack Overflow 질문 수')
axes[1, 0].set_title(f'상관계수: {correlation_matrix.loc["total_forks", "question_count"]:.3f}')
axes[1, 0].grid(True, alpha=0.3)

axes[1, 1].scatter(merged_monthly['total_stars'], merged_monthly['question_count'], alpha=0.6, color='red')
axes[1, 1].set_xlabel('GitHub 총 Stars')
axes[1, 1].set_ylabel('Stack Overflow 질문 수')
axes[1, 1].set_title(f'상관계수: {correlation_matrix.loc["total_stars", "question_count"]:.3f}')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('images/scatter_plots.png', dpi=300, bbox_inches='tight')
plt.close()

# ==========================================
# 7. R 분석용 데이터 저장
# ==========================================
print("\n[7단계] R 분석용 데이터 저장 중...")

os.makedirs('data', exist_ok=True)

# Period 더미 변수 추가
merged_monthly_with_period = pd.merge(
    merged_monthly,
    github_monthly[['year_month', 'period']].drop_duplicates(),
    on='year_month',
    how='left'
)
merged_monthly_with_period['period_dummy'] = (merged_monthly_with_period['period'] == 'After').astype(int)

# AI 관련 프로젝트 비율 계산
github_ai_ratio = github_df.groupby('year_month').apply(
    lambda x: (x['ai_field'].notna().sum() / len(x)) if len(x) > 0 else 0
).reset_index(name='ai_ratio')

merged_monthly_with_period = pd.merge(
    merged_monthly_with_period,
    github_ai_ratio,
    on='year_month',
    how='left'
)

# year_month를 문자열로 변환
merged_monthly_with_period['year_month'] = merged_monthly_with_period['year_month'].astype(str)
github_monthly['year_month'] = github_monthly['year_month'].astype(str)
so_monthly['year_month'] = so_monthly['year_month'].astype(str)

# CSV 저장
github_monthly.to_csv('data/github_monthly.csv', index=False, encoding='utf-8-sig')
so_monthly.to_csv('data/stackoverflow_monthly.csv', index=False, encoding='utf-8-sig')
merged_monthly_with_period.to_csv('data/merged_monthly.csv', index=False, encoding='utf-8-sig')

print("✓ data/github_monthly.csv")
print("✓ data/stackoverflow_monthly.csv")
print("✓ data/merged_monthly.csv")

# ==========================================
# 8. 분석 요약
# ==========================================
print("\n" + "=" * 80)
print("분석 결과 요약")
print("=" * 80)

print("\n1. 기술통계 분석")
print(f"   - GitHub 레포지토리 증가율: {(after_github['repo_count'].mean() / before_github['repo_count'].mean() - 1) * 100:+.1f}%")
print(f"   - Stack Overflow 질문 증가율: {(after_so['question_count'].mean() / before_so['question_count'].mean() - 1) * 100:+.1f}%")

print("\n2. 상관관계 분석")
print(f"   - GitHub 레포 vs SO 질문: {correlation_matrix.loc['repo_count', 'question_count']:.3f}")
print(f"   - GitHub Issues vs SO 질문: {correlation_matrix.loc['total_issues', 'question_count']:.3f}")

print("\n3. 저장된 그래프")
print("   - images/github_monthly_trend.png")
print("   - images/stackoverflow_monthly_trend.png")
print("   - images/before_after_comparison.png")
print("   - images/correlation_heatmap.png")
print("   - images/scatter_plots.png")

print("\n4. 다음 단계")
print("   → R 스크립트 실행: Rscript analysis.R")
print("   → 회귀분석 결과 확인")

print("\n" + "=" * 80)
print("Python 분석 완료!")
print("=" * 80)
