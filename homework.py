import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 폰트 설정 (마이너스 부호 깨짐 방지)
plt.rcParams['axes.unicode_minus'] = False

# ==============================================================================
# PART 1: 보스턴 주택가격 데이터 분석
# ==============================================================================
print("=" * 80)
print("PART 1: 보스턴 주택가격 데이터 분석")
print("=" * 80)

# Q1: 데이터 전처리
print("\nQ1: 데이터 전처리")
print("-" * 40)

boston_df = pd.read_csv('boston_csv.csv', na_values=['na', 'NaN'])
print(f"원본 데이터 shape: {boston_df.shape}")
print(f"결측치가 있는 행 수: {boston_df.isnull().any(axis=1).sum()}")
boston_df_cleaned = boston_df.dropna()
print(f"결측치 제거 후 shape: {boston_df_cleaned.shape}")

# Q2: 요약 통계 및 상관관계 분석
print("\nQ2: 요약 통계 및 상관관계 분석")
print("-" * 40)
print("\n요약 통계:")
print(boston_df_cleaned.describe())

plt.figure(figsize=(14, 10))
correlation_matrix = boston_df_cleaned.corr()
sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm', center=0, square=True, linewidths=0.5)
plt.title('Boston Housing Data - Correlation Heatmap')
plt.tight_layout()
print("\n상관관계 히트맵을 표시합니다.")
plt.show()

# Q3: 단순회귀분석 (LSTAT -> MEDV)
print("\nQ3: 단순회귀분석 (LSTAT -> MEDV)")
print("-" * 40)

X_simple = boston_df_cleaned[['LSTAT']].values
y = boston_df_cleaned['MEDV'].values
X_train_simple, X_test_simple, y_train_simple, y_test_simple = train_test_split(
    X_simple, y, test_size=0.25, random_state=42
)
print(f"Training/Test 분할: {len(X_train_simple)} (75%) / {len(X_test_simple)} (25%)")

lr_simple = LinearRegression()
lr_simple.fit(X_train_simple, y_train_simple)

y_train_pred_simple = lr_simple.predict(X_train_simple)
train_mse_simple = mean_squared_error(y_train_simple, y_train_pred_simple)
train_r2_simple = r2_score(y_train_simple, y_train_pred_simple)

print(f"\nTraining Set 결과:")
print(f"  - 회귀계수: Intercept={lr_simple.intercept_:.4f}, LSTAT={lr_simple.coef_[0]:.4f}")
print(f"  - R² Score: {train_r2_simple:.4f}")
print(f"  - MSE: {train_mse_simple:.4f}")

y_test_pred_simple = lr_simple.predict(X_test_simple)
test_mse_simple = mean_squared_error(y_test_simple, y_test_pred_simple)
print(f"\nTest Set 결과:")
print(f"  - MSE: {test_mse_simple:.4f}")

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(X_train_simple, y_train_simple, alpha=0.5, label='Training Data')
plt.plot(X_train_simple, y_train_pred_simple, 'r-', label='Regression Line')
plt.title('Simple Linear Regression - Training Set')
plt.legend()
plt.subplot(1, 2, 2)
plt.scatter(X_test_simple, y_test_simple, alpha=0.5, label='Test Data')
plt.plot(X_test_simple, y_test_pred_simple, 'r-', label='Predictions')
plt.title('Simple Linear Regression - Test Set')
plt.legend()
plt.tight_layout()
print("\n단순회귀분석 그래프를 표시합니다.")
plt.show()

# Q4: 다중회귀분석 (LSTAT, TAX -> MEDV)
print("\nQ4: 다중회귀분석 (LSTAT, TAX -> MEDV)")
print("-" * 40)

X_multiple = boston_df_cleaned[['LSTAT', 'TAX']].values
X_train_mult, X_test_mult, y_train_mult, y_test_mult = train_test_split(
    X_multiple, y, test_size=0.25, random_state=42
)
print(f"Training/Test 분할: {len(X_train_mult)} (75%) / {len(X_test_mult)} (25%)")

