number = int(input("숫자를 입력하시오:"))
frontNumber = number // 1000
backNumber = number % 1000

print(f"{frontNumber},{backNumber}")