### 변수 포맷
# %s 문자열
# %c 문자
# %d 정수
# %f 실수
#맨뒤에 %변수

### format 함수

### f 문자열 포맷 이용
#문자열 앞에 f 붙이고 변수 이름을 중괄호{}로 감싸기

a, b, c = 7, 23, 30

# print("%d + %d = %d" % (a, b, c))
# print("{a} + {b} = {c}".format(a=a, b=b, c=c))
print(f"{a} + {b} = {c}")
