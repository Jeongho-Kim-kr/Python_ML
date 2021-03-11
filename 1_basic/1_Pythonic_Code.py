## pythonic code: 간결한 코드

## split, join
## list comprehension
## enumerate, zip
## lambda, map, reduce (권장 안함 pandas 참고, list comprehension 권장)
## *(asterisk)



## split: string type의 값을 나눠서 list 형으로 변환
# 빈칸을 기준으로 문자열 나누기
items = 'zero one two three'.split()

print(items)


# "," 을 기준으로 문자열 나누기
example = 'python,jquery,javascript'

print(example.split(","))


# 리스트의 각 값을 a, b, c, 변수로 unpacking
example = 'python,jquery,javascript'

a, b, c = example.split(",")​


# "."을 기준으로 문자열 나누고 unpacking
example = 'cs50.gachon.edu'

subdomain, domain, tld = example.split(".")



## join: string List를 합쳐 하나의 string으로 반환
# 연결 시 빈칸 1칸으로 연결
colors = ['red','blue','green','yellow']
result = ''.join(colors)
print(result)


# 연결 시 ', '으로 연결
result = ', '.join(colors)
print(result)


# 연결 시 '-'으로 연결
result = '-'.join(colors)
print(result)



## List comprehensions: 기존 List사용하여 간단히 다른 List를 만드는 기법, for + append보다 속도가 빠름
# for loop + append 사용 경우
result = []

for i in range(10):
    result.append(i)

print(result)


# list Comprehension 사용 경우
result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i % 2 == 0]
print(result)


# list Comprehension(Nested for loop 2중 루프)
word_1 = "Hello"
word_2 = "World"

result = [i+j for i in word_1 for j in word_2]
print(result)


# list Comprehension(Nested for loop 2중 루프)
case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]

result = [i+j for i in case_1 for j in case_2]
print(result)


# list Comprehension(Nested for loop 2중 루프) if 문 추가(i==j 아닌 경우만 실행)
result = [i+j for i in case_1 for j in case_2 if not(i==j)]
result.sort()
print(result)


# list Comprehension
words = 'The quick brown fox jumps over the lazy dog'.split() # 문장을 빈칸 기준으로 나눠서 list로 변환
print(words)

stuff = [[w.upper(), w.lower(), len(w)] for w in words] # [대문자, 소문자, 길이]

for i in stuff:
    print(i)



## Enumerate: list의 element를 추출할 때 번호를 붙여서 추출
# list에 있는 index와 값을 unpacking
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# list에 있는 index와 값을 unpacking하여 list로 저장
mylist = ['a','b','c','d']
list(enumerate(mylist)) # [(0,'a'),(1,'b'),(2,'c'),(3,'d'),]


# 문장을 list로 반들고 list의 index와 값을 unpacking하여 dict로 출력
# 단어의 위치 출력
# {0: 'Gachori', 1: 'University', 2: 'is', 3: 'an', 4: 'academic', 5: 'institute', 6: 'located', 7: 'in', 8: 'South', 9: 'Korea.'}
print({i:j for i,j in enumerate('Gachori University is an academic institute located in South Korea.'.split())})



## zip: 두 개 list의 같은 위치 값을 병렬적으로 추출함
# for loop + zip
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for a, b in zip(alist, blist):
    print(a, b)


# list comprehension + zip
# (1 10 100) (2 20 200) (3 30 300)
a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)


# [111,222,333]
print([sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))])


# enumerate + zip
# 0 a1 b1
# 1 a2 b2
# 2 a3 b3
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, (a, b) in enumerate(zip(alist, blist)):
    print(i, a, b)



## lambda: 함수 이름 없이 함수처럼 쓸 수 있는 익명 함수(권장 안함)
# general function
def f(x,y):
    return x + y
print(f(1,4))


# lambda function
f = lambda x,y: x+y
print(f(1,4))



## map: sequence 자료형 '각 element'에 동일한 fuction을 적용함(권장 안함)
# list(map(function_name, list_data))
ex = [1,2,3,4,5]
f = lambda x: x**2
print(list(map(f, ex))) # [1, 4, 9, 16, 25]


# 두개의 인자를 받는 경우
ex = [1,2,3,4,5]
f = lambda x,y: x+y
print(list(map(f, ex, ex)))


# map필터(만족하지 않는 경우 else를 넣어줘야한다)
ex = [1,2,3,4,5]
print(list(map(lambda x: x**2 if x%2 == 0 else x, ex)))


# list comprehension(권장)
ex = [1,2,3,4,5]
print([value ** 2 for value in ex])



## reduce: map과 달리 list에 똑같은 함수를 순차적으로 적용해서 '통합'(권장 안함)
from functools import reduce
# 순차합
print(reduce(lambda x, y: x+y, [1,2,3,4,5])) # 15


# 펙토리얼 !
from functools import reduce
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print(factorial(5))



## *(asterisk): 흔히 알고 있는 *를 뜻하며 단순 곱셈, 제곱연산, 가변인자 활용 등에 사용
# *args 앞 변수를 뺀 나머지 변수를 가져옴
def asterisk_test(a, *args):
    print(a, args)
    print(type(args))

asterisk_test(1,2,3,4,5,6) # 1 (2,3,4,5,6) 뒤는 튜플


# **kargs 앞 변수를 뺀 나머지 키워드 인자를 받아옴
def asterisk_test(a, **kargs):
    print(a, kargs)
    print(type(kargs))

asterisk_test(1, b=2, c=3, d=4, e=5, f=6) # 1 {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6} 뒤는 dict타입


# unpacking a container 변수 앞에 *추가
a, b, c = ([1,2], [3,4], [5,6])
print(a,b,c) # [1, 2] [3, 4] [5, 6]

data = ([1,2], [3,4], [5,6])
print(*data) # [1, 2] [3, 4] [5, 6]


# 키워드 unpacking a container 변수 앞에 **추가
def asterisk_test(a,b,c,d):
    print(a,b,c,d)
data = {'b':1, 'c':2, 'd':3}
asterisk_test(10, **data) # 10 1 2 3


# unpacking a container 응용
# (1, 3, 5)
# (2, 4, 6)
for data in zip(*([1,2], [3,4], [5,6])):
    print(data)