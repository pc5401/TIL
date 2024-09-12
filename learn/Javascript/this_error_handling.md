# `this`에 관련 문제 해결

## 상황 설명

프로젝트에서 `history-wrapper` 웹 컴포넌트를 구현하면서, 외부 클릭 시 `history-wrapper`를 숨기는 기능을 추가하려 했다. 이를 위해 `document.addEventListener('click', this.handleOutsideClick)`로 이벤트 리스너를 추가하고 `this.hideHistory()`를 호출하여 컴포넌트를 숨기려고 했다.

그러나 클릭 이벤트는 발생했지만, `this.hideHistory()`가 호출되어도 `history-wrapper`는 사라지지 않았다. 또한 `this.hideHistory is not a function`이라는 오류도 발생했다.

## 개념 설명

`this`는 자바스크립트에서 **함수가 호출되는 방식**에 따라 달라지는 컨텍스트를 가리킨다. 특히, 이벤트 리스너에서 `this`는 **이벤트가 바인딩된 객체**가 아닌, **이벤트가 발생한 요소나 전역 객체**를 가리키는 경우가 있다. 이를 해결하려면, **함수를 호출할 때 `this`가 원하는 객체를 가리키도록 바인딩**해야 한다.

- **문제의 원인**: `this`가 `handleOutsideClick` 함수 내부에서 `history-wrapper` 웹 컴포넌트가 아니라, `document`나 `window` 같은 전역 객체를 가리키고 있었다.
- **해결 방법**: 이벤트 리스너를 추가할 때 `this`를 명시적으로 바인딩해야 하며, 동일한 함수 참조를 사용해 이벤트 리스너를 제거할 수 있도록 해야 한다.

### 문제 해결

1. **이벤트 리스너에 `this` 바인딩하기**: `this.handleOutsideClick.bind(this)`를 사용해 `this`를 `history-wrapper` 컴포넌트로 바인딩하고, 이를 변수에 저장했다.
2. **이벤트 리스너 제거**: 이벤트 리스너를 제거할 때, 동일한 바인딩된 함수 참조를 사용해야 하기 때문에 `boundHandleOutsideClick` 변수에 바인딩된 함수를 저장하고 이를 통해 `removeEventListener`를 호출했다.

## 코드 예시
### 개선 전 코드

개선 전 코드에서는 `this.handleOutsideClick`을 이벤트 리스너에 바로 등록했지만, 이 경우 `this`는 컴포넌트 인스턴스를 가리키지 않았다. 이로 인해 `this.hideHistory()`가 정상적으로 동작하지 않았다.

```javascript
class HistoryWrapper extends HTMLElement {
  showHistory() {
    this.classList.remove('hide');
    this.classList.add('show');
    console.log('showHistory');

    // 이벤트 리스너 추가 (문제: 바인딩되지 않음)
    document.addEventListener('click', this.handleOutsideClick, true);
  }

  hideHistory() {
    this.classList.remove('show');
    this.classList.add('hide');
    console.log('hideHistory');

    // 이벤트 리스너 제거 (문제: 동일한 참조가 사용되지 않음)
    document.removeEventListener('click', this.handleOutsideClick, true);
  }

  handleOutsideClick(event) {
    console.log('클릭 이벤트!');

    const historyWrapper = document.querySelector('history-wrapper');

    // 이벤트 경로에 history-wrapper가 포함되지 않는다면, 외부 클릭임
    if (!historyWrapper.contains(event.target)) {
      console.log('history-wrapper 외부 클릭 감지');
      this.hideHistory();
    }
  }
}

customElements.define('history-wrapper', HistoryWrapper);
```

### 문제점:

1. `this.handleOutsideClick`을 이벤트 리스너로 등록할 때, `this`가 `history-wrapper` 컴포넌트가 아니라 `document`나 `window` 같은 전역 객체를 가리키게 됨.
2. `removeEventListener`를 사용할 때, `bind`로 새로운 함수 객체를 생성하지 않기 때문에, 동일한 함수 참조를 사용하지 않아 이벤트가 제거되지 않음.

--- 
### 개선 후 코드

개선 후 코드에서는 `handleOutsideClick`을 `bind(this)`로 바인딩하여, `this`가 **컴포넌트 인스턴스**를 가리키도록 설정했고, **이 바인딩된 함수 참조를 저장**해 이벤트 리스너 추가 및 제거 시 동일한 함수 참조를 사용했다.

```javascript
class HistoryWrapper extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });

    // handleOutsideClick을 바인딩한 후 저장할 변수
    this.boundHandleOutsideClick = this.handleOutsideClick.bind(this);
  }

  showHistory() {
    this.classList.remove('hide');
    this.classList.add('show');
    console.log('showHistory');

    // 바인딩된 함수를 사용하여 이벤트 리스너 추가
    document.addEventListener('click', this.boundHandleOutsideClick, true);
  }

  hideHistory() {
    this.classList.remove('show');
    this.classList.add('hide');
    console.log('hideHistory');

    // 바인딩된 함수를 사용하여 이벤트 리스너 제거
    document.removeEventListener('click', this.boundHandleOutsideClick, true);
  }

  handleOutsideClick(event) {
    console.log('클릭 이벤트!');

    const historyWrapper = document.querySelector('history-wrapper');

    // 이벤트 경로에 history-wrapper가 포함되지 않는다면, 외부 클릭임
    if (!historyWrapper.contains(event.target)) {
      console.log('history-wrapper 외부 클릭 감지');
      this.hideHistory();
    }
  }
}

customElements.define('history-wrapper', HistoryWrapper);

```
### 개선 후 코드의 차이점:

1. **`this` 바인딩**: `handleOutsideClick`을 호출할 때 `this`가 `history-wrapper` 컴포넌트를 가리키도록 `bind(this)`로 바인딩하고, 이 바인딩된 함수의 참조를 `this.boundHandleOutsideClick`에 저장함.
2. **이벤트 리스너의 일관된 참조**: `addEventListener`와 `removeEventListener`에서 동일한 함수 참조인 `this.boundHandleOutsideClick`을 사용하여 이벤트 리스너를 정확히 추가하고 제거함.


### 요약

- `this`는 함수 호출 방식에 따라 달라진다.
- 이벤트 리스너에서 `this`를 명시적으로 바인딩하지 않으면 예상치 못한 객체를 가리킬 수 있다.
- 바인딩된 함수는 동일한 함수 참조를 통해 `removeEventListener`로 제거할 수 있어야 한다.

사실 `this` 바인딩과 관련해 개념만 알고 있었지. 에러 핸들링은 하지 않았다. 이번에 자바스크립트에서 `this`가 컨텍스트에 따라 어떻게 변화하는지와, 이를 바인딩하는 방법을 명확히 이해할 수 있었다.