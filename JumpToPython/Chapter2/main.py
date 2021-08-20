# # 정수형
# a = 123
# a = -178
# a = 0
#
# # 실수형
# a = 1.2
# a = -3.35
# a = 4.34E10
# a = 4.24e-10
# # 8진수
# a = 0o1777
# # 16진수
# a = 0x8ff
# b = 0xABC
#
# # 사칙연산
# a = 3
# b = 4
# print(a + b)
# print(a * b)
# print(a / b)
#
# # x의 y제곱을 나타내는 ** 연산자
# a = 3
# b = 4
# print(a ** b)
#
# # 나눗셈 후 나머지를 반환하는 % 연산자
# print(7 % 3)
# print(3 % 7)
#
# # 나눗셈 후 몫을 반환하는 // 연산자
# print(7 / 4)
# print(7 // 4)

# # 문자열
# print("hello world")
# print('python is fun')
# print("""life is too short, you need python""")
# print('''life is too short, you need python''')
#
# food = "python's favorite food is perl"
# say = '"python is very easy." he says.'
# food = 'python\'s favorite food is perl'
# say = "\"python is very easy.\"he says."

# multiline = "life is too short\n you need python"
# multiline = '''
# life is too short
# you need python
# '''
# print(multiline)
#
# head = "python"
# tail = " is fun!"
# head + tail
#
# a = "python"
# a * 2
#
# print("=" * 50)
# print("my program")
# print("=" * 50)
#
# a = 'life is to short'
# len(a)
#
# a = "life is too short, you need python"
# a[3]
# a[19:]
# #19번째부터 끝까지 출력
# a[:17]
# #0번부터 17번까지 출력
# a[:]
# #처음부터 끝까지 출력
# #0부터 시작함
#
# a[19:-7]
# #19번부터 끝이지만 -가 들어가면 -8번까지 빼서 출력

# 슬라이싱으로 날짜와 날씨를 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
year = a[:4]
day = a[4:8]

a = "pithon"
a[:1]
# p
a[2:]
# thon
a[:1] + 'y' + a[2:]
# python

# 문자열 포매팅 따라 하기
"I eat %d apples." %3
# 'I eat 3 apples.'

# %s는 문자열 ex) five 계산코드가 아니라면 문자열로 출력할 수 있게 해줌
# %c는 문자 1개
# %f 부도소수 ex) 3.4
# %o 8진수
# %x 16진수
# %% literal% (문자 % 자체) ex) %d%로 할경우 error, so %d%%

number = 3
"I eat %d apples." %number
# ' I eat 3 apples.'

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days" % (number, day)

"%10s" % "hi"
# '(10개 공백 생성)hi'
"%-10sJane." % "hi"
# 'hi (10개 공백 생성)Jane.'

"%0.4f" % 3.42134234
# '3.4213' 소수점 4번째까지 출력함 and 소수점 포인트(.)뒤에 수가 출력 결정

"%10.4f" % 3.42134234
# '   3.4313' (총 길이 10), 오른쪽 정렬

# format 함수
" I eat {0} apples" .format(3)
# ' I eat 3 apples' (문자열도 가능)

number = 3
"I eat {0} -" .format(number)

number = 10
day = "three"
" I ate {0} apples. so I was sick for {1} days" .format(number, day)

" I ate {number} apples. so I was sick for {day} days" .format(number=10, day=3)

" I ate {0} apples. so I was sick for {day} days" . format(10, day=3)
# 인덱스와 이름 혼용

"{0:<10}".format("hi")
# :<10 식은 왼쪽 정렬 후 10자리 만듦

"{0:>10}".format("hi")
# 10자리 만들고 오른쪽

"{0:^10}".format("hi")
# '    hi    ' :^ 가운데 정렬해줌

"{0:=^10}" # 공백대신 == 사용하며 가운데 정렬
"{0:!<10}" # 왼쪽 정렬 후 공백 !!로 채움

y = 3.42134234
"{0:0.4f}".format(y)
'3.4213'

"{0:10.4f}".format(y)
# 공백 생성 후 10자리 맞춤

"{{and}}".format()
'{and}'

name = 홍길동
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'

#수식 가능
age = 30
f'나는 내년이면 {age+1}살이 된다.'
# 31살로 출력 됨

d = {'name':'홍길동', 'age':30}
not f'나의 이름은 {d["name"]}입니다. 나이는 {["age"]}입니다'

