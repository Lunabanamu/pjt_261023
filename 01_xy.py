"""01 기본필수: CSV에서 입력과 정답을 각각 꺼내기"""
from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parent
# python 파일이 있는 경로 찾기

data = pd.read_csv(HERE / "requests.csv")
#requests.csv 파일 읽고 data 변수에 저장

# X는 예측 전에 알 수 있는 정보. ID와 정답은 입력 포함X
# TODO B01-1: 입력 열을 input_chars와 task_type 두 개 선택
X = data[["input_chars","task_type"]]

# TODO B01-2: 정답 열 failed를 선택. 0은 성공, 1은 실패입니다.
y = data["failed"]

print("입력 열:", X.columns.tolist())
# X에 있는 열 확인
print("X 모양:", X.shape)
# X의 행과 열 개수 확인
print("y 모양:", y.shape)
# y의 행과 열 개수 확인
print("처음 3개 정답:", y.head(3).tolist())
# 처음 3개의 정답 데이터 확인

#출력 형태 확인하기.
