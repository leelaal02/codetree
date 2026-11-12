"""
split()
문자열을 특정 기준으로 잘라주는 함수
공백 기준으로 문자열을 잘라, 잘려나간 단위가 하나의 원소 되어, 해당 원소를 가지고 있는 하나의 list 만들어짐
print(a.split())
arr = a.split()

list: 여러 원소를 들고 있는 묶음
arr[0], arr[1], arr[2]

input()과 split()를 한줄로 이어서 작성 가능
input().split()
"""


# a, b = input().split()
# a, b = int(a), int(b)
# print(a*b)


ab = input()
a, b = ab.split()
a, b = int(a), int(b)
print(a*b)


# 틀림 #
# a, b = int(input().split())
# split()의 결과가 리스트
# int()는 리스트 전체를 한 번에 정수로 변환할 수 없음

# a, b = int(a, b)
# int()는 두 개의 문자열을 동시에 정수로 변환할 수 없음


