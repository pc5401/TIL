
# TIL: JavaScript 구조 분해 할당

JavaScript는  **구조 분해 할당**이 있다. 구조 분해 할당은 배열이나 객체의 값을 개별적인 변수에 할당하는 문법이다. 이를 통해 코드의 가독성을 높이고 작성해야 할 코드의 양을 줄일 수 있다.
## 배열 구조 분해 할당

예를 들어, `colors`라는 배열이 있고, 이 배열에는 `"red"`, `"green"`, `"blue"`라는 세 개의 문자열이 들어 있다.

```javascript
const colors = ["red", "green", "blue"];
```

이 배열에서 첫 번째와 두 번째 요소를 각각 `red`, `green`라는 변수에 할당하려면 다음과 같이 작성할 수 있다.

```javascript
const [red, green] = colors;
console.log(red); // "red"
console.log(green); // "green"
```

만약 배열의 특정 요소를 제외하고 할당하고 싶다면, 아래와 같이 쉼표로 생략할 수 있다.

```javascript
const [red, , blue] = colors;
console.log(red);  // "red"
console.log(blue); // "blue"
```

존재하지 않는 요소를 할당하면 `undefined`가 반환되며, 기본값을 설정할 수도 있다.

```javascript
const [red, green, yellow = "yellow"] = colors;
console.log(yellow); // "yellow"
```

나머지 요소들을 배열로 모으고 싶다면 스프레드 연산자를 사용할 수 있다.

```javascript
const [red, ...restColors] = colors;
console.log(restColors); // ["green", "blue"]
```

## 객체 구조 분해 할당

객체 구조 분해 할당은 배열과 비슷하지만, 중괄호 `{}`를 사용하며, 변수 이름은 객체의 키와 동일해야 한다.

```javascript
const person = { name: "Alice", age: 30, city: "Seoul" };
const { name, age } = person;
console.log(name); // "Alice"
console.log(age);  // 30
```

만약 객체의 키와 다른 이름으로 변수를 사용하고 싶다면, 아래와 같이 작성할 수 있다.

```javascript
const { name: personName } = person;
console.log(personName); // "Alice"
```

또한, 존재하지 않는 키에 대해 기본값을 설정할 수 있다.

```javascript
const { country = "Korea" } = person;
console.log(country); // "Korea"
```

스프레드 연산자를 사용하여 나머지 키들을 새로운 객체로 모을 수도 있다.

```javascript
const { name, ...otherInfo } = person;
console.log(otherInfo); // { age: 30, city: "Seoul" }
```

## 유용한 팁

1. **변수 값 교환하기**:
   배열 구조 분해 할당을 사용하면 간단하게 변수 값을 교환할 수 있다.

   ```javascript
   let x = 10, y = 20;
   [x, y] = [y, x];
   console.log(x); // 20
   console.log(y); // 10
   ```

2. **함수에서 반환된 배열 구조 분해**:
   함수가 배열을 반환할 때, 그 즉시 구조 분해 할당을 할 수 있다.

   ```javascript
   function getCoordinates() {
       return [37.5665, 126.9780];
   }
   const [latitude, longitude] = getCoordinates();
   console.log(latitude);  // 37.5665
   console.log(longitude); // 126.9780
   ```

3. **반복문에서 구조 분해 할당 사용**:
   배열의 각 요소가 객체일 때, 반복문에서 구조 분해 할당을 활용할 수 있다.

   ```javascript
   const users = [{ username: "john_doe", age: 25 }, { username: "jane_doe", age: 28 }];
   for (const { username, age } of users) {
       console.log(username); // "john_doe", "jane_doe"
   }
   ```

4. **함수 매개변수로 객체 구조 분해 할당**:
   함수의 매개변수로 전달된 객체를 구조 분해 할당할 수 있다.

   ```javascript
   const user = { username: "john_doe", age: 25 };
   function displayUserInfo({ username, age }) {
       console.log(`${username} is ${age} years old.`);
   }
   displayUserInfo(user); // "john_doe is 25 years old."
   ```

## 구조 분해 할당 심화

### 중첩된 구조 분해 할당:
- 중첩된 배열이나 객체도 당연히 구조 분해 할당을 사용할 수 있다.
- 중첩해서 분해하면 된다.(simple~)
``` js
const nestedArray = [1, [2, 3], 4];
const [first, [second, third], fourth] = nestedArray;
console.log(second); // 2

const nestedObject = { a: { b: 1, c: 2 }, d: 3 };
const { a: { b, c }, d } = nestedObject;
console.log(c); // 2
```

- 기본값 설정도 중첩 구조 분해할 수 있다.

```js
const options = {
    size: { width: 100, height: 200 },
    color: "blue"
};

const { size: { width = 50, height = 100 }, color = "red" } = options;
console.log(width);  // 100
console.log(height); // 200
console.log(color);  // "blue"
```

### Rest와 Spread 연산자의 차이점

- Rest: 배열이나 객체의 나머지 요소를 모을 때 사용
   ``` js
   const [first, ...rest] = [1, 2, 3, 4];
   console.log(rest); // [2, 3, 4]
   ```
- Spread: 배열이나 객체의 요소를 펼칠 때 사용
   ``` js
   const arr1 = [1, 2];
   const arr2 = [...arr1, 3, 4];
   console.log(arr2); // [1, 2, 3, 4]
   ```

### 구조 분해 할당과 불변성
객체나 배열의 불변성을 유지하면서 구조 분해 할당을 사용할 수 있다.

``` js
const originalArray = [1, 2, 3];
const newArray = [...originalArray];
newArray[0] = 100;
console.log(originalArray); // [1, 2, 3]
console.log(newArray);      // [100, 2, 3]
```

### 구조 분해 할당과 함수 인자

``` js
function createUser({ username, email, password }) {
    // username, email, password를 사용하여 사용자 생성 로직
}

const userData = {
    username: "john_doe",
    email: "john@example.com",
    password: "secret"
};

createUser(userData);

```
