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

---

## Position

요소를 **정확한 위치**에 배치하기 위한 속성이다. 기본값은 `static`이며, `relative`, `absolute`, `fixed`, `sticky` 등이 자주 쓰인다.

### 1) `position: static`

- **기본 위치** 설정. 부모나 형제 요소의 배치 흐름에 따라 자동으로 배치된다.
- `top`, `left` 등의 좌표 속성이 **무시**된다.

```css
.static-example {
  position: static;
}
```

### 2) `position: relative`

- **자신의 원래 위치를 기준**으로 이동한다.
- `top`, `right`, `bottom`, `left`로 **상대**적인 이동이 가능하며, 이동 후에도 **원래 자리 공간은 유지**한다.

```css
.relative-example {
  position: relative;
  top: 10px;
  left: 20px;
}
```

### 3) `position: absolute`

- **부모 요소**(조상 중 가장 가까운 `position`이 지정된 요소)를 기준으로 이동한다.
- 레이아웃 흐름에서 **제외**되어, 원래 있던 공간은 사라진다.
- `z-index`를 사용하면 다른 요소와의 **쌓임 순서**(stack order)를 조절할 수 있다.

```css
.parent {
  position: relative; /* 기준 요소가 될 수 있음 */
}
.absolute-example {
  position: absolute;
  top: 0;
  right: 0;
  width: 100px;
  height: 50px;
  background-color: gold;
}
```

### 4) `position: fixed`

- *브라우저 화면(Window)**를 기준으로 고정된다.
- 스크롤해도 위치가 변하지 않는다.
- 주로 상단 바, 하단 바, 공지 배너 등에 활용된다.

```css
.fixed-example {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #333;
  color: #fff;
}
```

### 5) `position: sticky`

- 스크롤 위치에 따라 **상대(relative)**→**고정(fixed)** 상태로 전환된다.
- 스크롤이 특정 지점에 이르면 화면에 고정되고, 그 지점을 벗어나면 다시 상대 위치로 돌아간다.

```css
.sticky-example {
  position: sticky;
  top: 0;
  background-color: lightblue;
}
```

---

## Float

옛날 레이아웃 방식 중 하나로, 요소를 **왼쪽이나 오른쪽**으로 띄워서 배치한다.

본문 텍스트를 이미지 주위로 흐르게 하는 등 특정 목적에 사용한다.

### 1) 기본 사용법

```css
.float-left {
  float: left;
  width: 50%;
  background-color: #fafafa;
}

.float-right {
  float: right;
  width: 50%;
  background-color: #eee;
}
```

- `.float-left` 요소는 왼쪽에 붙고, `.float-right` 요소는 오른쪽에 붙는다.
- 주변 요소들은 부유한(floated) 요소의 **옆을 둘러싸** 배치된다.

### 2) Clear

`float`된 요소 다음에 오는 요소가 **겹치지 않게** 아래로 내려오도록 한다.

```css
.clear-both {
  clear: both;
}
```

- `clear: left`, `clear: right`로 왼쪽 또는 오른쪽만 피할 수도 있다.
- 보통 `clearfix` 기법을 써서 부모 요소가 부유된 자식들을 감싸도록 한다.

```css
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}
```

부모 요소에 `.clearfix` 클래스를 적용하면, 내부에 떠 있는(`float`) 자식 요소를 정리해준다.