lr_multiple = LinearRegression()
lr_multiple.fit(X_train_mult, y_train_mult)

y_train_pred_mult = lr_multiple.predict(X_train_mult)
train_mse_mult = mean_squared_error(y_train_mult, y_train_pred_mult)
train_r2_mult = r2_score(y_train_mult, y_train_pred_mult)

print(f"\nTraining Set 결과:")
print(f"  - 회귀계수: Intercept={lr_multiple.intercept_:.4f}, LSTAT={lr_multiple.coef_[0]:.4f}, TAX={lr_multiple.coef_[1]:.4f}")
print(f"  - R² Score: {train_r2_mult:.4f}")
print(f"  - MSE: {train_mse_mult:.4f}")

y_test_pred_mult = lr_multiple.predict(X_test_mult)
test_mse_mult = mean_squared_error(y_test_mult, y_test_pred_mult)
print(f"\nTest Set 결과:")
print(f"  - MSE: {test_mse_mult:.4f}")

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(y_train_mult, y_train_pred_mult, alpha=0.5)
plt.plot([y_train_mult.min(), y_train_mult.max()], [y_train_mult.min(), y_train_mult.max()], 'r--', lw=2)
plt.title('Multiple Regression - Training Set')
plt.xlabel('Actual MEDV')
plt.ylabel('Predicted MEDV')
plt.subplot(1, 2, 2)
plt.scatter(y_test_mult, y_test_pred_mult, alpha=0.5)
plt.plot([y_test_mult.min(), y_test_mult.max()], [y_test_mult.min(), y_test_mult.max()], 'r--', lw=2)
plt.title('Multiple Regression - Test Set')
plt.xlabel('Actual MEDV')
plt.ylabel('Predicted MEDV')
plt.tight_layout()
print("\n다중회귀분석 그래프를 표시합니다.")
plt.show()


# ==============================================================================
# PART 2: 와인 데이터 k-NN 분류
# ==============================================================================
print("\n" + "=" * 80)
print("PART 2: 와인 데이터 k-NN 분류")
print("=" * 80)

# --- k-NN 분석을 위한 헬퍼 함수 ---
def run_knn(k, X_train, X_test, y_train, y_test, feature_desc=""):
    """k-NN 모델을 학습하고 Train/Test 정확도를 출력 및 반환합니다."""
    
    knn = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    knn.fit(X_train, y_train)
    
    # Train 정확도
    y_train_pred = knn.predict(X_train)
    train_acc = accuracy_score(y_train, y_train_pred)
    
    # Test 정확도
    y_test_pred = knn.predict(X_test)
    test_acc = accuracy_score(y_test, y_test_pred)
    
    print(f"\n분석: {feature_desc} (k={k})")
    print(f"  - Training Set 정확도: {train_acc*100:.2f}%")
    print(f"  - Test Set 정확도: {test_acc*100:.2f}%")
    
    return train_acc, test_acc
# ---------------------------------

# 1. 데이터 로드
print("\n1. 와인 데이터 로드")
print("-" * 40)
wine = pd.read_csv('wine_data.csv')
print(f"데이터 shape: {wine.shape}")
print(f"클래스 분포:\n{wine['Class'].value_counts().sort_index()}")

# 2. 요약 통계
print("\n2. 요약 통계")
print("-" * 40)
print(wine.describe())

# 3. Train/Test 데이터 분할 (70%/30%)
print("\n3. Train/Test 데이터 분할 (70%/30%)")
print("-" * 40)

y = wine['Class'].values
X = wine.drop('Class', axis=1).values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
print(f"Training set 크기: {len(X_train)} ({len(X_train)/len(X)*100:.1f}%)")
print(f"Test set 크기: {len(X_test)} ({len(X_test)/len(X)*100:.1f}%)")

# 4-7. k-NN 분류 (모든 변수 사용)
print("\n4-7. k-NN 분류 (모든 변수 사용)")
print("-" * 40)

