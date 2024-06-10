# JSON 에 대해서

# JSON에 대해서

## JSON이란

JSON(JavaScript Object Notation)은 데이터 교환 형식으로 널리 사용되는 텍스트 기반의 경량 데이터 직렬화 표준이다. JSON은 주로 서버와 클라이언트 간의 데이터 전송에 사용되며, 인간이 읽기 쉽고 기계가 파싱하고 생성하기 쉬운 구조를 가지고 있다.

## 특징

- **경량 데이터 교환 형식**: JSON은 간결한 문법을 사용하여 데이터 구조를 표현하므로, 데이터 전송 및 저장 시 효율적이다.
- **다양한 데이터 타입 지원**: 문자열, 숫자, 배열, 객체(맵), boolean 및 null 값을 지원한다.
- **언어 독립적**: 대부분의 프로그래밍 언어에서 JSON을 쉽게 파싱하고 생성할 수 있는 라이브러리를 제공한다.
- **가독성**: 사람이 읽고 쓰기 쉽도록 설계되었다.
- **데이터 직렬화 및 역직렬화**: JSON은 데이터 직렬화 및 역직렬화가 용이하여 다양한 환경에서 쉽게 사용된다.

## 단점, 불편함 점

- **주석 지원 없음**: JSON은 주석을 지원하지 않아 설명이나 메모를 추가할 수 없다.
- **데이터 타입 제한**: JSON은 기본 데이터 타입만을 지원하며, 날짜나 이진 데이터 등의 복잡한 타입을 직접적으로 표현하기 어렵다.
- **문자열로만 키 표현**: 객체의 키는 반드시 문자열이어야 하며, 다른 타입을 키로 사용할 수 없다.
- **데이터 크기**: XML에 비해 크기가 작지만, 바이너리 형식에 비해 크기가 클 수 있다.
- **유효성 검사 및 스키마**: JSON 자체는 스키마를 포함하지 않으며, 추가적인 도구나 언어가 필요하다.

## 사용되는 곳

- **웹 API**: 서버와 클라이언트 간의 데이터 교환을 위해 JSON을 사용한다. (경험 O)
- **구성 파일**: 일부 애플리케이션 및 라이브러리는 설정 파일로 JSON을 사용한다. (경험 O)
- **데이터베이스**: NoSQL 데이터베이스(예: MongoDB)에서 JSON 형식의 문서를 저장하고 관리한다. (경험 O)
- **데이터 직렬화**: 프로그래밍 언어 간의 데이터 교환 및 저장을 위해 JSON을 사용한다. (경험 O)
- **로그 및 모니터링**: 시스템 로그 및 모니터링 데이터의 형식으로 JSON을 사용한다. (경험 X)

## 문법

#### JSON 객체

```json
{
  "name": "John Doe",
  "age": 30,
  "isStudent": false
}
```
#### JSON 배열
```json
{
  "integer": 123,
  "float": 12.34,
  "is_active": true,
  "has_license": false
}
```

#### 숫자와 boolean
```json
{
  "integer": 123,
  "float": 12.34,
  "is_active": true,
  "has_license": false
}
```

#### 문자열
```json
{
  "greeting": "Hello, World!",
  "escape": "Line1\\nLine2"
}
```

#### 중첩된 객체와 배열
```json
{
  "person": {
    "name": "John Doe",
    "age": 30,
    "address": {
      "street": "1234 JSON St.",
      "city": "Object City"
    }
  },
  "fruits": [
    {
      "name": "Apple",
      "color": "Red"
    },
    {
      "name": "Banana",
      "color": "Yellow"
    }
  ]
}
```

## JSON Schema
JSON의 유효성을 검사하고 구조를 정의하기 위해 JSON Schema를 사용할 수 있다. JSON Schema는 JSON 문서의 구조와 데이터 타입을 명시적으로 정의하여 데이터의 유효성을 검증하는 데 사용된다.

#### JSON Schema 예제

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Person",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "age": {
      "type": "integer",
      "minimum": 0
    },
    "isStudent": {
      "type": "boolean"
    }
  },
  "required": ["name", "age"]
}
```
이와 같이 JSON은 다양한 환경에서 데이터를 직렬화하고 전송하는 데 매우 유용한 형식이다. JSON Schema를 사용하면 데이터 구조와 유효성을 보다 명확하게 정의할 수 있다.