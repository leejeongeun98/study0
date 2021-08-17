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





