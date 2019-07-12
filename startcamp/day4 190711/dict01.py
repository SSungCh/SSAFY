"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

# 1. 기본 풀이
result = 0
count = 0
for score_value in score.values():
    # result = result + score_value
    # count = count + 1
    result += score_value
    count += 1
# print(result/len(score))
print(result/count)

# 2. sum 함수 활용하기
result2 = sum(score.values())
count = len(score)
print(result2/count)