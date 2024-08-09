import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
from sklearn.metrics import accuracy_score


# 데이터 불러오기
df = pd.read_csv("combined_reviews2.csv")

# 필요한 열 추출 및 결측값 제거
data = df[["height", "weight", "size"]].dropna()

# height와 weight를 숫자로 변환
data["height"] = pd.to_numeric(data["height"], errors="coerce")
data["weight"] = pd.to_numeric(data["weight"], errors="coerce")

# 결측값 제거
data = data.dropna()

# 문자열 레이블을 정수로 변환
label_encoder = LabelEncoder()
data["size"] = label_encoder.fit_transform(data["size"])

# Feature와 Label 분리
X = data[["height", "weight"]]
y = data["size"]

# 학습 데이터와 테스트 데이터로 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 예측에 사용할 데이터 포인트
predict_data = pd.DataFrame(
    {"height": [160, 170, 140, 190, 150], "weight": [45, 60, 30, 100, 100]}
)

# 모델 생성
xgb_model = xgb.XGBClassifier(n_estimators=100, random_state=42)

# 모델 학습
xgb_model.fit(X_train, y_train)

# 예측
xgb_predictions = xgb_model.predict(X_test)
xgb_accuracy = accuracy_score(y_test, xgb_predictions)
print(f"XGBoost Accuracy: {xgb_accuracy}")

# 주어진 데이터 포인트 예측
xgb_predict_results = xgb_model.predict(predict_data)
xgb_predict_results_labels = label_encoder.inverse_transform(xgb_predict_results)
print(f"XGBoost Predictions: {xgb_predict_results_labels}")
