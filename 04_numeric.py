"""04 기본필수: 결측이 없는 숫자를 train 기준으로 표준화하기"""
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 제공: 정상 숫자만 사용합니다. 결측 대체는 선택 단계에서 배웁니다.

train = pd.DataFrame({"input_chars": [100, 200, 300]})
#학습 데이터
valid = pd.DataFrame({"input_chars": [400, 500]})
# 검증 데이터
scaler = StandardScaler()
#숫자 데이터 표준화
scaler.fit(train)
#train 데이터 기준 학습

# transform은 이미 배운 평균과 크기를 사용합니다. 다시 fit하지 않습니다.
# TODO B04-1: scaler의 transform으로 valid를 변환하세요.
valid_ready = scaler.transform(valid)

print("train에서 배운 평균:", scaler.mean_.tolist())
# train에서 학습한 평균 확인
print("valid 변환 결과:")
print(valid_ready.round(3))
# 변환된 valid 데이터 출력


# StandardScaler를 이용한 숫자데이터 표준화 및 train 전처리기준 학습. valid로 변환
