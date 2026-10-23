"""02 기본필수: 평균을 어디에서 계산해야 하는지 비교"""
train_values = [10, 20]
#학습 데이터 값 2개 리스트로 저장

valid_values = [100]
#valid_values : 이름붙인 것

# 진짜 학습 기준으로 사용할 수 있는 것은 train의 평균입니다.
# TODO B02-1: train_values의 합을 개수로 나누세요.
train_mean = sum(train_values) / len(train_values)

# 아래 전체 평균은 '잘못된 기준과의 비교'를 위한 시연일 뿐입니다. 잘못된 방법임!
all_values = train_values + valid_values
#train을 이용해서 평균을 계산할 것.
all_mean = sum(all_values) / len(all_values)

print("train 평균:", round(train_mean, 2))
print("전체 평균(비교만):", round(all_mean, 2))
print("실제 전처리에는 train 평균만 사용합니다.")


# valid 데이터를 미리 사용해서 평균을 계산하면 안된다. 실제 머신러닝에서는 train_mean 만 사용할 것
