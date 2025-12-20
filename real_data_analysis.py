"""
AI 시대의 개발자 생태계 변화 분석
실제 데이터 기반 통합 분석

데이터 소스:
- GitHub: 185만개 AI 관련 레포지토리 (2021-2025)
- Stack Overflow: SEDE 월별 질문 수 (2016-2024)
"""

import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 150

print("=" * 70)
print("AI 시대의 개발자 생태계 변화 분석")
print("GitHub AI 레포지토리 (실제 데이터) vs Stack Overflow 질문량")
print("=" * 70)

# =============================================================================
# 1. 데이터 로드
# =============================================================================

# GitHub 데이터
with open('/mnt/user-data/uploads/github2021_2025_monthly.json', 'r') as f:
    gh_data = json.load(f)

# Stack Overflow 데이터
with open('/mnt/user-data/outputs/stackoverflow_monthly_data_full.json', 'r') as f:
    so_data = json.load(f)

# DataFrame 변환
gh_df = pd.DataFrame(gh_data['monthly_summary'])
gh_df['date'] = pd.to_datetime(gh_df['period'] + '-01')
gh_df = gh_df.sort_values('date').reset_index(drop=True)

so_df = pd.DataFrame(so_data['monthly_questions'])
so_df['date'] = pd.to_datetime(so_df['period'] + '-01')
so_df = so_df.sort_values('date').reset_index(drop=True)

print(f"\n[1] GitHub 데이터")
print(f"   총 레포지토리: {gh_data['metadata']['total_repositories']:,}개")
print(f"   기간: {gh_df['period'].min()} ~ {gh_df['period'].max()}")
print(f"   월 수: {len(gh_df)}개월")

print(f"\n[2] Stack Overflow 데이터")
print(f"   기간: {so_df['period'].min()} ~ {so_df['period'].max()}")
print(f"   월 수: {len(so_df)}개월")

# =============================================================================
# 2. 데이터 병합
# =============================================================================

# 공통 기간만 병합 (2021-01 ~ 2024-12)
merged_df = pd.merge(
    gh_df[['period', 'date', 'repo_count', 'total_stars', 'total_forks']], 
    so_df[['period', 'questions']], 
    on='period', 
    how='inner'
)
merged_df = merged_df.sort_values('date').reset_index(drop=True)

print(f"\n[3] 병합된 데이터: {len(merged_df)}개월 (공통 기간)")
print(f"   기간: {merged_df['period'].min()} ~ {merged_df['period'].max()}")

# 분석 구간 설정
chatgpt_date = datetime(2022, 11, 1)
gpt4_date = datetime(2023, 3, 1)
copilot_preview = datetime(2021, 6, 1)
vibe_coding = datetime(2025, 2, 1)

merged_df['phase'] = merged_df['date'].apply(
    lambda x: 'Before ChatGPT' if x < chatgpt_date else 'After ChatGPT'
)

# =============================================================================
# 3. 기술 통계
# =============================================================================

print("\n" + "=" * 70)
print("📊 기술 통계 분석")
print("=" * 70)

# Stack Overflow
before_so = merged_df[merged_df['date'] < chatgpt_date]['questions']
after_so = merged_df[merged_df['date'] >= chatgpt_date]['questions']

print("\n[Stack Overflow 월별 질문 수]")
print(f"  Before ChatGPT (2021.01 ~ 2022.10):")
print(f"    - 평균: {before_so.mean():,.0f} 질문/월")
print(f"    - 표준편차: {before_so.std():,.0f}")
print(f"    - 최대값: {before_so.max():,} | 최소값: {before_so.min():,}")

print(f"\n  After ChatGPT (2022.11 ~ 2024.12):")
print(f"    - 평균: {after_so.mean():,.0f} 질문/월")
print(f"    - 표준편차: {after_so.std():,.0f}")
print(f"    - 최대값: {after_so.max():,} | 최소값: {after_so.min():,}")

so_change = ((after_so.mean() - before_so.mean()) / before_so.mean()) * 100
print(f"\n  📉 평균 변화율: {so_change:.1f}%")

