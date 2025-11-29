import requests
import pandas as pd
from datetime import datetime
import time
import os

class ComprehensiveStackOverflowCollector:
    def __init__(self, api_key=None):
        self.base_url = "https://api.stackexchange.com/2.3"
        self.api_key = api_key
    
    def get_questions_by_tag(self, tag, from_date, to_date, max_pages=None):
        """단일 태그로 질문 수집 (max_pages=None이면 제한 없음)"""
        url = f"{self.base_url}/questions"
        
        params = {
            "site": "stackoverflow",
            "tagged": tag,
            "fromdate": int(from_date.timestamp()),
            "todate": int(to_date.timestamp()),
            "sort": "creation",
            "order": "desc",
            "pagesize": 100
        }
        
        if self.api_key:
            params["key"] = self.api_key
        
        all_questions = []
        page = 1
        
        print(f"\n🔍 '{tag}' 태그 수집 중...")

        while max_pages is None or page <= max_pages:
            params['page'] = page
            
            try:
                response = requests.get(url, params=params)
                
                if response.status_code != 200:
                    print(f"  ❌ 에러: {response.status_code}")
                    break
                
                data = response.json()
                questions = data.get('items', [])
                
                if not questions:
                    break
                
                all_questions.extend(questions)
                
                quota_remaining = data.get('quota_remaining', 0)
                has_more = data.get('has_more', False)

                max_pages_str = "무제한" if max_pages is None else str(max_pages)
                print(f"  [{page}/{max_pages_str}] 📦 {len(all_questions)}개 | 남은 요청: {quota_remaining}")
                
                if not has_more:
                    break
                
                page += 1
                time.sleep(0.3)
                
            except Exception as e:
                print(f"  ❌ 에러: {e}")
                break
        
        print(f"  ✅ '{tag}': {len(all_questions)}개 수집 완료")
        return all_questions
    
    def questions_to_dataframe(self, questions):
        """질문 리스트를 DataFrame으로 변환"""
        data = []
        
        for q in questions:
            data.append({
                'question_id': q['question_id'],
                'title': q['title'],
                'tags': '|'.join(q['tags']),
                'view_count': q['view_count'],
                'answer_count': q['answer_count'],
                'score': q['score'],
                'is_answered': q.get('is_answered', False),
                'creation_date': datetime.fromtimestamp(q['creation_date']),
                'owner_type': q['owner'].get('user_type', 'unknown'),
                'link': q['link']
            })
        
        return pd.DataFrame(data)
    
    def collect_multiple_tags(self, tags, from_date, to_date, max_pages=None):
        """여러 태그 순차 수집 (max_pages=None이면 제한 없음)"""
        all_questions = []
        tag_stats = {}
        
        print("\n" + "="*70)
        print(f"📅 기간: {from_date.strftime('%Y-%m-%d')} ~ {to_date.strftime('%Y-%m-%d')}")
        print(f"🏷️  수집 태그: {len(tags)}개")
        print("="*70)
        
        for i, tag in enumerate(tags, 1):
            print(f"\n[{i}/{len(tags)}] ", end="")
            questions = self.get_questions_by_tag(tag, from_date, to_date, max_pages)
            
            all_questions.extend(questions)
            tag_stats[tag] = len(questions)
            
            time.sleep(1)  # 태그 간 1초 대기
        
        # DataFrame 변환
        if all_questions:
            df = pd.DataFrame([q for q in all_questions])
            
            # question_id로 중복 제거
            df_unique = df.drop_duplicates(subset=['question_id'], keep='first')
            
            print("\n" + "="*70)
            print("🎉 전체 수집 완료!")
            print("="*70)
            print(f"총 수집: {len(all_questions)}개")
            print(f"중복 제거 후: {len(df_unique)}개")
            
            print("\n📊 태그별 수집 현황:")
            for tag, count in sorted(tag_stats.items(), key=lambda x: x[1], reverse=True):
                print(f"  {tag:25s}: {count:4d}개")
            
            # DataFrame 형식으로 변환
            final_df = self.questions_to_dataframe(df_unique.to_dict('records'))
            
            return final_df, tag_stats
        
        return None, tag_stats


# ========== 2023년 AI 관련 전체 키워드 수집 ==========

collector = ComprehensiveStackOverflowCollector()

# AI 관련 핵심 키워드 (RQ2 검증용)
ai_keywords = [
    # ChatGPT 관련
    "chatgpt",
    "gpt-4",
    "gpt-3.5",
    "gpt-3",
    "openai-api",
    
    # AI Agent 관련
    "ai-agent",
    "autonomous-agent",
    "langchain",
    "autogpt",
    
    # Vibe Coding 관련 (프롬프트 엔지니어링)
    "prompt-engineering",
    "prompt-design",
    
    # AI 코딩 도구
    "github-copilot",
    "ai-assisted-coding",
    "code-generation",
    "ai-code-review",
    
    # LLM 관련
    "large-language-model",
    "llm",
    "generative-ai",
    
    # 기타 AI
    "machine-learning",
    "artificial-intelligence",
    "deep-learning",
    "neural-network"
]

print(f"\n🎯 수집 대상: {len(ai_keywords)}개 키워드")

# 5년치 데이터 수집 (2020-2025 현재까지)
years = [2020, 2021, 2022, 2023, 2024, 2025]
all_dfs = []

