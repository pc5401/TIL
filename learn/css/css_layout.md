# 레이아웃(Layout) 방식 (Display, Position, Float 등)

레이아웃은 웹 페이지의 구성 요소들을 화면에 배치하는 방법이다. 주요 속성으로는 `display`, `position`, `float`가 있으며, 더 근래에는 `flex`, `grid` 같은 기술이 많이 쓰인다.

---

## Display

HTML 요소가 **어떻게 배치되는지**를 결정하는 가장 기본적인 속성이다.

### 1) `display: block`

- **블록(block)** 요소로 배치한다.
- 줄바꿈이 자동으로 일어나고, 너비는 부모 요소에 맞춰 **전체 가로 폭**을 차지한다.
- 대표적인 예로 `<div>`, `<p>`, `<h1>~<h6>` 등이 있다.

```css
.block-example {
  display: block;
  width: 100%;
  background-color: lightgray;
}
```

### 2) `display: inline`

- **인라인(inline)** 요소로 배치한다.
- 줄바꿈이 일어나지 않고, 콘텐츠의 크기만큼 가로 폭을 차지한다.
- 너비나 높이 설정이 불가능하거나 제한적이며, 수직 방향의 여백(margin, padding)도 제한적
- 대표적으로 `<span>`, `<a>`, `<strong>` 등이 인라인 요소이다.

```css
.inline-example {
  display: inline;
  color: blue;
}
```

### 3) `display: inline-block`

- 인라인처럼 **옆으로 배치**되면서도, **블록 요소**처럼 너비와 높이를 설정할 수 있다.
- 수직 마진과 패딩도 자유롭게 설정 가능하다.

```css
.inline-block-example {
  display: inline-block;
  width: 100px;
  height: 50px;
  background-color: coral;
}
```

### 4) 기타 Display 값

- `display: none`: 요소가 **화면에서 사라짐** (공간도 차지하지 않음).
- `display: table`, `display: table-row`, `display: table-cell` 등: 테이블 레이아웃을 위한 속성.
- **현대 레이아웃**에서는 `flex`, `grid`가 주로 사용된다. (이 부분은 따로 다뤄야 할듯)