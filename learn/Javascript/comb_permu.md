# js 의 조합, 순열, 중복조합 등등
> JavaScript에서 상기한 모듈을 직접 구현한다. ㅠㅠ

### 목차

- [js 의 조합, 순열, 중복조합 등등](#js-의-조합-순열-중복조합-등등)
    - [목차](#목차)
  - [조합](#조합)
    - [조합 결과](#조합-결과)
  - [순열](#순열)
    - [순열 결과](#순열-결과)
  - [중복조합](#중복조합)
    - [중복조합 결과](#중복조합-결과)
  - [중복순열](#중복순열)
    - [중복순열 결과](#중복순열-결과)
  - [카르테시안 곱](#카르테시안-곱)
    - [중복순열 결과](#중복순열-결과-1)
---

## 조합 
> Combinations
- 주어진 배열의 요소들을 순서를 고려하여 모든 가능한 경우로 배열한 것.

``` js
function combinations(arr, k) {
  const results = [];

  function combine(start, path) {
    if (path.length === k) {
      results.push([...path]); // 얇은 복사
      return;
    }
    for (let i = start; i < arr.length; i++) {
      path.push(arr[i]);
      combine(i + 1, path);
      path.pop();
    }
  }

  combine(0, []);
  return results;
}

console.log(combinations([1, 2, 3], 2));
```

### 조합 결과
``` sh
[[1, 2],[1, 3],[2, 3]]
```

## 순열
> Permutations
- 주어진 배열의 요소들을 순서를 고려하지 않고 선택한 모든 가능한 경우
``` js
function permutations(arr) {
  const results = [];

  function permute(path, used) {
    if (path.length === arr.length) {
      results.push([...path]);
      return;
    }
    for (let i = 0; i < arr.length; i++) {
      if (used[i]) continue;
      used[i] = true;
      path.push(arr[i]);
      permute(path, used);
      path.pop();
      used[i] = false;
    }
  }

  permute([], Array(arr.length).fill(false));
  return results;
}

console.log(permutations([1, 2, 3]));
```
### 순열 결과
``` sh
[
  [1, 2, 3],
  [1, 3, 2],
  [2, 1, 3],
  [2, 3, 1],
  [3, 1, 2],
  [3, 2, 1]
]
```
## 중복조합
> Combinations with Repetition
- 주어진 배열의 요소들을 순서를 고려하지 않고 중복을 허용하여 선택한 모든 가능한 경우.

``` js
function combinationsWithRepetition(arr, k) {
  const results = [];

  function combine(start, path) {
    if (path.length === k) {
      results.push([...path]);
      return;
    }
    for (let i = start; i < arr.length; i++) {
      path.push(arr[i]);
      combine(i, path);  // Note the use of 'i' instead of 'i + 1'
      path.pop();
    }
  }

  combine(0, []);
  return results;
}

console.log(combinationsWithRepetition([1, 2, 3], 2));
```
### 중복조합 결과
``` sh
[
  [1, 1],
  [1, 2],
  [1, 3],
  [2, 2],
  [2, 3],
  [3, 3]
]
```


## 중복순열
> Permutations with Repetition
- 주어진 배열의 요소들을 순서를 고려하여 중복을 허용한 모든 가능한 경우.

``` js
function combinationsWithRepetition(arr, k) {
  const results = [];

  function combine(start, path) {
    if (path.length === k) {
      results.push([...path]);
      return;
    }
    for (let i = start; i < arr.length; i++) {
      path.push(arr[i]);
      combine(i, path);  // Note the use of 'i' instead of 'i + 1'
      path.pop();
    }
  }

  combine(0, []);
  return results;
}

console.log(combinationsWithRepetition([1, 2, 3], 2));
```
### 중복순열 결과
``` sh
[
  [1, 1],
  [1, 2],
  [1, 3],
  [2, 1],
  [2, 2],
  [2, 3],
  [3, 1],
  [3, 2],
  [3, 3]
]
```


## 카르테시안 곱
> Cartesian Product
- 여러 배열의 요소들을 조합하여 가능한 모든 쌍을 나열한 것.

``` js
function permutationsWithRepetition(arr, k) {
  const results = [];

  function permute(path) {
    if (path.length === k) {
      results.push([...path]);
      return;
    }
    for (let i = 0; i < arr.length; i++) {
      path.push(arr[i]);
      permute(path);
      path.pop();
    }
  }

  permute([]);
  return results;
}

console.log(permutationsWithRepetition([1, 2, 3], 2));
```

### 중복순열 결과
``` sh
[  [1, 'a', 'X'],
  [1, 'a', 'Y'],
  [1, 'b', 'X'],
  [1, 'b', 'Y'],
  [2, 'a', 'X'],
  [2, 'a', 'Y'],
  [2, 'b', 'X'],
  [2, 'b', 'Y']
]
```