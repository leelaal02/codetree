#소수점#

# 변수 포멧
#print("%.4f" % a)

# format 함수
#print("{0:.4f}".format(a))

# f 포멧  
#print(f"{a:.4f}")

a, b= 13, 0.165
#c= a*b

#print(f"{a} * {b:.6f} = {c:.6f}")


# f-string이 먼저 처리되고, 그다음 % 포맷이 처리
# f-string의 f는 {} 부분을 처리하고, % 연산자는 %d, %f, %s 부분을 처리 
print(f"{a} * {b:.6f} = %.6f" %(a*b))




