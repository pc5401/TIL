# 자바스크립트 디버깅 기억소

## 목차

- [[object Object]가 출력되는 문제](#[object-object]가-출력되는-문제)

## [object Object]가 출력되는 문제

- 문제 : 함수의 반환 값을 console.log() 를 실행 결과 [object Object] 이 출력되었다. 
- 원인 : 객체의 내용이 아닌 객체 타입을 나타내는 [object Object]가 출력된다.
- 해결 : : 문자열로 변화한 값을 리턴하도록 구현 ex. `JSON.stringify()`

예시

```js
class User {
  constructor(name, age, city) {
    this.name = name;
    this.age = age;
    this.city = city;
  }

  getUserInfo() {
    const userInfo = {
      name: this.name,
      age: this.age,
      city: this.city
    };
    // 문자열로 구현 안 할 경우 [object Object]가 출력
    return JSON.stringify(userInfo);
  }
}

// 함수 사용 예시
const user = new User('Alice', 25, 'Wonderland');
console.log(`User Info: ${user.getUserInfo()}`);
// 출력: User Info: {"name":"Alice","age":25,"city":"Wonderland"}
```