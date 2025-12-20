"""
GitHub CSV → 월별 집계 JSON 변환 스크립트
로컬에서 실행하세요.

사용법:
1. 이 파일을 github_csv_to_json.py로 저장
2. GitHub CSV 파일과 같은 폴더에 넣기
3. 터미널에서 실행: python github_csv_to_json.py your_github_data.csv
"""

import pandas as pd
import json
from datetime import datetime
import sys

def convert_github_csv_to_json(csv_path, output_path="github_monthly_data.json"):
    """
    GitHub CSV를 월별 집계 JSON으로 변환
    """
    print(f"Loading CSV: {csv_path}")
    
    # CSV 로드
    df = pd.read_csv(csv_path, low_memory=False)
    
    print(f"Total rows: {len(df):,}")
    print(f"Columns: {list(df.columns)}")
    
    # created_at을 datetime으로 변환
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
    
    # 결측값 제거
    df = df.dropna(subset=['created_at'])
    
    # 연-월 컬럼 추가
    df['year_month'] = df['created_at'].dt.to_period('M').astype(str)
    df['year'] = df['created_at'].dt.year
    df['month'] = df['created_at'].dt.month
    
    # period 컬럼이 있으면 Before/After 구분
    if 'period' in df.columns:
        has_period = True
    else:
        has_period = False
        # ChatGPT 출시일 기준으로 생성
        chatgpt_date = datetime(2022, 11, 30)
        df['period'] = df['created_at'].apply(
            lambda x: 'Before' if x < chatgpt_date else 'After'
        )
    
    print(f"\nDate range: {df['created_at'].min()} ~ {df['created_at'].max()}")
    
    # =========================================================================
    # 월별 집계
    # =========================================================================
    
    monthly_stats = df.groupby('year_month').agg({
        'id': 'count',  # 레포지토리 수
        'stars': 'sum',
        'forks': 'sum',
        'watchers': 'sum',
        'open_issues': 'sum'
    }).reset_index()
    
    monthly_stats.columns = ['period', 'repo_count', 'total_stars', 'total_forks', 
                             'total_watchers', 'total_issues']
    
    # Before/After별 월별 집계
    period_monthly = df.groupby(['year_month', 'period']).agg({
        'id': 'count'
    }).reset_index()
    period_monthly.columns = ['year_month', 'ai_period', 'repo_count']
    
    # AI 분야별 집계 (ai_field 컬럼이 있는 경우)
    if 'ai_field' in df.columns:
        field_monthly = df.groupby(['year_month', 'ai_field']).agg({
            'id': 'count'
        }).reset_index()
        field_monthly.columns = ['year_month', 'ai_field', 'repo_count']
        field_data = field_monthly.to_dict('records')
    else:
        field_data = []
    
    # 키워드별 집계 (keyword 컬럼이 있는 경우)
    if 'keyword' in df.columns:
        keyword_monthly = df.groupby(['year_month', 'keyword']).agg({
            'id': 'count'
        }).reset_index()
        keyword_monthly.columns = ['year_month', 'keyword', 'repo_count']
        keyword_data = keyword_monthly.to_dict('records')
    else:
        keyword_data = []
    
    # 언어별 집계
    if 'language' in df.columns:
        lang_monthly = df.groupby(['year_month', 'language']).agg({
            'id': 'count'
        }).reset_index()
        lang_monthly.columns = ['year_month', 'language', 'repo_count']
        # 상위 10개 언어만
        top_langs = df['language'].value_counts().head(10).index.tolist()
        lang_data = lang_monthly[lang_monthly['language'].isin(top_langs)].to_dict('records')
    else:
        lang_data = []
    
    # =========================================================================
    # JSON 구조 생성
    # =========================================================================
    
    result = {
        "metadata": {
            "source": "GitHub API",
            "original_file": csv_path,
            "total_repositories": len(df),
            "date_range": {
                "start": str(df['created_at'].min().date()),
                "end": str(df['created_at'].max().date())
            },
            "conversion_timestamp": datetime.now().isoformat(),
            "ai_events": {
                "github_copilot_preview": "2021-06-29",
                "github_copilot_release": "2022-06-21",
                "chatgpt_release": "2022-11-30",
                "gpt4_release": "2023-03-14",
                "copilot_chat_release": "2023-12-29",
                "vibe_coding_coined": "2025-02-02"
            }
        },
        "monthly_summary": monthly_stats.to_dict('records'),
        "by_period": period_monthly.to_dict('records'),
        "by_ai_field": field_data,
        "by_keyword": keyword_data,
        "by_language": lang_data,
        "statistics": {
            "before_chatgpt": {
                "total_repos": int(df[df['period'] == 'Before']['id'].count()),
                "avg_monthly_repos": float(df[df['period'] == 'Before'].groupby('year_month')['id'].count().mean()),
                "total_stars": int(df[df['period'] == 'Before']['stars'].sum()),
                "total_forks": int(df[df['period'] == 'Before']['forks'].sum())
            },
            "after_chatgpt": {
                "total_repos": int(df[df['period'] == 'After']['id'].count()),
                "avg_monthly_repos": float(df[df['period'] == 'After'].groupby('year_month')['id'].count().mean()),
                "total_stars": int(df[df['period'] == 'After']['stars'].sum()),
                "total_forks": int(df[df['period'] == 'After']['forks'].sum())
            }
        }
    }
    
    # JSON 저장
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2, default=str)
    
    print(f"\n✅ JSON 저장 완료: {output_path}")
    print(f"   - 월별 데이터: {len(monthly_stats)}개월")
    print(f"   - Before ChatGPT: {result['statistics']['before_chatgpt']['total_repos']:,}개 레포")
    print(f"   - After ChatGPT: {result['statistics']['after_chatgpt']['total_repos']:,}개 레포")
    
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python github_csv_to_json.py <csv_file_path>")
        print("예시: python github_csv_to_json.py github_ai_repos.csv")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    output_file = csv_file.replace('.csv', '_monthly.json')
    
    convert_github_csv_to_json(csv_file, output_file)