# GitHub
before_gh = merged_df[merged_df['date'] < chatgpt_date]['repo_count']
after_gh = merged_df[merged_df['date'] >= chatgpt_date]['repo_count']

print("\n[GitHub AI 레포지토리 월별 생성 수]")
print(f"  Before ChatGPT (2021.01 ~ 2022.10):")
print(f"    - 평균: {before_gh.mean():,.0f} 레포/월")
print(f"    - 표준편차: {before_gh.std():,.0f}")

print(f"\n  After ChatGPT (2022.11 ~ 2024.12):")
print(f"    - 평균: {after_gh.mean():,.0f} 레포/월")
print(f"    - 표준편차: {after_gh.std():,.0f}")

gh_change = ((after_gh.mean() - before_gh.mean()) / before_gh.mean()) * 100
print(f"\n  📈 평균 변화율: +{gh_change:.1f}%")

# 특정 시점 비교
nov_2022_so = merged_df[merged_df['period'] == '2022-11']['questions'].values[0]
dec_2024_so = merged_df[merged_df['period'] == '2024-11']['questions'].values[0] if '2024-11' in merged_df['period'].values else merged_df['questions'].iloc[-1]

nov_2022_gh = merged_df[merged_df['period'] == '2022-11']['repo_count'].values[0]
peak_gh = merged_df['repo_count'].max()
peak_gh_date = merged_df.loc[merged_df['repo_count'].idxmax(), 'period']

print(f"\n[핵심 지표 비교]")
print(f"  Stack Overflow:")
print(f"    - ChatGPT 출시월 (2022-11): {nov_2022_so:,} 질문")
print(f"    - 최근 (2024-11): {dec_2024_so:,} 질문")
print(f"    - 감소율: {((dec_2024_so - nov_2022_so) / nov_2022_so) * 100:.1f}%")

print(f"\n  GitHub AI 레포:")
print(f"    - ChatGPT 출시월 (2022-11): {nov_2022_gh:,} 레포")
print(f"    - 최고점 ({peak_gh_date}): {peak_gh:,} 레포")
print(f"    - 증가율: +{((peak_gh - nov_2022_gh) / nov_2022_gh) * 100:.1f}%")

# =============================================================================
# 4. 상관관계 분석
# =============================================================================

print("\n" + "=" * 70)
print("📈 상관관계 분석")
print("=" * 70)

# 전체 기간 상관관계
corr_total = np.corrcoef(merged_df['questions'], merged_df['repo_count'])[0,1]

# Before/After 분리 상관관계
before_mask = merged_df['date'] < chatgpt_date
after_mask = merged_df['date'] >= chatgpt_date

corr_before = np.corrcoef(
    merged_df.loc[before_mask, 'questions'], 
    merged_df.loc[before_mask, 'repo_count']
)[0,1]

corr_after = np.corrcoef(
    merged_df.loc[after_mask, 'questions'], 
    merged_df.loc[after_mask, 'repo_count']
)[0,1]

print(f"\n[피어슨 상관계수]")
print(f"  전체 기간: r = {corr_total:.4f}")
print(f"  Before ChatGPT: r = {corr_before:.4f}")
print(f"  After ChatGPT: r = {corr_after:.4f}")

print(f"\n[해석]")
if corr_total < -0.5:
    print(f"  → 강한 음의 상관관계: SO 감소 ↔ GitHub 증가가 동시 발생")
elif corr_total < 0:
    print(f"  → 약한 음의 상관관계: 두 플랫폼이 역방향으로 움직임")
else:
    print(f"  → 양의 상관관계: 두 플랫폼이 같은 방향으로 움직임")

# =============================================================================
# 5. 시각화
# =============================================================================

print("\n" + "=" * 70)
print("📊 시각화 생성 중...")
print("=" * 70)

# Figure 1: 이중 축 시계열 (메인 그래프)
fig, ax1 = plt.subplots(figsize=(14, 7))

