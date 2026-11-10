a=3
b=4
b=a

print(a,b)
print(f"{a*b}")

# Python의 print()는 쉼표(,)로 구분된 값 사이에 기본적으로 공백 한 칸
# 이유는 print()의 기본 설정이 sep=" " 이기 때문
# print(a, b)             # 10 20
# print(a, b, sep=" ")    # 10 20
# print(a, b, sep="")     # 1020
# print(a, b, sep="\n")   # 줄바꿈