# js 알고리즘 노하우
> 알고리듬 풀면서 얻은 노하우

## 목차

- [정렬](#정렬) 
- [대소문자 구별](#대소문자-구별)
  
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