train_acc_knn5, test_acc_knn5 = run_knn(5, X_train, X_test, y_train, y_test, "All features")
train_acc_knn3, test_acc_knn3 = run_knn(3, X_train, X_test, y_train, y_test, "All features")

# 8. 4개 변수만 사용한 k-NN 분류
print("\n8. 4개 변수만 사용한 k-NN 분류")
print("   (Alcohol, Malic acid, Ash, Alcalinity of ash)")
print("-" * 40)

selected_features = ['Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash']
X_reduced = wine[selected_features].values

X_train_red, X_test_red, y_train_red, y_test_red = train_test_split(
    X_reduced, y, test_size=0.3, random_state=42, stratify=y
)

train_acc_red5, test_acc_red5 = run_knn(5, X_train_red, X_test_red, y_train_red, y_test_red, "4 features")
train_acc_red3, test_acc_red3 = run_knn(3, X_train_red, X_test_red, y_train_red, y_test_red, "4 features")


# ==============================================================================
# 결과 요약
# ==============================================================================
print("\n" + "=" * 80)
print("결과 요약")
print("=" * 80)

# Part 1 결과 요약
print("\nPart 1 - 보스턴 주택가격 회귀분석 결과:")
print("-" * 40)
results_part1 = pd.DataFrame({
    'Model': ['Simple Regression (LSTAT)', 'Multiple Regression (LSTAT, TAX)'],
    'Train R²': [train_r2_simple, train_r2_mult],
    'Train MSE': [train_mse_simple, train_mse_mult],
    'Test MSE': [test_mse_simple, test_mse_mult]
})
print(results_part1.to_string(index=False))

# Part 2 결과 요약
print("\nPart 2 - 와인 k-NN 분류 결과:")
print("-" * 40)
results_part2 = pd.DataFrame({
    'Features': ['All features', 'All features', '4 features', '4 features'],
    'k': [5, 3, 5, 3],
    'Train Accuracy (%)': [train_acc_knn5*100, train_acc_knn3*100, train_acc_red5*100, train_acc_red3*100],
    'Test Accuracy (%)': [test_acc_knn5*100, test_acc_knn3*100, test_acc_red5*100, test_acc_red3*100]
})
# k값 순서대로 정렬 (3, 5)
results_part2 = results_part2.sort_values(by=['Features', 'k'], ascending=[True, True]).reset_index(drop=True)
print(results_part2.to_string(index=False))

# k값 비교 시각화
plt.figure(figsize=(12, 5))

# 전체 특징 사용
plt.subplot(1, 2, 1)
k_values = [3, 5]
train_accs_all = [train_acc_knn3*100, train_acc_knn5*100]
test_accs_all = [test_acc_knn3*100, test_acc_knn5*100]
x = np.arange(len(k_values))
width = 0.35
plt.bar(x - width/2, train_accs_all, width, label='Train Accuracy', alpha=0.8)
plt.bar(x + width/2, test_accs_all, width, label='Test Accuracy', alpha=0.8)
plt.xlabel('k value')
plt.ylabel('Accuracy (%)')
plt.title('k-NN Classification - All Features')
plt.xticks(x, k_values)
plt.legend()
plt.ylim([0, 105])

# 4개 특징 사용
plt.subplot(1, 2, 2)
train_accs_red = [train_acc_red3*100, train_acc_red5*100]
test_accs_red = [test_acc_red3*100, test_acc_red5*100]
plt.bar(x - width/2, train_accs_red, width, label='Train Accuracy', alpha=0.8)
plt.bar(x + width/2, test_accs_red, width, label='Test Accuracy', alpha=0.8)
plt.xlabel('k value')
plt.ylabel('Accuracy (%)')
plt.title('k-NN Classification - 4 Features')
plt.xticks(x, k_values)
plt.legend()
plt.ylim([0, 105])

plt.tight_layout()
print("\nk-NN 비교 그래프를 표시합니다.")
plt.show()

print("\n" + "=" * 80)
print("모든 분석이 완료되었습니다!")
print("=" * 80)