f'{"hi":<10}' # left 정렬
f'{"hi":>10}' # right 정렬
f'{"hi":^10}' # center 정렬

f'{"hi":=^10}' # center 정렬 and  =로 공백 채움
f'{"hi":!<10}' # 왼쪽 정렬 and  !로 공백 채움

y = 3.42134234
f'{y:0.4f}' # 소수점 4자리까지 출력
f'{y:10.4f}' # 소수점 4자리 출력 후 10자리 맞춤

f'{{and}}'
'{and}'

문자 개수 세기
a = "hobby"
a.count('b')
# 2

a = "python is the best choice"
a.find('b')
# 14 즉 위치 나옴
a.find('k')
# -1 없는 문자를 find할 경우는 -1이 출력됨

a = "life is too short"
a.index('t')
# 8 t가 우선으로 나온 자리를 반환
# 없는 문자 넣으면 오류 발생 문구 나옴

",".join('abcd')
# 'a,b,c,d'
",".join(['a','b','c','d'])
# 'a,b,c,d'

a = "hi"
a.upper()
# 'HI' 반대는 .lower()

a = " hi "
a.lstrip()
# 'hi ' 왼쪽 공백 지움/ 오른쪽은 .rstrip()/ both .strip()

a = "life is too short"
a.replace("life","your leg")
# 'your leg is too short' 출력

# 문자열 나누기 split
a.split()
['life','is','too','short']
# 알아서 공백을 기준으로 나눔
b= "a:b:c:d"
b.split(':')
# :를 기준으로 나눠줌

# 리스트
odd = [1,3,5,7,9]
리스트명 = [요소1 , 요소2, 요소3, ....]

a = []
b = [1, 2, 3]
c = ['life', 'is', 'too', 'short']
d = [1, 2, 'life', 'is']

# 비어있는 리스트  a = list() 생성가능함

a = [1,2,3]
a[0] # 1
a[0] + a[2] # 4
a[-1] # 3

a = [1,2,3,['a','b','c']]
a[0] # 1
a[-1] # ['a','b','c']
a[3] # ['a','b','c']

a[-1][0] # 'a'
a[-1][1] # 'b'
a[-1][2] # 'c'

a = [1,2,['a','b',['life', 'is']]]
a[2][2][0] # 'life'

# 리스트의 슬라이싱

a = [1,2,3,4,5]
a[0:2] # [1,2]

a = "12345"
a[0:2] #'12'

a = [1,2,3['a','b','c'],4,5]
a[2:5] # [3,['a','b','c'],4]
a[3][:2] # ['a','b']

a = [1,2,3]
b = [4,5,6]
a + b #[1,2,3,4,5,6]

a = [1,2,3]
a * b # [1,2,3,1,2,3,1,2,3]

a = [1,2,3]
len(a) # 3

# 오류
# a = [1,2,3]
# a[2] + "hi" 3hi가 아닌 오류가 뜨게 됨
# 이때 str 함수를 사용해 정수나 실수를 문자열로 바꿔줘야 함

str(a[2]) + "hi" # 3hi

# 리스트 수정과 삭제
a = [1,2,3]
a[2] = 4
a # [1,2,4]

a = [1,2,3]
del a[1]
a # [1,3]

a = [1,2,3,4,5]
del a[2:]
a # [1,2]

# 리스트에 요소 추가 (append)

a = [1,2,3]
a.append(4)
a # [1,2,3,4]

a.append([5,6])
a # [1,2,3,4,[5,6]]

# 리스트 정렬 (sort)
a = [1,4,3,2]
a.sort()
a # [1,2,3,4]

# 마찬가지로 알파벳순도 가능함

# 뒤집기 (reverse)
a = ['a','c','b']
a.reverse()
a #['b','c','a']

# 위치반환 (index)
# 리스트 안에 () 넣은 x값이 있음 x의 위치 값을 돌려줌
a = [1,2,3]
a.index(3) #2
a.index(1) #0
a.index(0) #error

# 리스트에 요소 삽입 (insert)
# insert(a,b) a = 위치 b = 삽입 함수
a = [1,2,3]
a.insert(0,4) # [4,1,2,3]
a.insert(3,5) # [4,1,2,5,3]

# 리스트 요소 제거 (remove)
# remove(x) 첫번쨰로 나오는 x값 함수 삭제
a = [1,2,3,1,2,3]
a. remove(3)
a #[1,2,1,2,3]
a.remove(3)
a # [1,2,1,2] 한번 더 실행 했을 경우

