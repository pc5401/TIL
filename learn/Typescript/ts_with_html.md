# TypeScript를 이용한 HTML 조작

## 개요

JavaScript의 주요 목적 중 하나는 HTML을 조작하고 변경하는 것이다. TypeScript를 사용해도 HTML 조작이 가능하지만, JavaScript와 약간의 차이점이 존재한다. 이는 주로 타입 안전성 때문에 발생하며, 이를 해결하기 위해서는 약간의 추가 작업이 필요하다.

## `strictNullChecks` 옵션 활성화

TypeScript 프로젝트에서 `strictNullChecks` 옵션을 활성화하면, 변수에 `null`이 할당될 수 있는지 여부를 명확히 체크할 수 있다. 이는 HTML 요소를 선택할 때 `null`이 반환될 가능성을 고려하여 보다 안전한 코드를 작성하는 데 도움을 준다.

```json
{
  "compilerOptions": {
    "target": "ES5",
    "module": "commonjs",
    "strictNullChecks": true}
}
```

또는 `strict` 옵션을 `true`로 설정하면 `strictNullChecks`가 자동으로 활성화된다.

```json
{
  "compilerOptions": {
    "target": "ES5",
    "module": "commonjs",
    "strict": true}
}
```

## HTML 파일 준비

다음과 같은 간단한 HTML 파일을 준비한다.

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TypeScript Example</title>
</head>
<body>
  <h4 id="title">Hello</h4>
  <a id="link" href="https://example.com">Link</a>
  <button id="button">Button</button>

  <script src="compiled.js"></script>
</body>
</html>
```

## HTML 요소 찾고 변경하기

TypeScript를 사용하여 HTML 요소를 찾고 내용을 변경하는 예제를 살펴본다.

### 예제 1: 제목 변경

다음 코드는 `id`가 `title`인 `<h4>` 요소의 내용을 변경한다.

```tsx
let titleElement = document.querySelector('#title');
titleElement.innerHTML = 'Welcome'; // 에러 발생
```

위 코드에서는 `titleElement`가 `HTMLElement` 또는 `null`일 수 있기 때문에, TypeScript는 `null` 가능성을 고려하여 에러를 발생시킨다. 이를 해결하기 위한 방법은 다음과 같다.

### 해결책 1: Type Narrowing 사용

`if` 문을 사용하여 `titleElement`가 `null`이 아님을 확인한 후에 내용을 변경한다.

```tsx
let titleElement = document.querySelector('#title');
if (titleElement !== null) {
  titleElement.innerHTML = 'Welcome';
}
```

### 해결책 2: `instanceof` 연산자 사용

`instanceof` 연산자를 사용하여 `titleElement`가 특정 HTML 요소 타입임을 확인한다.

```tsx
let titleElement = document.querySelector('#title');
if (titleElement instanceof HTMLElement) {
  titleElement.innerHTML = 'Welcome';
}
```

### 해결책 3: Type Assertion 사용

Type Assertion을 사용하여 `titleElement`가 `HTMLElement`임을 명시적으로 지정한다.

```tsx
let titleElement = document.querySelector('#title') as HTMLElement;
titleElement.innerHTML = 'Welcome';
```

### 해결책 4: Optional Chaining 연산자 사용

Optional Chaining 연산자를 사용하여 `titleElement`가 존재할 경우에만 내용을 변경한다.

```tsx
let titleElement = document.querySelector('#title');
titleElement?.innerHTML = 'Welcome';
```

### 해결책 5: `strictNullChecks` 비활성화

`tsconfig.json`에서 `strictNullChecks` 옵션을 `false`로 설정하면, `null` 체크를 생략할 수 있다. 하지만 이는 권장되지 않는다.

```json
{
  "compilerOptions": {
    "target": "ES5",
    "module": "commonjs",
    "strictNullChecks": false}
}
```

### 링크 요소의 `href` 속성 변경

다음 예제는 `<a>` 태그의 `href` 속성을 변경하는 방법을 보여준다.

```tsx
let linkElement = document.querySelector('#link');
if (linkElement instanceof HTMLAnchorElement) {
  linkElement.href = 'https://kakao.com';
}
```

`HTMLAnchorElement` 타입을 사용하여 `href` 속성을 안전하게 변경할 수 있다.

## HTML 요소 타입

TypeScript에서 사용할 수 있는 HTML 요소 타입은 다양하다. 예를 들어:

- `<a>` 태그: `HTMLAnchorElement`
- `<img>` 태그: `HTMLImageElement`
- `<h4>` 태그: `HTMLHeadingElement`
- 기타 등등

HTML 요소를 선택할 때, 정확한 타입으로 Narrowing 해야 HTML 속성을 안전하게 수정할 수 있다.

### 원리 설명

TypeScript에서 HTML 요소는 계층적인 타입 구조를 가진다. 예를 들어:

- `Element`
    - `HTMLElement`
        - `HTMLAnchorElement`
        - `HTMLImageElement`
        - `HTMLHeadingElement`
        - 등등

`document.querySelector` 메서드는 기본적으로 `Element | null` 타입을 반환한다. 따라서, 특정 HTML 요소의 속성을 사용하려면 해당 요소의 구체적인 타입으로 Narrowing 해야 한다.

### 결론

TypeScript를 사용하여 HTML 요소를 조작할 때는 `strictNullChecks` 옵션을 활성화하고, 타입 Narrowing 또는 Type Assertion을 사용하여 안전하게 요소를 다루는 것이 중요하다. 이를 통해 코드의 안정성을 높이고, 예상치 못한 런타임 오류를 방지할 수 있다.

### 추가 참고 사항

- TypeScript 공식 문서의 DOM 타입을 참고하여 다양한 HTML 요소 타입을 확인할 수 있다.
- HTML 요소를 선택하고 조작할 때는 항상 타입 안전성을 고려하여 코드를 작성해야 한다.