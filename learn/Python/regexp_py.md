# python 에서 정규표현식

예전에 `javascript` 의 정규표현식을 정리했는데, 정규표현식을 자주 안 쓰다보니, 까먹어서 겸사겸사 복습하려고 python으로도 정리했다.

---

## 정규표현식 기본 구조

- Python에서 정규표현식은 `re` 모듈을 사용한다.
- 문자열로 직접 사용하거나, `re.compile()`로 패턴을 미리 컴파일하여 사용한다.

```python
import re

# 문자열로 직접 사용
re.search(r'pattern', '대상 문자열')

# 컴파일 후 사용
pattern = re.compile(r'pattern')
pattern.search('대상 문자열')
```

---

## 주요 플래그

- `re.IGNORECASE` (`re.I`): 대소문자를 구분하지 않는다.
- `re.MULTILINE` (`re.M`): 여러 줄 모드에서 `^`와 `$`를 각 줄의 시작과 끝으로 인식한다.
- `re.DOTALL` (`re.S`): `.`이 줄바꿈 문자까지 매칭한다.
- `re.VERBOSE` (`re.X`): 공백과 주석을 허용하여 가독성을 높인다.
- `re.ASCII` (`re.A`): `\w`, `\W` 등이 ASCII 범위만 인식하도록 한다.
- `re.UNICODE` (`re.U`): 유니코드 문자를 인식한다. (기본값)

---

## 예제와 함께 주요 패턴

### 문자 클래스

- `[abc]`: a, b, c 중 하나
- `[^abc]`: a, b, c를 제외한 모든 문자
- `[0-9]`: 모든 숫자
- `[a-zA-Z]`: 모든 알파벳(대·소문자)

```python
import re

pattern = re.compile(r'[aeiou]')
match_list = pattern.findall("Python Regular Expression")
print(match_list)
# 모음만 추출: ['o', 'e', 'u', 'a', 'E', 'e', 'io']
```

### 특수 문자

- `.`: 줄바꿈을 제외한 임의의 문자
- `\d`: 숫자 (`[0-9]`)
- `\D`: 숫자가 아닌 것 (`[^0-9]`)
- `\w`: 단어 문자 (알파벳, 숫자, 밑줄)
- `\W`: 단어 문자가 아닌 것
- `\s`: 공백 문자 (스페이스, 탭, 줄바꿈 등)
- `\S`: 공백이 아닌 문자

```python
import re

pattern = re.compile(r'\d+')
result = pattern.findall("나이: 20, 키: 180, 몸무게: 70")
print(result)
# ['20', '180', '70']
```

### 앵커(Anchor)

- `^`: 문자열의 시작
- `$`: 문자열의 끝
- `\b`: 단어 경계(단어와 공백, 구두점 등 사이)
- `\B`: 단어 경계가 아닌 위치

```python
import re

# 문자열이 숫자로만 구성되어 있는지 확인
pattern = re.compile(r'^\d+$')
print(bool(pattern.match("12345")))   # True
print(bool(pattern.match("12345abc")))# False
```

### 수량자

- : 0회 이상
- `+`: 1회 이상
- `?`: 0회 또는 1회
- `{n}`: 정확히 n회
- `{n,}`: 최소 n회
- `{n,m}`: 최소 n회, 최대 m회

```python
import re

pattern = re.compile(r'\d{2,4}')
print(pattern.findall("연도 2023, 월 01, 일 5"))
# ['2023', '01']
```

### 그룹화와 참조

- `(...)`: 캡처 그룹
- `(?:...)`: 캡처하지 않는 그룹
- `(?P<name>...)`: 이름 있는 캡처 그룹
- `\1`, `\2`... : 이전에 캡처한 그룹을 다시 참조

```python
import re

text = "banana"
pattern = re.compile(r'(ba)(na)\1')
# (ba)(na)\1 -> (ba)(na)(ba) => "banana" 내에 "banana" 패턴을 매칭
match = pattern.search(text)
if match:
    print(match.group())  # "banana"
    print(match.groups()) # ('ba', 'na')
```

---

