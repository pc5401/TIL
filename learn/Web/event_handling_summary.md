# 이벤트 다루기

## 쓰는 이유?

JavaScript 개발은 이벤트 중심으로 이루어진다. 사용자가 웹 페이지에서 상호작용할 때 대부분의 기능은 이벤트를 통해 작동한다. 이벤트의 동작 방식을 이해하면 더 나은 웹 프론트엔드 개발이 가능하다.

## 기본 개념

### 이벤트란?

브라우저에서 발생하는 다양한 상호작용(스크롤, 클릭 등)을 이벤트라고 한다. 특정 HTML 요소에 대해 발생하는 이벤트에 원하는 동작을 등록하여 제어할 수 있다.

### 이벤트 종류

이벤트는 마우스, 키보드, 네트워크, 터치 등 여러 종류가 있다. [MDN 웹 문서](https://developer.mozilla.org/en-US/docs/Web/Events)를 통해 다양한 이벤트를 미리 살펴보자.

### 주요 이벤트 종류

- **마우스 이벤트**: `click`, `dblclick`, `mouseover`, `mouseout`, `mousedown`, `mouseup`
- **키보드 이벤트**: `keydown`, `keyup`, `keypress`
- **폼 이벤트**: `submit`, `change`, `focus`, `blur`
- **윈도우 이벤트**: `load`, `resize`, `scroll`, `unload`
- **터치 이벤트**: `touchstart`, `touchmove`, `touchend`
- **네트워크 이벤트**: `online`, `offline`

### 이벤트 흐름

이벤트는 **캡처링**(capturing), **타겟**(target), **버블링**(bubbling) 단계를 거쳐 전파된다. 기본적으로 대부분의 이벤트는 버블링 단계에서 처리되지만, `addEventListener`의 세 번째 인자를 통해 캡처링 단계에서 이벤트를 처리할 수도 있다.

## 이벤트 등록 방법

이벤트는 `addEventListener` 함수를 사용하여 등록한다. 이 함수는 이벤트가 발생했을 때 실행할 함수를 지정한다.

```jsx
const element = document.getElementById("myElement");
element.addEventListener("click", function(event) {
  // 수행할 작업
}, false);
```

### 이벤트 객체

이벤트 핸들러는 이벤트가 발생할 때 실행되며, 이때 이벤트 객체를 통해 추가적인 정보를 제공받을 수 있다. 예를 들어, `event.target`은 이벤트가 발생한 요소를 가리킨다.

```jsx
element.addEventListener("click", function(event) {
  console.log(event.target); // 이벤트가 발생한 요소
}, false);
```

### 이벤트 위임

여러 개의 자식 요소에 동일한 이벤트를 적용해야 할 때, 부모 요소에 이벤트를 등록하고 이벤트 버블링을 활용하여 처리하는 방법이다. 이를 통해 메모리 사용을 줄이고 코드의 효율성을 높일 수 있다.

```jsx
const parent = document.getElementById("parentElement");
parent.addEventListener("click", function(event) {
  if (event.target && event.target.matches("button.className")) {
    // 버튼 클릭 시 수행할 작업
  }
});
```

### preventDefault 메서드

`preventDefault` 메서드를 사용하면 브라우저에서 기본으로 제공하는 이벤트 동작을 막을 수 있다. 예를 들어, 링크의 기본 동작을 막거나 폼 제출을 막을 수 있다.

```jsx
const link = document.getElementById("myLink");
link.addEventListener("click", function(event) {
  event.preventDefault();
  // 커스텀 동작 수행
}, false);

```

### stopPropagation 메서드

`stopPropagation` 메서드를 사용하면 이벤트가 더 이상 상위 요소로 전파되지 않도록 할 수 있다. 이를 통해 특정 요소에서만 이벤트를 처리할 수 있다.

```jsx
element.addEventListener("click", function(event) {
  event.stopPropagation();
  // 이벤트 전파를 중지하고 작업 수행
}, false);
```

### 이벤트 리스너 옵션

`addEventListener`의 세 번째 인자는 이벤트 리스너의 옵션을 설정할 수 있다.

- `capture`: 이벤트 캡처링 단계를 사용할지 여부
- `once`: 이벤트가 한 번만 실행되고 자동으로 제거될지 여부
- `passive`: 이벤트 리스너가 `preventDefault`를 호출하지 않을 것임을 브라우저에 알림으로써 성능 최적화

```jsx
element.addEventListener("scroll", function(event) {
  // 스크롤 시 수행할 작업
}, { passive: true });
```

## 이벤트 제거 방법

등록된 이벤트 핸들러는 `removeEventListener`를 사용하여 제거할 수 있다. 이를 통해 메모리 누수를 방지하고 필요하지 않은 이벤트 핸들러를 정리할 수 있다.

```jsx
function handleClick(event) {
  // 작업 수행
}

element.addEventListener("click", handleClick, false);

// 나중에 이벤트 제거
element.removeEventListener("click", handleClick, false);
```

## onclick을 통한 이벤트 핸들러 등록

`onclick` 속성으로 이벤트 핸들러를 등록할 수 있지만, 여러 이벤트를 등록할 수 없고 코드의 재사용성이 떨어지므로 `addEventListener` 사용이 더 효과적이다.

```html
<!-- 권장되지 않음 -->
<button onclick="alert('Clicked!')">Click me</button>
```

```jsx
// 권장됨
const button = document.querySelector("button");
button.addEventListener("click", function() {
  alert("Clicked!");
});
```

## 추가 학습 자료

더 많은 이벤트 개념을 학습하려면 [MDN 이벤트 핸들러 속성](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#Event_handler_properties)과 [이벤트 참고 문서](https://developer.mozilla.org/en-US/docs/Web/Events)를 참고하자.

## 요약

이벤트의 종류는 매우 다양하며, 이를 잘 이해하고 적절히 사용하는 것이 중요하다. 이벤트 객체를 잘 활용하면 보다 세밀한 제어가 가능하다. 다른 사람의 코드를 검토하며 다양한 구현 방식을 학습하는 것도 중요하다.
