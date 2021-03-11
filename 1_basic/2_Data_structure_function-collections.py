from collections import deque
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple


## list, tuple, dict에 대한 python built-in 확장 자료 구조(모듈)
## deque: deque로 정의한 list는 stack과 queue를 지원(아래 기능들), 기존 list에 비해 효율적이고 빠른 자료구조를 제공
deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)

deque_list.appendleft(10) # appendleft 왼쪽에(가장 첫 위치) 원소 추가
print(deque_list)

deque_list.rotate(2) # rotate 원소 둘을 왼쪽으로 이동
print(deque_list)
deque_list.rotate(2)
print(deque_list)

print(deque_list)
print(deque(reversed(deque_list))) # reversed 역순

deque_list.extend([5, 6, 7]) # extend 확장
print(deque_list)

deque_list.extendleft([5,6,7]) # extendleft 왼쪽 확장(순서대로 삽입)
print(deque_list)



## OrderedDict: Dict와 달리 데이터를 입력한 순서대로 dict를 반환함
d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 500


# key 값 정렬
for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[0])).items():
    print(k,v)


# value 정렬
for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[1])).items():
    print(k,v)



## defaultdict: Dict type의 값에 기본 값을 지정, 신규값 생성시 사용하는 방법
# 기존 dict
# d = dict()
# print(d['first']) # first값이 없으므로 오류


# defaultdict
d = defaultdict(object)
d = defaultdict(lambda:0) # default 값을 0으로 설정
print(d['first']) # 위와 같이 오류로 값이 없지만 default 값이 0이므로 그 값을 출력한다.



## Counter: Sequence 내부 data element들의 갯수를 dict 형태로 반환(갯수 새기)
c = Counter()
c = Counter('gallahad')
print(c) # Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})