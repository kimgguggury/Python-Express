import random

alph = [chr(i) for i in range(65,91)]
for _ in range(10) :
    print(random.choice(alph), end= " ")