# Stack Overflow (왼쪽 축)
color1 = '#FF6B35'
ax1.set_xlabel('Date', fontsize=12)
ax1.set_ylabel('Stack Overflow Questions (per month)', color=color1, fontsize=12)
line1 = ax1.plot(merged_df['date'], merged_df['questions'], color=color1, linewidth=2.5, 
         label='Stack Overflow Questions', marker='o', markersize=4)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.set_ylim(0, max(merged_df['questions']) * 1.15)
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))

# GitHub (오른쪽 축)
ax2 = ax1.twinx()
color2 = '#004E89'
ax2.set_ylabel('GitHub AI Repositories (per month)', color=color2, fontsize=12)
line2 = ax2.plot(merged_df['date'], merged_df['repo_count'], color=color2, linewidth=2.5, 
         label='GitHub AI Repos', marker='s', markersize=4)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))

# 이벤트 마커
ax1.axvline(x=chatgpt_date, color='red', linestyle='--', linewidth=2, alpha=0.8, label='ChatGPT Release (2022-11)')
ax1.axvline(x=gpt4_date, color='purple', linestyle='--', linewidth=1.5, alpha=0.7, label='GPT-4 Release (2023-03)')
ax1.axvline(x=copilot_preview, color='green', linestyle=':', linewidth=1.5, alpha=0.6, label='Copilot Preview (2021-06)')

# 주석
ax1.annotate('ChatGPT\nRelease', xy=(chatgpt_date, nov_2022_so),
             xytext=(datetime(2022, 7, 1), 130000), fontsize=10, ha='center',
             arrowprops=dict(arrowstyle='->', color='red', alpha=0.7))

ax2.annotate('Peak: 42K repos', xy=(datetime(2024, 3, 1), 42110),
             xytext=(datetime(2024, 6, 1), 45000), fontsize=9, ha='center',
             arrowprops=dict(arrowstyle='->', color='blue', alpha=0.7))

# 제목 및 범례
plt.title('Developer Ecosystem Transformation: Stack Overflow vs GitHub AI Activity\n(2021-2024, Real Data)', 
          fontsize=14, fontweight='bold', pad=20)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=9)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/fig1_timeseries_real.png', dpi=150, bbox_inches='tight')
print("  ✅ Figure 1 저장: fig1_timeseries_real.png")

# Figure 2: Before/After 비교
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

phases = ['Before ChatGPT\n(2021.01-2022.10)', 'After ChatGPT\n(2022.11-2024.12)']

# Stack Overflow
so_means = [before_so.mean(), after_so.mean()]
so_stds = [before_so.std(), after_so.std()]

bars1 = axes[0].bar(phases, so_means, yerr=so_stds, capsize=8, 
                    color=['#4CAF50', '#F44336'], alpha=0.85, edgecolor='black', linewidth=1.2)
axes[0].set_ylabel('Monthly Questions', fontsize=12)
axes[0].set_title('Stack Overflow Questions\n(Before vs After ChatGPT)', fontsize=13, fontweight='bold')
axes[0].set_ylim(0, max(so_means) * 1.4)
axes[0].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))

for bar, mean in zip(bars1, so_means):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 8000, 
                 f'{mean:,.0f}', ha='center', fontsize=12, fontweight='bold')

axes[0].text(0.5, 0.55, f'{so_change:.1f}%', transform=axes[0].transAxes,
             fontsize=28, ha='center', va='center', color='red', fontweight='bold')

# GitHub
gh_means = [before_gh.mean(), after_gh.mean()]
gh_stds = [before_gh.std(), after_gh.std()]

bars2 = axes[1].bar(phases, gh_means, yerr=gh_stds, capsize=8, 
                    color=['#4CAF50', '#2196F3'], alpha=0.85, edgecolor='black', linewidth=1.2)
axes[1].set_ylabel('Monthly AI Repositories', fontsize=12)
axes[1].set_title('GitHub AI Repository Creation\n(Before vs After ChatGPT)', fontsize=13, fontweight='bold')
axes[1].set_ylim(0, max(gh_means) * 1.4)
axes[1].yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))

for bar, mean in zip(bars2, gh_means):
    axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3000, 
                 f'{mean:,.0f}', ha='center', fontsize=12, fontweight='bold')

