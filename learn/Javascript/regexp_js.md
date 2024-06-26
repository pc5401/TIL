# js 에서 정규표현

> 정규표현식(Regular Expressions, RegExp)은 문자열의 패턴을 찾거나 일치시키는 데 사용



사실 정규표현식은 js 말고 많이 사용된다. 최근 js 를 사용하는 일이 늘어나면서 js로 정규표현식을 쓰는법에 대해서 정리할 필요성을 느꼈다. ~~사실 맨날 까먹는다~~

---

### 목차

- [정규표현식 기본 구조](#정규표현식-기본-구조)
- [주요 플래그](#주요-플래그)
- [예제와 함께 주요 패턴](#예제와-함께-주요-패턴)
- [자주 사용되는 메서드](#자주-사용되는-메서드)
- [예제](#예제)

---

## 정규표현식 기본 구조

JavaScript에서 정규표현식(Regular Expressions, RegExp)은 문자열의 패턴을 찾거나 일치시키는 데 사용됩니다. 정규표현식은 슬래시(`/`)로 둘러싸인 패턴으로 작성하거나 `RegExp` 객체를 생성하여 사용할 수 있다.

```javascript
// 리터럴 표기법
const regex = /pattern/flags;

// 객체 생성 표기법
const regexObj = new RegExp('pattern', 'flags');

```

## 주요 플래그

- `g` (global): 모든 일치 항목을 찾는다.
- `i` (ignore case): 대소문자를 구분하지 않는다.
- `m` (multiline): 여러 줄 모드에서 앵커(^, $)를 줄의 시작과 끝에서 일치시킨다.
- `s` (dotAll): 점(.)이 줄 바꿈 문자를 포함하여 모든 문자를 일치시킨다.
- `u` (unicode): 유니코드 코드 포인트로 패턴을 처리한다.
- `y` (sticky): 시작 위치를 고정하여 검색한다.

## 예제와 함께 주요 패턴

### 문자 클래스

- `[abc]`: a, b, c 중 하나
- `[^abc]`: a, b, c가 아닌 것
- `[0-9]`: 모든 숫자
- `[a-zA-Z]`: 모든 알파벳 대소문자

### 특수 문자

- `.`: 모든 단일 문자
- `\d`: 숫자 (`[0-9]`와 동일)
- `\D`: 숫자가 아닌 것 (`[^0-9]`와 동일)
- `\w`: 단어 문자 (알파벳 대소문자, 숫자, 밑줄)
- `\W`: 단어 문자가 아닌 것
- `\s`: 공백 문자 (스페이스, 탭 등)
- `\S`: 공백 문자가 아닌 것

### 앵커

- `^`: 문자열의 시작
- `$`: 문자열의 끝
- `\b`: 단어 경계
- `\B`: 단어 경계가 아닌 것

### 수량자

- `*`: 0회 이상
- `+`: 1회 이상
- `?`: 0회 또는 1회
- `{n}`: 정확히 n회
- `{n,}`: 최소 n회
- `{n,m}`: 최소 n회, 최대 m회

### 그룹화와 참조

- `(...)`: 캡처 그룹
- `(?:...)`: 캡처하지 않는 그룹
- `\1, \2, ...`: 캡처 그룹 참조

## 자주 사용되는 메서드

### `test`

패턴이 문자열에 일치하는지 테스트하여 결과를 `true` 또는 `false`로 반환한다.

```javascript
const regex = /hello/i;
console.log(regex.test('Hello world')); // true
```

### `match`

패턴과 일치하는 문자열을 배열로 반환한다.

```javascript
const str = 'Hello world';
const regex = /hello/i;
console.log(str.match(regex)); // ["Hello"]
```

### `replace`

일치하는 문자열을 다른 문자열로 대체한다.

```javascript
const str = 'Hello world';
const regex = /world/i;
console.log(str.replace(regex, 'JavaScript')); // "Hello JavaScript"
```

### `split`

패턴을 기준으로 문자열을 나누어 배열로 반환한다.

```javascript
const str = 'Hello world';
const regex = /\s/;
console.log(str.split(regex)); // ["Hello", "world"]
```

### `search`

패턴이 일치하는 문자열의 인덱스를 반환한다. 일치하지 않으면 `-1`을 반환한다.

```javascript
const str = 'Hello world';
const regex = /world/i;
console.log(str.search(regex)); // 6
```



## 예제

### 이메일 검증

```javascript
const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
console.log(emailPattern.test('test@example.com')); // true
```

### 전화번호 검증

```javascript
const phonePattern = /^\d{3}-\d{3}-\d{4}$/;
console.log(phonePattern.test('123-456-7890')); // true
```

### URL 검증

```javascript
const urlPattern = /^(https?:\/\/)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}([\/\w .-]*)*\/?$/;
console.log(urlPattern.test('https://www.example.com')); // true
```



---



정규표현식을 연습하기 좋은 자료도 많으니까. 검색해서 틈틈이 복습하자.
