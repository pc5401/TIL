# 선택자(Selector)

선택자는 HTML 요소에 스타일을 적용하기 위해 요소를 특정할 때 사용한다. 원하는 요소를 정확히 지칭함으로써 CSS 충돌을 줄이고, 유지보수를 쉽게 만든다.

## 기본 선택자

- **태그 선택자(Tag Selector)**  
  태그 이름으로 요소를 선택한다.  
  ```css
  p {
    color: blue;
  }
  ```

- **클래스 선택자(Class Selector)**
  
  클래스명을 가진 요소를 선택한다. 여러 요소에 공통 스타일을 적용할 때 유용하다.
  
  ```css
  .highlight {
    background-color: yellow;
  
  ```
  
- **아이디 선택자(ID Selector)**
  
  문서 내에서 유일한 식별자(`#id`)를 가진 요소를 선택한다. 문서에 중복되지 않도록 주의해야 한다.
  
  ```css
  #header {
    font-weight: bold;
  }
  ```

### 참고 선택자 우선순위(Specificity)

- CSS에서 여러 규칙이 동일한 요소에 적용될 경우, 우선순위에 따라 어떤 스타일이 적용될지 결정된다.  
- 다음과 같음

| 우선순위 | 분류 / 선택자 | 예시                                       | 점수 개념                | 설명                                                                                                      |
|:------:|:-----------:|:-----------------------------------------:|:------------------------:|:--------------------------------------------------------------------------------------------------------|
| 1      | `!important` | `color: red !important;`                | -                        | **일반적인 우선순위 규칙을 무시**하고 가장 먼저 적용된다. 단, 가독성과 유지보수를 위해 신중하게 사용해야 한다. |
| 2      | 인라인 스타일 (Inline Style) | `<div style="color:red;">`        | 1000 (가정치)            | HTML 요소에 직접 작성된 스타일이다. 선택자 계산과 별개로 최상위 우선순위를 가진다.                          |
| 3      | 아이디 선택자 (#id) | `#header { font-weight: bold; }`    | 100                      | 문서에서 유일해야 하며, 매우 강력한 우선순위를 가진다. 중복해서 사용하지 않도록 주의한다.                    |
| 4      | 클래스 선택자 (.class), 속성 선택자([attr]), 의사 클래스 (:hover 등) | `.highlight { background-color: yellow; }`<br>`a[href] { color: green; }`<br>`:hover { color: blue; }` | 10                       | 클래스, 속성, 상태 등을 기반으로 요소를 선택한다. 여러 요소에 공통 스타일을 적용할 때 사용한다.                    |
| 5      | 태그(요소) 선택자 (Tag Selector) | `p { color: blue; }`<br>`div { margin: 0; }` | 1                        | 태그 이름으로 요소를 선택한다. 가장 낮은 우선순위를 가진다.                                                   |

- **점수 개념**: 일반적으로 ID는 100점, 클래스∙속성∙의사 클래스는 10점, 태그 선택자는 1점으로 계산한다. 인라인 스타일은 1000점 정도의 최상위로 취급하기도 한다.
- `!important`는 **점수 계산과 무관**하게 최우선으로 적용된다.

  - 선택자 우선순위를 이해하고 적용하면 스타일 충돌이나 예측 불가능한 결과를 방지할 수 있다.  
  - 불필요하게 `!important`를 사용하는 것을 지양하고, 구조적이고 명확한 선택자를 통해 관리하는 것이 좋다.

# 고급 선택자(Advanced Selectors)

## 결합자(Combinator)

### 1) 자손 선택자(Descendant Combinator)

`A B` 형태로, **선택자 A의 모든 후손 요소 중 선택자 B에 해당하는 것**을 선택하는 방식이다. 띄어쓰기만으로 표현하며 가장 많이 사용하는 결합자이다.

```css
/* .container 내부에 있는 모든 p 태그를 선택 */
.container p {
  color: green;
}
```

- `.container` 내부 어디에 있든 `p` 요소이면 스타일이 적용된다.
- 깊은 중첩 구조에서도 하위에 있는 모든 `p`에 스타일을 적용한다.

### 2) 자식 선택자(Child Combinator)

`A > B` 형태로, **선택자 A의 바로 아래(직계) 자식 요소 중 선택자 B**에 해당하는 것을 선택한다.

```css
/* .container의 직계 자식으로 존재하는 p 태그만 선택 */
.container > p {
  font-size: 16px;
}
```

- `.container` 안에 들어 있더라도, 자식의 자식(손자) 요소는 선택되지 않는다.
- 구조가 복잡할 때, 의도한 범위에만 스타일을 적용하고 싶을 때 유용하다.

### 3) 인접 형제 선택자(Adjacent Sibling Combinator)

`A + B` 형태로, **선택자 A 바로 뒤에 인접해 있는 형제 요소 중 선택자 B**만 선택한다.

```css
/* h2 바로 뒤에 오는 p 태그에만 스타일 적용 */
h2 + p {
  margin-top: 0;
}
```

- `h2`와 같은 레벨에 있고, `h2` 다음에 바로 오는 `p` 요소만 선택된다.
- 인접한 형제 관계인지가 매우 중요하다.

### 4) 일반 형제 선택자(General Sibling Combinator)

`A ~ B` 형태로, **선택자 A와 같은 부모를 공유하며, A 뒤에 위치하는 모든 형제 요소 중 선택자 B**를 선택한다.

```css
/* .notice 뒤에 오는 모든 .message 클래스를 가진 형제 요소 */
.notice ~ .message {
  color: red;
}
```

- 중간에 다른 요소가 여러 개 끼어 있어도, 같은 부모 내에서 `A` 뒤에 등장하면 모두 선택된다.
- 여러 요소에 한 번에 스타일을 적용할 때 유용하다.

## 속성 선택자(Attribute Selector)

HTML 요소가 가진 **속성(attribute)과 그 값(value)**을 기반으로 선택한다. 폼 요소나 링크 등 특정 속성을 가진 요소만 골라 적용하기에 편리하다.

### 1) 기본 속성 존재 여부: `[attr]`

해당 속성이 존재하기만 하면 선택한다.

```css
/* disabled 속성이 있는 모든 요소 */
[disabled] {
  opacity: 0.6;
}
```

### 2) 정확한 값 일치: `[attr="value"]`

속성 값이 정확히 `value`와 일치하는 요소를 선택한다.

```css
/* type="submit"인 input 요소만 선택 */
input[type="submit"] {
  background-color: blue;
  color: white;
}
```

### 3) 공백으로 구분된 값 중 하나 포함: `[attr~=value]`

속성 값이 **공백을 구분자로 하는 여러 단어** 중에 `value`를 포함하고 있으면 선택한다.

```css
/* class 속성에 "btn"이라는 단어가 포함되어 있으면 선택 */
[class~=btn] {
  padding: 10px 20px;
  border-radius: 4px;
}
```

### 4) 값의 시작 부분 일치: `[attr^=value]`

속성 값이 `value`로 **시작**하면 선택한다.

```css
/* href가 "https://"로 시작하는 링크에만 스타일 적용 (SSL 페이지) */
a[href^="https://"] {
  color: green;
}
```

### 5) 값의 끝부분 일치: `[attr$=value]`

속성 값이 `value`로 **끝**나면 선택한다.

```css
/* 파일이 .png로 끝나는 이미지에만 스타일 적용 */
img[src$=".png"] {
  border: 1px solid #ccc;
}
```

### 6) 값의 일부 포함: `[attr*=value]`

속성 값 어딘가에 `value`가 **포함**되어 있으면 선택한다.

```css
/* data-info 속성에 'warning'이라는 단어가 포함된 요소 */
[data-info*="warning"] {
  background-color: yellow;
}
```

### 7) 대쉬(-)로 구분된 패턴: `[attr|=value]`

속성 값이 `value`와 정확히 일치하거나 `value-`로 시작하면 선택한다.

```css
/* lang 속성이 'en' 또는 'en-US', 'en-GB' 등으로 시작하면 선택 */
[lang|="en"] {
  font-family: "Arial", sans-serif;
}
```
## 의사 클래스(Pseudo-class)와 의사 요소(Pseudo-element)

CSS에서 동적인 상태나 특정 부분을 가상으로 선택해서 스타일을 적용할 수 있다.

### 1) 의사 클래스(Pseudo-class)

`:hover`, `:focus`, `:active`, `:visited`, `:nth-child(n)`, `:nth-of-type(n)` 등이 대표적이다.

```css
/* 마우스 오버 상태 */
button:hover {
  background-color: #333;
  color: #fff;
}

/* 부모 안에서 3번째 자식 */
.parent :nth-child(3) {
  font-weight: bold;
}
```

- 의사 클래스는 **사용자의 상호작용**(hover, focus)이나 문서 구조(nth-child 등)에 따라 동적으로 적용된다.

### 2) 의사 요소(Pseudo-element)

`::before`, `::after`, `::first-line`, `::selection` 등이 대표적이다. 요소의 특정 부분(텍스트 첫 줄, 선택 영역 등)이나, 존재하지 않던 내용(::before/::after)을 가상으로 만들어낼 때 사용한다.

```css
/* 요소의 시작 부분에 내용 추가 */
.list-item::before {
  content: "▶ ";
  color: orange;
}

/* 첫 줄만 스타일 다르게 적용 */
p::first-line {
  font-size: 1.2em;
  font-weight: bold;
}
```

- `::before`와 `::after`는 `content` 프로퍼티를 통해 가상 요소를 생성한다.
- 시각적인 장식을 추가하거나, 특정 텍스트를 강조하는 데 유용하다.
---
