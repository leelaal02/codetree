# split() 함수는 공백을 사이에 두고 문자열을 잘라주는 함수

# 특정 문자 사이에 두고 값 출력

h, m = input().split(":")

h, m = int(h), int(m)

if 1 <=h<= 22 and 0 <=m<= 60:
    print(f"{h+1}:{m}")