# 리스트 요소 끄집어내기 (pop)
# pop은 리스트의 맨 마지막 요소를 돌려준 다음 그 요소 삭제
a = [1,2,3]
a.pop() # 3
a #[1,2]

a = [1,2,3]
a.pop(1) # 2
a [1,3]

# 리스트에 포함된 요소 x의 개수 세기 (count)
a = [1,2,3,4]
a.count(1) #2

# 확장 (extend)
a = [1,2,3]
a.extend([4,5])
a  # [1,2,3,4,5]
b =[6,7]
a.extend(b)
a # [1,2,3,4,5,6,7]
# a.extend([4,5]) = a +=[4,5]

# 튜플 (list와 거의 흡사)
t1 = ()
t2 = (1,) # 1개의 요소만을 가질 때 , must need
t3 = (1,2,3)
t4 = 1,2,3 # 괄호 생략해도 무방
t5 = ('a','b',('ab','cd'))

# 삭제 요솟값 변경 지원 안됨
t1 = (1,2,'a','b')
del t1[0] # error 지원되는 기능 아님

t1 = (1,2,'a','b')
t1[0] = 'c' # error 지원되는 기능 아님

# 딕셔너리
a = {1:'a'}
a[2] = 'b'
a # {1: 'a', 2: 'b'}

a['name'] = 'pey'
a # {1: 'a', 2: 'b', 'name': 'pey'}
a[3] = [1,2,3]
a # {1: 'a', 2: 'b', 'name': 'pey', 3:[1,2,3]}

del a[1]
a # {2: 'b', 'name': 'pey', 3:[1,2,3]}

dic = {'name': 'pey', 'phone': '010298374', 'birth': '1118'}
dic['name'] # 'pey'
dic['phone'] # '010298374'

# dictionary 주의점 중복되는 key값 뒤에 값만 인식함 so 다른 key값 설정

a = {[1,2]: 'hi'} # error

a = {'name': 'pey', 'phone': '010298374', 'birth': '1118'}
a.keys()
dict_keys(['name', 'phone', 'birth'])
# a의 key만을 모아 dict_keys 객체를 돌려주는 형태
# 리스트 고유의 append, insert, pop remove, sort 함수 사용 금지
# dict_keys 객체 리스트 변환
list(a.keys())
['name', 'phone', 'birth']

a.values()
dict_values(['pey,', '010298374', '1118'])
a.items()
dict_values([('name','pey,'),('phone','010298374'),('birth', '1118')])
#key와 value의 쌍을 튜플로 묶은 값 출력
a.clear()
a # {} dictionary 안에 모든 요소 delete

a.get('name') # 'pey' = a['name']
# 차이점 a.get('nokey') 는 None값  돌려줌 [None = 거짓]

a.get('foo','bar')
# 'bar'  a dictionary에는 'foo' 해당값 없어, default값인 'bar' 출력

'name' in a
# True
'email' in a
# False

# 집합 자료형
s1 = set([1,2,3])
s1 # {1,2,3}
s2 = set("Hello")
s2 # { 'e', 'h', 'l', 'o'} Unordered형으로 문자열 입력, 중복 허용 안함
# s = set() 비어있는 자료형

s1 = set([1,2,3])
l1 = list(s1)
l1 #[1,2,3]
l1[0] # 1
# list = tuple(s1) (1,2,3) t1[0] - 1

# 교집합, 합집합, 차집합 구하기
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합 s1 & s2 or s1.intersection(s2) = s2.intersection(s1)
# 합집합 s1 | s2 or s1.union(s2) = s2.union(s1)
# 차집합 s1 - s2 /= s2 - s1 or s1.difference(s2) /= s2.difference(s1)

s1.add() # 한개값 추가시
s1.update([]) # 여러값 추가시
s1.remove() # 특정값 제거

# bool 자료형
a = True
b = False

type(a)
<class 'bool'>
type(b)
<class 'bool'>

1 == 1 # True
2 > 1 # True
2 < 1 # False

# True
# "python" [1,2,3] 1
# False
# "" [] {} () 0 None

bool('python') # True
bool("") # False

a = [1,2,3]
id(a) # 4303029896 id() 객체의 주소값을 돌려주는 내장 함수

from copy import copy
a = [1,2,3]
b = copy(a)

b is a  # False

a = [1,2,3]
b = a.copy()

a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a,b] = ['python', 'life']
a = b = 'python'

# 변수 바꾸기
a = 3
b =5
a, b = b, a
a # 5
b # 3






