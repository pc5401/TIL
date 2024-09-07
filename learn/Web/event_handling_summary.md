
# 이벤트 다루기

## 쓰는 이유?

JavaScript 개발은 이벤트 중심으로 이루어진다. 사용자가 웹 페이지에서 상호작용할 때 대부분의 기능은 이벤트를 통해 작동한다. 이벤트의 동작 방식을 이해하면 더 나은 웹 프론트엔드 개발이 가능하다.

## 기본 개념

### 이벤트란?

브라우저에서 발생하는 다양한 상호작용(스크롤, 클릭 등)을 이벤트라고 한다. 특정 HTML 요소에 대해 발생하는 이벤트에 원하는 동작을 등록하여 제어할 수 있다.

### 이벤트 종류

이벤트는 마우스, 키보드, 네트워크 등 여러 종류가 있다. [MDN 웹 문서](https://developer.mozilla.org/en-US/docs/Web/Events)를 통해 다양한 이벤트를 미리 살펴보자.

## 이벤트 등록 방법

이벤트는 `addEventListener` 함수를 사용하여 등록한다. 이 함수는 이벤트가 발생했을 때 실행할 함수를 지정한다.

```javascript
const element = document.getElementById("myElement");
element.addEventListener("click", function() {
  // 수행할 작업
}, false);
```

### 이벤트 객체

이벤트 핸들러는 이벤트가 발생할 때 실행되며, 이때 이벤트 객체를 통해 추가적인 정보를 제공받을 수 있다. 예를 들어, `event.target`은 이벤트가 발생한 요소를 가리킨다.

```javascript
element.addEventListener("click", function(event) {
  console.log(event.target); // 이벤트가 발생한 요소
}, false);
```

### preventDefault 메서드

`preventDefault` 메서드를 사용하면 브라우저에서 기본으로 제공하는 이벤트 동작을 막을 수 있다. 예를 들어, 링크의 기본 동작을 막을 수 있다.

## onclick을 통한 이벤트 핸들러 등록

`onclick` 속성으로 이벤트 핸들러를 등록할 수 있지만, 여러 이벤트를 등록할 수 없으므로 `addEventListener` 사용이 더 효과적이다.

## 추가 학습 자료

더 많은 이벤트 개념을 학습하려면 [MDN 이벤트 핸들러 속성](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#Event_handler_properties)과 [이벤트 참고 문서](https://developer.mozilla.org/en-US/docs/Web/Events)를 참고하자.

## 요약

이벤트의 종류는 매우 다양하며, 이를 잘 이해하고 적절히 사용하는 것이 중요하다. 이벤트 객체를 잘 활용하면 보다 세밀한 제어가 가능하다. 다른 사람의 코드를 검토하며 다양한 구현 방식을 학습하는 것도 중요하다.