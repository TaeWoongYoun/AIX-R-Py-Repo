-- ============================================================================
-- Stack Overflow Data Collection SQL Queries
-- Source: Stack Exchange Data Explorer (SEDE)
-- URL: https://data.stackexchange.com/stackoverflow/query/new
-- ============================================================================

-- ============================================================================
-- Query 1: 월별 전체 질문 수 (기본)
-- ============================================================================
SELECT 
    YEAR(CreationDate) AS Year, 
    MONTH(CreationDate) AS Month, 
    COUNT(*) AS NumQuestions
FROM Posts
WHERE PostTypeId = 1  -- Questions only
GROUP BY YEAR(CreationDate), MONTH(CreationDate)
ORDER BY Year DESC, Month DESC;

-- ============================================================================
-- Query 2: 월별 질문 + 답변 수
-- ============================================================================
SELECT 
    YEAR(CreationDate) AS Year, 
    MONTH(CreationDate) AS Month,
    SUM(CASE WHEN PostTypeId = 1 THEN 1 ELSE 0 END) AS Questions,
    SUM(CASE WHEN PostTypeId = 2 THEN 1 ELSE 0 END) AS Answers
FROM Posts
WHERE PostTypeId IN (1, 2)
GROUP BY YEAR(CreationDate), MONTH(CreationDate)
ORDER BY Year DESC, Month DESC;

-- ============================================================================
-- Query 3: Python 태그 월별 질문 수
-- ============================================================================
SELECT 
    YEAR(p.CreationDate) AS Year, 
    MONTH(p.CreationDate) AS Month, 
    COUNT(*) AS PythonQuestions
FROM Posts p
INNER JOIN PostTags pt ON p.Id = pt.PostId
INNER JOIN Tags t ON pt.TagId = t.Id
WHERE p.PostTypeId = 1 
  AND t.TagName = 'python'
GROUP BY YEAR(p.CreationDate), MONTH(p.CreationDate)
ORDER BY Year DESC, Month DESC;

-- ============================================================================
-- Query 4: JavaScript 태그 월별 질문 수
-- ============================================================================
SELECT 
    YEAR(p.CreationDate) AS Year, 
    MONTH(p.CreationDate) AS Month, 
    COUNT(*) AS JavaScriptQuestions
FROM Posts p
INNER JOIN PostTags pt ON p.Id = pt.PostId
INNER JOIN Tags t ON pt.TagId = t.Id
WHERE p.PostTypeId = 1 
  AND t.TagName = 'javascript'
GROUP BY YEAR(p.CreationDate), MONTH(p.CreationDate)
ORDER BY Year DESC, Month DESC;

-- ============================================================================
-- Query 5: AI/ML 관련 태그 월별 질문 수
-- ============================================================================
SELECT 
    YEAR(p.CreationDate) AS Year, 
    MONTH(p.CreationDate) AS Month, 
    COUNT(DISTINCT p.Id) AS AIMLQuestions
FROM Posts p
INNER JOIN PostTags pt ON p.Id = pt.PostId
INNER JOIN Tags t ON pt.TagId = t.Id
WHERE p.PostTypeId = 1 
  AND t.TagName IN (
    'machine-learning', 
    'deep-learning', 
    'artificial-intelligence',
    'neural-network',
    'tensorflow',
    'pytorch',
    'keras',
    'scikit-learn'
  )
GROUP BY YEAR(p.CreationDate), MONTH(p.CreationDate)
ORDER BY Year DESC, Month DESC;

-- ============================================================================
-- Query 6: ChatGPT/OpenAI 관련 태그 (2022년 11월 이후)
-- ============================================================================
SELECT 
    YEAR(p.CreationDate) AS Year, 
    MONTH(p.CreationDate) AS Month, 
    COUNT(DISTINCT p.Id) AS ChatGPTQuestions
FROM Posts p
INNER JOIN PostTags pt ON p.Id = pt.PostId
INNER JOIN Tags t ON pt.TagId = t.Id
WHERE p.PostTypeId = 1 
  AND t.TagName IN (
    'chatgpt', 
    'openai-api', 
    'gpt-3',
    'gpt-4',
    'langchain'
  )
  AND p.CreationDate >= '2022-11-01'
GROUP BY YEAR(p.CreationDate), MONTH(p.CreationDate)
ORDER BY Year DESC, Month DESC;

-- ============================================================================
-- Query 7: 월별 활성 사용자 수 (질문 작성 기준)
-- ============================================================================
SELECT 
    YEAR(CreationDate) AS Year, 
    MONTH(CreationDate) AS Month, 
    COUNT(DISTINCT OwnerUserId) AS ActiveQuestioners
FROM Posts
WHERE PostTypeId = 1
  AND OwnerUserId IS NOT NULL
GROUP BY YEAR(CreationDate), MONTH(CreationDate)
ORDER BY Year DESC, Month DESC;

-- ============================================================================
-- Query 8: 월별 평균 답변 수 (질문당)
-- ============================================================================
SELECT 
    YEAR(q.CreationDate) AS Year,
    MONTH(q.CreationDate) AS Month,
    COUNT(q.Id) AS Questions,
    COUNT(a.Id) AS Answers,
    CAST(COUNT(a.Id) AS FLOAT) / NULLIF(COUNT(q.Id), 0) AS AvgAnswersPerQuestion
FROM Posts q
LEFT JOIN Posts a ON q.Id = a.ParentId AND a.PostTypeId = 2
WHERE q.PostTypeId = 1
GROUP BY YEAR(q.CreationDate), MONTH(q.CreationDate)
ORDER BY Year DESC, Month DESC;

-- ============================================================================
-- 사용 방법:
-- 1. https://data.stackexchange.com/stackoverflow/query/new 접속
-- 2. 위 쿼리 중 필요한 것을 복사하여 붙여넣기
-- 3. Run Query 클릭
-- 4. Download CSV 또는 Download JSON으로 결과 저장
-- ============================================================================
