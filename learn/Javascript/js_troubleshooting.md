# 자바스크립트 디버깅 기억소

## 목차

- [에러 코드 예시](#에러-코드-예시) 

- [[object Object]가 출력되는 문제](#object-object가-출력되는-문제)

--- 

## 에러코드 예시

터미널에서 에러코드가 나왔을 때, node의 에러코드의 형태를 정리해 보았다.

### 에러 메시지 예시

```shell
node:internal/readline/emitKeypressEvents:74
            throw err;
            ^

TypeError: arr is not iterable
    at checkArr (/path/to/your/project/directory/app.js:13:18)      
    at checkTable (/path/to/your/project/directory/app.js:32:17)    
    at solve (/path/to/your/project/directory/app.js:50:21)
    at Interface.<anonymous> (/path/to/your/project/directory/app.js:70:21)
    at Interface.emit (node:events:526:35)
    at Interface.close (node:internal/readline/interface:527:10)
    at [_ttyWrite] [as _ttyWrite] (node:internal/readline/interface:1128:18)
    at ReadStream.onkeypress (node:internal/readline/interface:264:20)
    at ReadStream.emit (node:events:514:28)
    at emitKeys (node:internal/readline/utils:371:14)

Node.js v20.10.0

```



### 에러 메시지의 각 부분 설명

1. **에러 발생 파일 및 라인 정보**:
   
   ```shell
   node:internal/readline/emitKeypressEvents:74
               throw err;
               ^
   ```
   
   - Node.js 내부 모듈의 파일과 해당 파일의 라인 번호를 나타냄
   - `node:internal/readline/emitKeypressEvents:74`는 Node.js의 내부 `readline` 모듈의 `emitKeypressEvents` 파일의 74번째 라인에서 에러가 발생했음을 의미함
   - 내부 모듈의 구성은 왁벽히 이해하기 어렵지만 좀 더 깊게 해결해야할 때는 당당히 모듈속으로 들어가자.

2. **에러 유형 및 메시지**:
   
   ```shell
   TypeError: arr is not iterable
   ```
   
   - 에러의 종류가 `TypeError`이며, 구체적인 메시지는 `arr is not iterable`임
   - 이는 `arr` 변수가 반복 가능한(iterable) 객체가 아님을 의미함

3. **스택 트레이스**:
   
   ```shell
   at checkArr (/path/to/your/project/directory/app.js:13:18)      
   at checkTable (/path/to/your/project/directory/app.js:32:17)    
   at solve (/path/to/your/project/directory/app.js:50:21)
   at Interface.<anonymous> (/path/to/your/project/directory/app.js:70:21)
   at Interface.emit (node:events:526:35)
   at Interface.close (node:internal/readline/interface:527:10)
   at [_ttyWrite] [as _ttyWrite] (node:internal/readline/interface:1128:18)
   at ReadStream.onkeypress (node:internal/readline/interface:264:20)
   at ReadStream.emit (node:events:514:28)
   at emitKeys (node:internal/readline/utils:371:14)
   
   ```
   
   
   
   - 스택 트레이스는 에러가 발생한 위치와 그 위치로 이어진 함수 호출의 역추적을 보여준다.
   - 가장 상위에 있는 항목이 에러가 발생한 직접적인 위치이며, 그 아래로 함수 호출의 역순으로 나열됨
     - 가장 위에서 부터 확인하자.
   - 각 항목은 다음과 같이 구성됨:
     - `at checkArr (/path/to/your/project/directory/app.js:13:18)`:
       - `checkArr` 함수 내부에서 `/path/to/your/project/directory/app.js` **파일의 13번째 라인, 18번째 열**에서 에러가 발생
     - `at checkTable (/path/to/your/project/directory/app.js:32:17)`:
       - `checkTable` 함수가 호출된 위치를 나타냄
     - `at solve (/path/to/your/project/directory/app.js:50:21)`:
       - `solve` 함수가 호출된 위치를 나타냄
     - 그 외의 항목들은 Node.js의 내부 모듈에서 발생한 호출 스택을 나타냄
   - 의미 모를 스택 트레이스에 겁을 먹지 말자. 

4. **Node.js 버전**:
   
   ```shell
   Node.js v20.10.0`
   ```
   
   - 에러가 발생한 환경의 Node.js 버전
   - 이는 디버깅 과정에서 중요한 정보가 될 수 있다. 에러는 버전의 차이에서 일어나기도...

### 에러 디버깅 절차

1. **에러 메시지 확인**:
   
   - 에러 유형(`TypeError`)과 구체적인 메시지(`arr is not iterable`)를 확인하여 어떤 종류의 문제가 발생했는지 파악하자.

2. **스택 트레이스 분석**:
   
   - 스택 트레이스를 위에서 아래로 따라가면서 에러가 발생한 정확한 위치를 찾음
   - 예를 들어, `checkArr` 함수의 13번째 라인에서 에러가 발생했음을 알 수 있음

3. **코드 수정**:
   
   - `checkArr` 함수의 13번째 라인으로 가서 `arr` 변수가 왜 반복 가능한 객체가 아닌지 확인하고 수정한다.
   - 해당 변수가 올바른 값을 갖도록 초기화하거나, 필요한 경우 예외 처리를 추가한다.







--- 

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