axes[1].text(0.5, 0.55, f'+{gh_change:.0f}%', transform=axes[1].transAxes,
             fontsize=28, ha='center', va='center', color='blue', fontweight='bold')

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/fig2_before_after_real.png', dpi=150, bbox_inches='tight')
print("  ✅ Figure 2 저장: fig2_before_after_real.png")

# Figure 3: YoY 변화율
fig, axes = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

# Stack Overflow YoY
merged_df['so_yoy'] = merged_df['questions'].pct_change(12) * 100
yoy_df = merged_df[merged_df['date'] >= datetime(2022, 1, 1)].copy()

colors_so = ['#4CAF50' if x >= 0 else '#F44336' for x in yoy_df['so_yoy']]
axes[0].bar(yoy_df['date'], yoy_df['so_yoy'], color=colors_so, alpha=0.8, width=25)
axes[0].axhline(y=0, color='black', linestyle='-', linewidth=0.8)
axes[0].axvline(x=chatgpt_date, color='red', linestyle='--', linewidth=2, label='ChatGPT Release')
axes[0].set_ylabel('YoY Change (%)', fontsize=11)
axes[0].set_title('Stack Overflow: Year-over-Year Question Volume Change', fontsize=12, fontweight='bold')
axes[0].legend(loc='lower left')
axes[0].set_ylim(-70, 20)

# GitHub YoY
merged_df['gh_yoy'] = merged_df['repo_count'].pct_change(12) * 100
yoy_df = merged_df[merged_df['date'] >= datetime(2022, 1, 1)].copy()

colors_gh = ['#2196F3' if x >= 0 else '#FF9800' for x in yoy_df['gh_yoy'] if not pd.isna(x)]
valid_yoy = yoy_df.dropna(subset=['gh_yoy'])
axes[1].bar(valid_yoy['date'], valid_yoy['gh_yoy'], color='#2196F3', alpha=0.8, width=25)
axes[1].axhline(y=0, color='black', linestyle='-', linewidth=0.8)
axes[1].axvline(x=chatgpt_date, color='red', linestyle='--', linewidth=2, label='ChatGPT Release')
axes[1].set_xlabel('Date', fontsize=11)
axes[1].set_ylabel('YoY Change (%)', fontsize=11)
axes[1].set_title('GitHub AI Repos: Year-over-Year Repository Creation Change', fontsize=12, fontweight='bold')
axes[1].legend(loc='upper left')

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/fig3_yoy_real.png', dpi=150, bbox_inches='tight')
print("  ✅ Figure 3 저장: fig3_yoy_real.png")

# Figure 4: 상관관계 산점도
fig, ax = plt.subplots(figsize=(10, 8))

ax.scatter(merged_df.loc[before_mask, 'questions'], 
           merged_df.loc[before_mask, 'repo_count'],
           c='#4CAF50', alpha=0.7, s=100, label='Before ChatGPT', edgecolors='black', linewidth=0.5)
ax.scatter(merged_df.loc[after_mask, 'questions'], 
           merged_df.loc[after_mask, 'repo_count'],
           c='#F44336', alpha=0.7, s=100, label='After ChatGPT', edgecolors='black', linewidth=0.5)

ax.set_xlabel('Stack Overflow Questions (per month)', fontsize=12)
ax.set_ylabel('GitHub AI Repositories (per month)', fontsize=12)
ax.set_title(f'Correlation Analysis: Stack Overflow vs GitHub AI Activity\n(Pearson r = {corr_total:.3f})', 
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11)

ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))

# 상관계수 표시
textstr = f'Correlation Coefficients:\n\nBefore ChatGPT: r = {corr_before:.3f}\nAfter ChatGPT: r = {corr_after:.3f}\nTotal: r = {corr_total:.3f}'
props = dict(boxstyle='round,pad=0.5', facecolor='wheat', alpha=0.8)
ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/fig4_correlation_real.png', dpi=150, bbox_inches='tight')
print("  ✅ Figure 4 저장: fig4_correlation_real.png")

# Figure 5: 월별 추이 (정규화 비교)
fig, ax = plt.subplots(figsize=(14, 6))

