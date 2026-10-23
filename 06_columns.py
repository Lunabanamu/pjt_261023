"""06 기본필수: 숫자 1열과 문자 1열을 함께 변환하기"""
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

train = pd.DataFrame({"input_chars": [100, 200, 300],
                      "task_type": ["qa", "summary", "qa"]})
# 학습 데이터 input_chars는 숫자, task_type은 문자 데이터임

valid = pd.DataFrame({"input_chars": [400, 500],
                      "task_type": ["summary", "qa"]})
# 검증 데이터

# 제공: 숫자에는 표준화, 문자에는 원-핫 변환을 지정합니다.
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), ["input_chars"]),
    ("cat", OneHotEncoder(sparse_output=False), ["task_type"]),
])
# 데이터 종류에 따라 숫자는 StandardScaler, 문자는 OneHotEncoder 적용

preprocessor.fit(train)
# train 데이터 기준 전처리 방법 학습

# TODO B06-1: preprocessor의 transform으로 valid를 변환하세요.
valid_ready = preprocessor.transform(valid)

print("변환 전:", valid.shape)
print("변환 후:", valid_ready.shape)
print(valid_ready.round(3))
# 변환된 데이터를 소수점 셋째 자리까지 반올림 출력

# 숫자형과 문자형 각각 전처리하기
