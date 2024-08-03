# 함수 선언과 화살표 함수

- 화살표 함수가 나오게 된 배경

화살표 함수는 ECMAScript 6(ES6, ECMAScript 2015)에서 도입된 기능이다. 이는 기존 함수 표현식의 몇 가지 단점을 보완하고, 보다 간결하고 직관적인 문법을 제공하기 위해 도입되었다. 다음은 화살표 함수가 도입된 주요 배경과 그 이유들이다.

### 1. 간결한 문법

화살표 함수는 기존의 함수 표현식보다 더 간결하게 작성할 수 있다. 이는 특히 콜백 함수를 자주 사용하는 상황에서 코드의 가독성을 높이는 데 유리하다.

```javascript
// 기존 함수 표현식
var numbers = [1, 2, 3];
var doubled = numbers.map(function(n) {
    return n * 2;
});

// 화살표 함수
var doubled = numbers.map(n => n * 2);
```

### 2. 렉시컬 `this` 바인딩

기존 함수 표현식에서 `this`는 함수가 호출될 때 동적으로 바인딩된다. 반면, 화살표 함수는 정의된 위치에서의 `this` 값을 그대로 사용한다. 이는 특히 객체 메소드나 콜백 함수 내에서 `this`가 예상과 다르게 동작하는 문제를 해결하는 데 도움이 된다.

```javascript
function Timer() {
    this.seconds = 0;
    setInterval(function() {
        this.seconds++;
        console.log(this.seconds);
    }, 1000);
}

var timer = new Timer(); // NaN 출력, this가 전역 객체를 참조

function Timer() {
    this.seconds = 0;
    setInterval(() => {
        this.seconds++;
        console.log(this.seconds);
    }, 1000);
}

var timer = new Timer(); // 1, 2, 3, ... 출력, this가 Timer 객체를 참조
```

## 최신 문법으로서의 화살표 함수

화살표 함수는 최신 문법으로서 많은 JavaScript 라이브러리와 프레임워크에서 권장되고 있다. 그 이유는 다음과 같다.

### 1. 일관성 있는 코드 스타일

화살표 함수는 간결한 문법을 제공하여 코드의 일관성을 유지하는 데 도움을 준다. 특히, 함수 선언과 콜백 함수의 사용이 많은 코드베이스에서 코드 스타일을 통일하기 쉽게 만든다.

### 2. 가독성 향상

코드가 간결해지면서 가독성이 향상된다. 이는 유지보수성에도 긍정적인 영향을 미친다. 짧고 명확한 코드 구조는 다른 개발자가 이해하고 수정하는 데 유리하다.

### 3. 예측 가능한 `this` 바인딩

화살표 함수는 `this` 바인딩 문제를 해결함으로써, 특히 객체 지향 프로그래밍과 비동기 프로그래밍에서 발생하는 `this` 관련 버그를 줄이는 데 기여한다.

## 함수 선언과 화살표 함수의 호이스팅 (Hoisting)

### 함수 선언

함수 선언은 호이스팅된다. 즉, 함수 선언은 해당 범위의 최상위로 끌어올려지므로 함수 선언 이전에도 호출할 수 있다.

```javascript
func1(); // 정상 실행

function func1() {
    console.log('This is func1');
}
```

### 화살표 함수 (const로 선언된 함수 표현식)

화살표 함수는 변수에 할당되는 함수 표현식으로, 변수는 호이스팅되지만 초기화는 되지 않으므로 함수 선언 이전에 호출하면 오류가 발생한다.

```javascript
func2(); // TypeError: func2 is not a function

const func2 = () => {
    console.log('This is func2');
};
```

### 화살표 함수의 제한점

1. `this`, `arguments`, `super`에 대한 자체 바인딩 없음
   화살표 함수는 자신의 `this` 값을 가지지 않는다. 대신, 화살표 함수가 정의된 렉시컬 환경의 `this`를 사용한다. 이 특성 때문에 메소드로 사용해서는 안 된다.

```javascript
const obj = {
    value: 10,
    method: function() {
        setTimeout(() => {
            console.log(this.value); // 화살표 함수가 상위 스코프의 this를 사용
        }, 1000);
    }
};
obj.method(); // 10

const obj2 = {
    value: 10,
    method: () => {
        console.log(this.value); // 화살표 함수의 this는 obj2가 아님
    }
};
obj2.method(); // undefined
```

2. `new.target` 키워드가 없음
   화살표 함수는 생성자 함수로 사용할 수 없으며, `new` 키워드와 함께 호출할 수 없다. `new.target` 키워드는 생성자 함수 내부에서 함수가 `new`를 사용하여 호출되었는지 여부를 확인할 수 있는 키워드이다.

```javascript
const Func = () => {};
const instance = new Func(); // TypeError: Func is not a constructor

function NormalFunc() {
    if (new.target) {
        console.log('Called with new');
    } else {
        console.log('Called without new');
    }
}
new NormalFunc(); // Called with new
NormalFunc(); // Called without new
```

3. `call`, `apply`, `bind` 메소드 사용 불가
   화살표 함수는 `this`가 정적으로 바인딩되므로, `call`, `apply`, `bind` 메소드를 사용하여 `this` 값을 변경할 수 없다.

```javascript
const obj = { value: 42 };

const func = () => {
    console.log(this.value);
};

func.call(obj); // undefined
func.apply(obj); // undefined
const boundFunc = func.bind(obj);
boundFunc(); // undefined
```

4. 생성자로 사용할 수 없음
   화살표 함수는 생성자 함수로 사용할 수 없다. `new` 키워드로 화살표 함수를 호출하면 오류가 발생한다.

```javascript
const Func = () => {};
const instance = new Func(); // TypeError: Func is not a constructor
```

5. `yield` 사용 불가
   화살표 함수는 제너레이터 함수가 될 수 없다. 따라서 `yield` 키워드를 사용할 수 없다.

```javascript
const genFunc = function* () {
    yield 1;
    yield 2;
};

const arrowGenFunc = () => {
    yield 1; // SyntaxError: Unexpected strict mode reserved word
};
```

### 함수 표현식으로의 대안

화살표 함수 외에도 함수 표현식으로 함수를 정의할 수 있다. 함수 표현식은 호이스팅되지 않으며, 호출하기 전에 정의되어 있어야 한다.

```javascript
const func = function() {
    console.log('This is a function expression');
};

func(); // 정상 실행
```

이 요약을 통해 함수 선언과 화살표 함수의 차이점과 각각의 특성을 이해할 수 있다. 이 차이점은 함수의 사용 목적에 따라 적합한 방식을 선택하는 데 도움이 된다.

## 결론

화살표 함수는 코드의 간결성, 가독성, 예측 가능한 `this` 바인딩을 제공함으로써 현대 JavaScript 개발에 있어 중요한 역할을 한다. 이러한 이유로 최신 라이브러리와 프레임워크에서도 화살표 함수를 권장하고 있으며, 개발자들 사이에서 널리 사용되고 있다.
