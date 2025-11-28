"""
데이터 연도별 분포 확인 스크립트
"""

import pandas as pd

print("=" * 80)
print("Stack Overflow 데이터 연도별 분포 확인")
print("=" * 80)

# Stack Overflow 데이터 로드
print("\n[1] 데이터 로딩 중...")
stackoverflow_df = pd.read_csv('Dataset/stackoverflow2021~2025.csv')

print(f"총 데이터 개수: {len(stackoverflow_df):,} 개")

# 날짜 파싱
print("\n[2] 날짜 파싱 중...")
stackoverflow_df['creation_date'] = pd.to_datetime(stackoverflow_df['creation_date'], format='ISO8601', errors='coerce')

# 연도 추출
stackoverflow_df['year'] = stackoverflow_df['creation_date'].dt.year

# 연도별 개수
print("\n" + "=" * 80)
print("연도별 데이터 개수")
print("=" * 80)

year_counts = stackoverflow_df['year'].value_counts().sort_index()

for year, count in year_counts.items():
    if pd.notna(year):
        print(f"{int(year)}년: {count:>10,} 개")

# 연도-월별 개수 (2022년 상세)
print("\n" + "=" * 80)
print("2022년 월별 데이터 개수")
print("=" * 80)

stackoverflow_2022 = stackoverflow_df[stackoverflow_df['year'] == 2022]
stackoverflow_2022['month'] = stackoverflow_2022['creation_date'].dt.month

month_counts = stackoverflow_2022['month'].value_counts().sort_index()

for month, count in month_counts.items():
    if pd.notna(month):
        print(f"2022-{int(month):02d}: {count:>10,} 개")

# Period별 개수
print("\n" + "=" * 80)
print("Period별 데이터 개수")
print("=" * 80)

period_counts = stackoverflow_df['period'].value_counts()
for period, count in period_counts.items():
    print(f"{period}: {count:>10,} 개")

# 날짜 범위
print("\n" + "=" * 80)
print("데이터 날짜 범위")
print("=" * 80)

valid_dates = stackoverflow_df['creation_date'].dropna()
if len(valid_dates) > 0:
    print(f"최소 날짜: {valid_dates.min()}")
    print(f"최대 날짜: {valid_dates.max()}")

# GitHub 데이터도 확인
print("\n\n" + "=" * 80)
print("GitHub 데이터 연도별 분포 확인")
print("=" * 80)

github_df = pd.read_csv('Dataset/github2021~2025.csv')
print(f"총 데이터 개수: {len(github_df):,} 개")

github_df['created_at'] = pd.to_datetime(github_df['created_at'], format='ISO8601', errors='coerce')
github_df['year'] = github_df['created_at'].dt.year

print("\n" + "=" * 80)
print("연도별 데이터 개수")
print("=" * 80)

year_counts_gh = github_df['year'].value_counts().sort_index()

for year, count in year_counts_gh.items():
    if pd.notna(year):
        print(f"{int(year)}년: {count:>10,} 개")

# Period별 개수
print("\n" + "=" * 80)
print("Period별 데이터 개수")
print("=" * 80)

period_counts_gh = github_df['period'].value_counts()
for period, count in period_counts_gh.items():
    print(f"{period}: {count:>10,} 개")

print("\n" + "=" * 80)
print("완료!")
print("=" * 80)
