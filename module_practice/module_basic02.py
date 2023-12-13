import math

# 모듈 내에 존재하는 변수,함수,클래스 등을 직접 임포트 하는 방법
from math import factorial,gcd
print(factorial(10))
print(gcd(12,18))


# import 할 모듈에 별칭을 지정하여 사용하기
import statistics
li = [13,45,657,34,23,99,66]
print(f'평균 : {statistics.mean(li)}')
print(f'분산 : {statistics.variance(li)}')
print(f'표준편차 : {statistics.stdev(li)}')
