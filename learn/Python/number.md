# Python의 진수 변환 방법

파이썬은 기본적으로 10진수를 사용하지만, 다양한 진수 간의 변환이 필요할 때가 있다. 이 문서에서는 파이썬에서 2진수, 8진수, 10진수, 16진수 간의 변환 방법을 소개한다.

## 진수의 접두사

파이썬에서 다른 진수를 표현할 때는 다음과 같은 접두사가 사용된다:

- **2진수**: `0b`
- **8진수**: `0o`
- **16진수**: `0x`

## 10진수에서 다른 진수로 변환

파이썬은 내장 함수 `bin()`, `oct()`, `hex()`를 제공하여 10진수를 손쉽게 다른 진수로 변환할 수 있다.

```python
value = 60

binary = bin(value)
octal = oct(value)
hexadecimal = hex(value)

print(binary)      # 출력: 0b111100
print(octal)       # 출력: 0o74
print(hexadecimal) # 출력: 0x3
```

변환 결과는 모두 문자열 타입으로 반환된다.

### `format()` 함수 사용

`format()` 함수를 활용하면 더욱 유연하게 진수 변환을 수행할 수 있다.

```python
value = 60

binary = format(value, '#b')
octal = format(value, '#o')
hexadecimal = format(value, '#x')

print(binary)      # 출력: 0b111100
print(octal)       # 출력: 0o74
print(hexadecimal) # 출력: 0x3c
```

두 번째 인자에서 `#`을 제거하면 접두사가 없는 결과를 얻을 수 있다.

```python
binary = format(value, 'b')   # '111100'
octal = format(value, 'o')    # '74'
hexadecimal = format(value, 'x') # '3c'

print(binary)      # 출력: 111100
print(octal)       # 출력: 74
print(hexadecimal) # 출력: 3c
```

## 다른 진수에서 10진수로 변환

`int()` 함수를 사용하여 2진수, 8진수, 16진수 문자열을 10진수로 변환할 수 있다.

```python
binary = int('0b111100', 2)  # 60
octal = int('0o74', 8)       # 60
hexadecimal = int('0x3c', 16) # 60

print(binary)      # 출력: 60
print(octal)       # 출력: 60
print(hexadecimal) # 출력: 60
```

`int()` 함수의 첫 번째 인자는 변환할 문자열이고, 두 번째 인자는 해당 문자열의 진수이다. 진수가 잘못되면 에러가 발생한다.

## 다른 진수 간 변환

10진수를 거치지 않고 직접 다른 진수 간의 변환도 가능하다. 예를 들어, 2진수를 8진수로 변환하는 방법은 다음과 같다.

```python
octal = oct(0b111100)    # '0o74'
hexadecimal = hex(0b111100) # '0x3c'
decimal_str = str(0b111100)  # '60'

print(octal)        # 출력: 0o74
print(hexadecimal)  # 출력: 0x3c
print(decimal_str)  # 출력: 60
```

## 문자열 `format()`을 사용한 진수 변환

문자열의 `format()` 메소드를 이용하면 여러 진수로 동시에 변환할 수 있다.

```python
s = "2진수: {0:#b}, 8진수: {0:#o}, 10진수: {0:#d}, 16진수: {0:#x}".format(60)
print(s)
# 출력: 2진수: 0b111100, 8진수: 0o74, 10진수: 60, 16진수: 0x3c
```

`#`을 제거하면 접두사가 없는 형태로 반환된다.

```python
s = "2진수: {0:b}, 8진수: {0:o}, 10진수: {0:d}, 16진수: {0:x}".format(60)
print(s)
# 출력: 2진수: 111100, 8진수: 74, 10진수: 60, 16진수: 3c
```

## 요약

파이썬은 다양한 내장 함수를 통해 진수 변환을 손쉽게 수행할 수 있다. `bin()`, `oct()`, `hex()` 함수와 `format()` 메소드를 적절히 활용하여 필요한 진수 형태로 데이터를 변환할 수 있다. 또한, `int()` 함수를 사용하면 다른 진수에서 10진수로의 변환도 간편하게 이루어진다.