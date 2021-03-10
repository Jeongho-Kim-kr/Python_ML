## pythonic code: 간결한 코드

# split, join
# list comprehension
# enumerate, zip


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