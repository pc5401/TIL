# js 알고리즘 노하우
> 알고리듬 풀면서 얻은 노하우

## 목차

- [정렬](#정렬) 
- [대소문자 구별](#대소문자-구별)
- [계산된 속성 이름](#계산된-속성-이름)
  
--- 


## 정렬

- 알고리즘 풀면 정렬은 필수, 기본적으로 2가지 있다.
  - Array.prototype.sort() : 기존 배열을 변경
  - Array.prototype.toSorted() : 원본 배열을 변경하지 않고 새로운 정렬된 배열을 반환

### 정렬할 키 지정

``` js
let numbers = [10, 1, 21, 2 , 30];
numbers.sort((a, b) => a - b); // 오름차순
console.log(numbers); // [1, 2, 10, 21, 30]

numbers.sort((a, b) => b - a); // 내림차순
console.log(numbers); // [30, 21, 10, 2, 1]
```

#### 객체 배열도 정렬 가능
```js
let people = [
    { name: 'John', age: 30 },
    { name: 'Jane', age: 25 },
    { name: 'Jim', age: 35 }
];

// 나이 순으로 오름차순 정렬
people.sort((a, b) => a.age - b.age);
console.log(people);
```

### 2차원 배열도 가능
``` js
let arr = [[3, 2],[1, 3],[2, 2],[4, 1],[5, 3]];

arr.sort((a, b) => {
    if (a[1] === b[1]) {
        return b[0] - a[0]; // 인덱스 0 기준 내림차순
    } else {
        return a[1] - b[1]; // 인덱스 1 기준 오름차순
    }
});

console.log(arr); // 출력 결과: [ [ 4, 1 ], [ 3, 2 ], [ 2, 2 ], [ 5, 3 ], [ 1, 3 ] ]
```

## 대소문자 구별
``` js
if (word === word.toUpperCase()){ // 대문자라면,
    rtn += word.toLowerCase();
} else { // 소문잘라면,
    rtn += word.toUpperCase();
}
```

---

## 계산된 속성 이름 
> Computed Property Names

### 예시 상황 설명

계산된 속성 이름(Computed Property Names)은 객체의 키를 동적으로 할당해야 하는 상황에서 유용했다. 둘 개의 배열이 `key` `value` 를 가진 경우가 그러하다. 예를 들어, 데이터베이스에서 가져온 컬럼 이름을 키로 하고 해당 컬럼의 값을 값으로 설정해야 하는 경우, 계산된 속성 이름을 사용할 수 있다. 이 문법을 사용하면 객체를 생성할 때 동적으로 키를 설정할 수 있어 유연하고 강력한 코드를 작성할 수 있다.

### 예시 코드

다음은 `columns` 배열과 `values` 배열을 기반으로 동적으로 객체를 생성하는 예시 코드이다. `columns` 배열은 객체의 키가 되고, `values` 배열은 해당 키에 할당되는 값이 된다.

```javascript
class DataProcessor {
  constructor(columns, values) {
    this.columns = columns;
    this.values = values;
  }

  generateData(id) {
    const jsonData = {
      id,
      ...this.columns.reduce((acc, col, idx) => ({ ...acc, [col]: this.values[idx] }), {})
    };
    return jsonData;
  }
}

// 예시 사용법
const columns = ['name', 'age', 'city'];
const values = ['Alice', 30, 'New York'];
const processor = new DataProcessor(columns, values);
const id = 1;
const jsonData = processor.generateData(id);

console.log(jsonData);
```

#### 출력 결과

위 코드를 실행하면 `jsonData` 객체는 다음과 같이 출력된다.

```javascript
{
  id: 1,
  name: 'Alice',
  age: 30,
  city: 'New York'
}
```

#### 설명

1. `columns` 배열은 객체의 키가 된다.
2. `values` 배열은 `columns` 배열에 대응하는 값이 된다.
3. `reduce` 메서드는 `columns` 배열을 순회하며 각 키-값 쌍을 누적 객체(`acc`)에 추가한다.
4. `[col]`은 계산된 속성 이름으로, `col` 변수의 값이 객체의 키로 사용된다.

이와 같은 방식으로 계산된 속성 이름을 사용하면 객체의 키를 동적으로 설정할 수 있어, 데이터 처리 및 변환 시 매우 유용햇다.
