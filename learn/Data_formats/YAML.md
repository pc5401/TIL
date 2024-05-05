# YAML 에 대해서



## YAML 이란

YAML은 데이터 직렬화 언어로 `JSON`의 불편함을 해소하기 위해 만들어진 `superset`이다. 그래서 YAML 에서 JSON 파일을 사용할 수 있다. 간단히 확장자만 바꿔도 된다. 파이썬처럼 들여쓰기로 문장 구조를 정의한다.



## 특징

- **인간이 읽기 쉬운 데이터 형식**: YAML은 들여쓰기와 간결한 문법을 사용하여 데이터를 명확하고 읽기 쉽게 표현한다.

- **다양한 데이터 타입 지원**: 문자열, 숫자, 배열, 객체(맵) 및 복합 데이터 타입을 지원한다.

- **중복 내용 제거 기능**: 앵커(anchors)와 별칭(aliases)을 사용하여 문서 내에서 중복되는 내용을 재사용할 수 있다.

- **휴대성과 호환성**: JSON은 YAML의 하위 집합이므로, 모든 JSON 파일은 유효한 YAML이기도 하다.

- 그리고 **주석** 이 지원된다. JSON은 주석이 안 되어서 불편했던 기억이 ㅠㅠ



## 단점, 불편함 점

- **들여쓰기 오류**: YAML은 들여쓰기를 사용하여 데이터 구조를 나타내기 때문에 실수가 많다. 

- **탭 문자 사용 불가**: YAML에서는 탭(tab) 문자를 들여쓰기 용도로 사용할 수 없다고 한다.

- **암묵적 형 변환**: YAML은 특정 문자열을 자동으로 데이터 타입(예: 부울, 숫자)으로 변환하는데, 파이썬처럼 암무적 형 변환은 버그 유발자다. 예를 들어, `yes`, `no`, `on`, `off`와 같은 문자열이 부울 값으로 해석될 수 있으며, 이는 예상치 못한 버그를 유발할 수 있음.

- **가독성 문제**: 비록 YAML이 읽기 쉬운 형식을 제공한다고 하지만, 매우 크거나 복잡한 데이터 구조에서는 여전히 읽기 어렵고 관리하기 어려움

- **표준화 문제**: YAML의 다양한 버전(1.1, 1.2 등)에서 지원하는 기능이나 구문이 다를 수 있어, 특정 도구나 라이브러리에서 예상대로 작동하지 않을 수 있다.

- **데이터 직렬화의 불편함**: 데이터를 직렬화하는 과정에서 이스케이프를 사용할 수는 있지만, 이러한 과정이 번거로울 경우 JSON을 사용하는 것이 더 효과적이다. 이 때문에 데이터 전송이나 API와 같은 분야에서는 YAML의 사용이 드뭄.

## 사용되는 곳

- **GitHub Actions**: 워크플로우 파일을 YAML 형식으로 작성하여 사용한다. (경험 O)
- **Swagger (OpenAPI)**: API 명세를 작성할 때 사용되며, YAML을 통해 API의 구조를 명확하게 정의한다. (경험 O)
- **Docker Compose**: 여러 컨테이너의 설정을 YAML 파일로 정의하여 관리한다. (경험 O)
- **Kubernetes**: 애플리케이션의 배포, 관리 및 확장을 위해 YAML 파일을 사용하여 리소스를 정의한다. (경험 X)
- **Ansible**: 자동화 스크립트를 YAML 형식으로 작성하여 서버 구성 및 관리 작업을 수행한다. (경험 X)

대체로 DevOps 쪽에서 많이 사용하는듯



## 문법

#### YAML 주석

```yaml
# 이것은 주석, YAML에서는 # 기호를 사용하여 주석을 표시한다. 하고 싶은 말은
# 주석으로 한다.
```

#### 문자열 표현

```yaml
# 문자열에 따옴표를 사용하지 않아도 되지만, 
# 특수 문자가 포함된 경우나 명확성을 위해 사용할 수 있다.
name: John Doe
nickname: 'Johnny'

# 프로퍼티 이름에 공백이 포함되어 있어도 정상적으로 파싱됨.
"full name": John Doe
```

#### 특수 문자와 이스케이프

```yaml
# 특수 문자를 포함하는 경우 따옴표를 사용 
# 이스케이프 문자를 사용하려면 작은따옴표를 사용
example: 'Line1\nLine2'
path: "C:\\Program Files\\example"

# YAML에서 특수 문자가 필요한 경우 따옴표를 사용한다.
query: "value:1"
```

#### 긴 문자열 표현

```yaml
# 여러 줄에 걸친 텍스트는 > 또는 |를 사용하여 표현할 수 있습니다.
description: >
  이 텍스트는 여러 줄에 걸쳐 있으며,
  하나의 공백 문자로 결합됩니다.

# |를 사용하면 개행 문자를 유지할 수 있습니다.
address: |
  1234 Yaml St.
  Config City, CI 12345

```

### 숫자와 boolean

```yaml
# YAML은 숫자를 자동으로 인식
integer: 123
float: 12.34

# 특수 숫자 값
max_value: .inf
not_a_number: .NaN

# 부울 값은 다양한 방법으로 표현할 수 있다.
# 기본적인 부울 값
is_active: true
has_license: false

# YAML 1.1에서는 대소문자에 관계 없이 여러 표현을 지원
is_approved: YES    # true
is_denied: no       # false

# 더 많은 예시
user_verified: TRUE  # true
email_sent: FALSE    # false

# YAML 1.2에서는 더 엄격하게 true와 false만 인식
is_complete: true
is_pending: false

# 다양한 표현 (YAML 1.1)
registration_complete: on  # true
service_enabled: off       # false

# 사용자의 혼동을 방지하기 위해 명시적인 표현을 권장한
is_visible: "true"  # 문자열 "true", 부울 값 아님


```

#### 복합 데이터 타입

```yaml
# 배열과 객체는 YAML에서 널리 사용된다. json 을 생각하면 너무 당연

# 배열 예제
fruits:
  - Apple
  - Banana
  - Cherry

deep array:
    - - - - - value # 배열을 여러번 중첩 가능

# 객체 예제
person:
  name: John Doe
  age: 30

# 중첩된 객체
details:
  bio:
    name: Jane Doe
    age: 22
  preferences:
    food: Pizza


```

#### 참조와 복제

```yaml
# YAML에서는 &로 객체를 정의하고 *로 참조하여 중복을 방지할 수 있다.
base_item: &base
  name: example item
  id: 1

duplicate_item: *base


```

#### 여러 문서의 표현

```yaml
# YAML 파일 내에서 여러 문서를 구분하여 표현할 수 있다.
# ---로 시작하고 ...로 끝내는 것이 가장 이상적인 방법
---
document: 1
...
---
document: 2
...


```


