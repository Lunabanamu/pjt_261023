"""05 기본필수: qa와 summary를 서로 다른 0/1 열로 표현하기"""
from sklearn.preprocessing import OneHotEncoder

train = [["qa"], ["summary"], ["qa"]]
#학습 데이터 생성
valid = [["summary"], ["qa"]]
#검증 데이터 생성

# sparse_output=False는 결과를 바로 볼 수 있는 숫자 표로 받는 설정입니다.
encoder = OneHotEncoder(sparse_output=False)
encoder.fit(train)
# train 데이터를 기준으로 학습

# TODO B05-1: encoder.transform(valid).tolist()로 실제 변환 결과를 구하세요.
valid_ready = encoder.transform(valid).tolist()

print("열 순서:", encoder.categories_[0].tolist())
# 인코딩된 열의 순서 확인
print("valid 변환:", valid_ready)
# 변환된 valid 데이터 확인

# 문자형 데이터를 숫자로 변환하는 방법