for year in years:
    print(f"\n📅 {year}년 데이터 수집 시작")
    print("="*70)

    # 2025년은 현재 날짜까지만
    if year == 2025:
        to_date = datetime.now()
    else:
        to_date = datetime(year, 12, 31)

    df_year, tag_stats = collector.collect_multiple_tags(
        tags=ai_keywords,
        from_date=datetime(year, 1, 1),
        to_date=to_date
        # max_pages를 지정하지 않으면 제한 없이 모든 데이터 수집
    )

    if df_year is not None:
        all_dfs.append(df_year)
        print(f"\n✅ {year}년: {len(df_year)}개 수집 완료")

    # 년도 간 2초 대기
    if year != years[-1]:
        print(f"\n⏳ 다음 년도 수집 전 대기 중...")
        time.sleep(2)

# 모든 년도 데이터 통합
if all_dfs:
    df_2023 = pd.concat(all_dfs, ignore_index=True)
    df_2023 = df_2023.drop_duplicates(subset=['question_id'], keep='first')

    print("\n" + "="*70)
    print("🎉 전체 6년치 데이터 통합 완료!")
    print("="*70)
    print(f"총 수집: {len(df_2023)}개 (2020-2025)")

    # 년도별 통계
    df_2023['year'] = df_2023['creation_date'].dt.year
    yearly_counts = df_2023.groupby('year').size()
    print(f"\n📅 년도별 질문 수:")
    for year, count in yearly_counts.items():
        print(f"  {year}: {count:5d}개")

# 상세 분석
if len(all_dfs) > 0 and df_2023 is not None:
    print("\n" + "="*70)
    print("📊 상세 통계")
    print("="*70)
    
    # 기본 통계
    print(f"\n총 질문 수: {len(df_2023)}개")
    print(f"답변된 질문: {df_2023['is_answered'].sum()}개 ({df_2023['is_answered'].sum()/len(df_2023)*100:.1f}%)")
    
    # 조회수/답변/점수 통계
    print(f"\n조회수 통계:")
    print(f"  평균: {df_2023['view_count'].mean():.0f}")
    print(f"  중앙값: {df_2023['view_count'].median():.0f}")
    print(f"  최대: {df_2023['view_count'].max():,}")
    
    print(f"\n답변 수 통계:")
    print(f"  평균: {df_2023['answer_count'].mean():.1f}")
    print(f"  최대: {df_2023['answer_count'].max()}")
    
    print(f"\n점수 통계:")
    print(f"  평균: {df_2023['score'].mean():.1f}")
    print(f"  최대: {df_2023['score'].max()}")
    
    # 월별 집계
    df_2023['year_month'] = df_2023['creation_date'].dt.to_period('M')
    monthly_counts = df_2023.groupby('year_month').size()
    
    print(f"\n📅 월별 질문 수:")
    for month, count in monthly_counts.items():
        print(f"  {month}: {count:4d}개")
    
    # 주요 태그 분석
    print(f"\n🏷️  가장 많이 등장한 태그 (Top 15):")
    all_tags = []
    for tags_str in df_2023['tags']:
        all_tags.extend(tags_str.split('|'))
    
    tag_counts = pd.Series(all_tags).value_counts()
    for i, (tag, count) in enumerate(tag_counts.head(15).items(), 1):
        print(f"  {i:2d}. {tag:25s}: {count:4d}회")
    
    # 상위 10개 인기 질문
    print(f"\n⭐ Top 10 인기 질문 (조회수 기준):")
    top_10 = df_2023.nlargest(10, 'view_count')[['title', 'view_count', 'answer_count', 'score', 'creation_date']]
    for i, (idx, row) in enumerate(top_10.iterrows(), 1):
        print(f"\n{i:2d}. {row['title'][:70]}")
        print(f"    👁️  {row['view_count']:,} 조회 | 💬 {row['answer_count']}개 답변 | ⭐ {row['score']}점 | 📅 {row['creation_date'].strftime('%Y-%m-%d')}")
    
    # CSV 저장
    if not os.path.exists('data'):
        os.makedirs('data')

    filename = 'data/stackoverflow_ai_2020_2025_full.csv'
    df_2023.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"\n💾 전체 데이터 저장: {filename}")

    # 월별 통계 저장
    monthly_stats = df_2023.groupby('year_month').agg({
        'question_id': 'count',
        'view_count': 'mean',
        'answer_count': 'mean',
        'score': 'sum'
    }).rename(columns={
        'question_id': 'question_count',
        'view_count': 'avg_views',
        'answer_count': 'avg_answers',
        'score': 'total_score'
    })

    monthly_stats.to_csv('data/stackoverflow_ai_2020_2025_monthly.csv')
    print(f"💾 월별 통계 저장: data/stackoverflow_ai_2020_2025_monthly.csv")

    # 년도별 통계 저장
    yearly_stats = df_2023.groupby('year').agg({
        'question_id': 'count',
        'view_count': 'mean',
        'answer_count': 'mean',
        'score': 'sum',
        'is_answered': lambda x: (x.sum() / len(x) * 100)
    }).rename(columns={
        'question_id': 'question_count',
        'view_count': 'avg_views',
        'answer_count': 'avg_answers',
        'score': 'total_score',
        'is_answered': 'answered_rate'
    })

    yearly_stats.to_csv('data/stackoverflow_ai_2020_2025_yearly.csv')
    print(f"💾 년도별 통계 저장: data/stackoverflow_ai_2020_2025_yearly.csv")

print("\n" + "="*70)
print("✅ 모든 작업 완료!")
print("="*70)