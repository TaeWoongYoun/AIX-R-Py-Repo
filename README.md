# AI 도구가 개발자 생태계에 미치는 영향 분석

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-4.5.2-276DC3?style=flat-square&logo=r&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=flat-square&logo=json&logoColor=white)

> 한양대학교 ERICA 스마트융합공학부 스마트ICT융합전공
> Stack Overflow와 GitHub AI 레포지토리 데이터 기반 실증 분석

## 프로젝트 소개

본 연구는 2022년 11월 ChatGPT 출시 이후 소프트웨어 개발 생태계의 변화를 실제 데이터를 통해 정량적으로 분석합니다. GitHub AI 레포지토리 185만 개와 Stack Overflow 질문 데이터를 기반으로, ChatGPT 출시 전후의 개발자 행동 패턴 변화를 통계적으로 검증합니다.

### 주요 성과

- **Stack Overflow 질문 수**: ChatGPT 출시 후 **51% 감소** (t-test p < 0.001)
- **GitHub AI 레포지토리**: ChatGPT 출시 후 **141% 증가** (t-test p < 0.001)
- **상관관계 분석**: Pearson 상관계수 **r = -0.933** (매우 강한 음의 상관관계)
- **통계적 유의성**: 모든 검정에서 p-value < 0.001로 통계적으로 유의미한 변화 확인

## 프로젝트 웹페이지

연구 결과 시각화 및 데이터셋은 GitHub Pages를 통해 확인하실 수 있습니다:

**🔗 [https://taewooungyoun.github.io/AIX-R-Py-Repo/](https://taewooungyoun.github.io/AIX-R-Py-Repo/)**

## 관련 저장소

- **메인 저장소**: [https://github.com/TaeWoongYoun/AIX-R-Py-Repo](https://github.com/TaeWoongYoun/AIX-R-Py-Repo)

## 기술 스택

### 데이터 분석
- **Python**: Pandas, NumPy, Matplotlib, JSON
- **R**: jsonlite, t-test, 상관분석
- **데이터 소스**: GitHub API, Stack Overflow API

### 통계 분석
- **검정 방법**: Independent t-test, Pearson Correlation
- **시각화**: 시계열 그래프, Before/After 비교, 상관관계 산점도, 정규화 추세 분석

### 데이터셋
- **기간**: 2021년 1월 ~ 2024년 12월 (48개월)
- **GitHub**: 월별 AI 레포지토리 생성 수 (185만+ 레포지토리)
- **Stack Overflow**: 월별 질문 수 데이터

## 연구 방법론

### 1. 데이터 수집
- GitHub API를 통한 AI 관련 레포지토리 데이터 수집
- Stack Overflow API를 통한 월별 질문 데이터 수집
- 2021-2024년 4년간 월별 데이터 집계

### 2. 통계 분석
- **Before/After 분석**: ChatGPT 출시(2022년 11월) 전후 비교
- **t-test**: 두 기간의 평균 차이 검정
- **상관분석**: Stack Overflow와 GitHub AI 레포지토리 간 관계 분석

### 3. 시각화
- 이중 축 시계열 그래프
- Before vs After 막대 그래프
- 전년대비 변화율 분석
- 상관관계 산점도
- 정규화 추세 비교

## 프로젝트 구조

```
AIX-R-Py-Repo/
├── analysis_code.R              # R 통계 분석 코드
├── real_data_analysis (2).py    # Python 데이터 분석 및 시각화
├── index.html                   # 프로젝트 웹페이지
├── styles.css                   # 웹페이지 스타일
├── script.js                    # 이미지 슬라이더 기능
├── images/                      # 분석 결과 시각화 이미지
│   ├── fig1_timeseries_real.png
│   ├── fig2_before_after_real.png
│   ├── fig3_yoy_real.png
│   ├── fig4_correlation_real.png
│   └── fig5_normalized_trends.png
├── doc/                         # 데이터셋 및 보고서
│   ├── github2021_2025_monthly.json
│   ├── stackoverflow_monthly_data_full.json
│   └── 2025084557 윤태웅 기말보고서.docx
├── HOMEWORK1/                   # Python 과제 (보스턴 주택가격, 와인 품질)
└── HOMEWORK2/                   # R 과제 (통계 분석 및 시각화)
```

## 실행 방법

### Python 분석 실행
```bash
python "real_data_analysis (2).py"
```

### R 통계 분석 실행
```bash
Rscript analysis_code.R
```

### 웹페이지 로컬 실행
```bash
# 로컬 서버 실행 (Python)
python -m http.server 8000

# 브라우저에서 접속
# http://localhost:8000
```

## 주요 발견사항

### 1. Stack Overflow 감소
- ChatGPT 출시 전: 평균 약 360,000건/월
- ChatGPT 출시 후: 평균 약 176,000건/월
- **감소율: 51%** (p < 0.001)

### 2. GitHub AI 레포지토리 증가
- ChatGPT 출시 전: 평균 약 27,000개/월
- ChatGPT 출시 후: 평균 약 65,000개/월
- **증가율: 141%** (p < 0.001)

### 3. 강한 음의 상관관계
- Pearson 상관계수: **r = -0.933**
- 개발자들이 Stack Overflow에서 AI 도구로 문제 해결 방식 전환
- AI 도구 사용 증가 → 전통적 Q&A 플랫폼 의존도 감소

## 연구자

**윤태웅**
- 한양대학교 ERICA 스마트융합공학부 스마트ICT융합전공
- 📧 taewoong25@hanyang.ac.kr
- 📧 24457545yong@gmail.com

## 문의

프로젝트에 대한 질문이나 협업 제안은 아래 연락처로 문의해주세요:

**윤태웅** - 24457545yong@gmail.com

---

**License**: MIT License
**Last Updated**: 2024-12