## 정규표현식(`re`) 주요 함수

### `re.match()`

- 문자열 시작 부분에서 패턴이 일치하는지 확인한다.
- 일치하면 `Match` 객체를 반환하고, 아니면 `None`을 반환한다.

```python
import re

pattern = re.compile(r'hello', re.I)
result = pattern.match("Hello World")
print(bool(result))  # True
```

### `re.search()`

- 문자열 전체에서 패턴이 일치하는 첫 위치를 찾는다.
- 일치하면 `Match` 객체를 반환하고, 아니면 `None`을 반환한다.

```python
import re

pattern = re.compile(r'world', re.I)
result = pattern.search("Hello World")
if result:
    print(result.start())  # 6
```

### `re.findall()`

- 패턴과 일치하는 모든 문자열을 리스트로 반환한다.

```python
import re

pattern = re.compile(r'\d+')
result = pattern.findall("전화번호: 010-1234-5678, 우편번호: 12345")
print(result)
# ['010', '1234', '5678', '12345']
```

### `re.sub()`

- 패턴과 일치하는 문자열을 다른 문자열로 치환한다.

```python
import re

pattern = re.compile(r'\d+', re.I)
result = pattern.sub("###", "비밀번호: 1234, PIN: 9999")
print(result)
# "비밀번호: ###, PIN: ###"
```

### `re.split()`

- 패턴을 기준으로 문자열을 분할하여 리스트로 반환한다.

```python
import re

pattern = re.compile(r'[\s,]+')
result = pattern.split("사과, 배  포도,수박")
print(result)
# ['사과', '배', '포도', '수박']
```

### `re.finditer()`

- 패턴과 일치하는 모든 `Match` 객체를 이터레이터로 반환한다.

```python
import re

pattern = re.compile(r'[A-Z][a-z]+')
for match in pattern.finditer("Hello World, This Is Regex"):
    print(match.group())
# Hello
# World
# This
# Is
# Regex
```

---

## 추가 예시

### IP 주소 검증

```python
import re

ip_pattern = re.compile(
    r'^(25[0-5]|2[0-4]\d|[0-1]\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]\d?\d)){3}$'
)
print(bool(ip_pattern.match("192.168.0.1")))   # True
print(bool(ip_pattern.match("256.300.123.999"))) # False
```

### HTML 태그 검증 (매우 간단한 예시)

```python
import re

# 실제 HTML 파싱은 정규표현식보다는 전용 파서 사용 권장
html_tag_pattern = re.compile(r'^<([a-zA-Z]+)>(.*?)</\1>$')
print(bool(html_tag_pattern.match("<p>Hello</p>")))    # True
print(bool(html_tag_pattern.match("<p>Hello</div>")))  # False
```

### 단어 앞뒤 토큰 검사

```python
import re

# "python" 앞뒤로 공백 또는 문장 부호가 있는지 확인
pattern = re.compile(r'(\s|^|[^a-zA-Z0-9_])python(\s|$|[^a-zA-Z0-9_])')
text = "I love python! 파이썬도 좋아."
print(bool(pattern.search(text)))  # True
```

---

## 종합 예제

### 이메일, 전화번호, URL을 동시에 검증하기

```python
import re

email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
phone_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
url_pattern = re.compile(
    r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}([\/\w .-]*)*\/?$'
)

examples = [
    "test@example.com",
    "123-456-7890",
    "https://www.example.com",
    "invalid@com",
    "1234-567-890",
    "http://example"
]

for example in examples:
    if email_pattern.match(example):
        print(f"{example} 는 올바른 이메일이다.")
    elif phone_pattern.match(example):
        print(f"{example} 는 올바른 전화번호이다.")
    elif url_pattern.match(example):
        print(f"{example} 는 올바른 URL이다.")
    else:
        print(f"{example} 는 어느 패턴에도 맞지 않는다.")
```

---

이처럼 정규표현식은 문자열 처리에 강력한 도구이다. Python의 `re` 모듈을 잘 활용하면, 복잡한 문자열 탐색과 변환 작업을 효과적으로 처리할 수 있다.