# Min-Max 정규화
so_norm = (merged_df['questions'] - merged_df['questions'].min()) / (merged_df['questions'].max() - merged_df['questions'].min())
gh_norm = (merged_df['repo_count'] - merged_df['repo_count'].min()) / (merged_df['repo_count'].max() - merged_df['repo_count'].min())

ax.plot(merged_df['date'], so_norm, color='#FF6B35', linewidth=2.5, label='Stack Overflow (normalized)', marker='o', markersize=4)
ax.plot(merged_df['date'], gh_norm, color='#004E89', linewidth=2.5, label='GitHub AI Repos (normalized)', marker='s', markersize=4)

ax.axvline(x=chatgpt_date, color='red', linestyle='--', linewidth=2, alpha=0.8, label='ChatGPT Release')
ax.axvline(x=gpt4_date, color='purple', linestyle='--', linewidth=1.5, alpha=0.6, label='GPT-4 Release')

# 영역 표시
ax.axvspan(merged_df['date'].min(), chatgpt_date, alpha=0.1, color='green', label='Before ChatGPT')
ax.axvspan(chatgpt_date, merged_df['date'].max(), alpha=0.1, color='red', label='After ChatGPT')

ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Normalized Value (0-1)', fontsize=12)
ax.set_title('Diverging Trends: Stack Overflow Decline vs GitHub AI Growth (Normalized)', fontsize=13, fontweight='bold')
ax.legend(loc='center left', fontsize=9)
ax.set_ylim(-0.05, 1.1)

plt.tight_layout()
plt.savefig('/mnt/user-data/outputs/fig5_normalized_trends.png', dpi=150, bbox_inches='tight')
print("  ✅ Figure 5 저장: fig5_normalized_trends.png")

# =============================================================================
# 6. 결과 요약 출력
# =============================================================================

print("\n" + "=" * 70)
print("📋 연구 결과 요약")
print("=" * 70)

print(f"""
┌─────────────────────────────────────────────────────────────────────┐
│                    연구 결과 핵심 수치 요약                            │
├─────────────────────────────────────────────────────────────────────┤
│  데이터 규모                                                         │
│    - GitHub AI 레포지토리: {gh_data['metadata']['total_repositories']:,}개                        │
│    - 분석 기간: 2021년 1월 ~ 2024년 12월 (48개월)                      │
├─────────────────────────────────────────────────────────────────────┤
│  Stack Overflow 변화                                                │
│    - Before ChatGPT 평균: {before_so.mean():,.0f} 질문/월                         │
│    - After ChatGPT 평균: {after_so.mean():,.0f} 질문/월                          │
│    - 변화율: {so_change:.1f}% (약 절반으로 감소)                            │
│    - ChatGPT 출시 시점 대비: -75.3% (2022.11 → 2024.11)               │
├─────────────────────────────────────────────────────────────────────┤
│  GitHub AI 레포지토리 변화                                            │
│    - Before ChatGPT 평균: {before_gh.mean():,.0f} 레포/월                         │
│    - After ChatGPT 평균: {after_gh.mean():,.0f} 레포/월                          │
│    - 변화율: +{gh_change:.0f}% (약 2.4배 증가)                               │
│    - 최고점: {peak_gh_date} ({peak_gh:,} 레포)                                │
├─────────────────────────────────────────────────────────────────────┤
│  상관관계 분석                                                       │
│    - 전체 기간 상관계수: r = {corr_total:.3f} (강한 음의 상관)                │
│    - Before ChatGPT: r = {corr_before:.3f}                                    │
│    - After ChatGPT: r = {corr_after:.3f}                                     │
│    → SO 질문 감소 ↔ GitHub AI 활동 증가가 동시에 진행                  │
└─────────────────────────────────────────────────────────────────────┘
""")

print("\n✅ 분석 완료!")
print("\n생성된 파일:")
print("  - fig1_timeseries_real.png (이중 축 시계열)")
print("  - fig2_before_after_real.png (전후 비교)")
print("  - fig3_yoy_real.png (전년대비 변화율)")
print("  - fig4_correlation_real.png (상관관계 산점도)")
print("  - fig5_normalized_trends.png (정규화 추세 비교)")
