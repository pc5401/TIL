# CSS Grid

CSS Grid는 2차원 레이아웃을 손쉽게 구성할 수 있게 해주는 강력한 CSS 모듈이다.

가로(`row`)와 세로(`column`)를 동시에 제어할 수 있어, 복잡한 페이지 구성을 명료하게 작성할 수 있다.

---

## 기본 개념

1. **Grid Container**
    - `display: grid;` 또는 `display: inline-grid;`로 설정한 부모 요소
    - 내부의 자식 요소(직계 자식)들은 **Grid Item**이 된다.
2. **Grid Item**
    - Grid 컨테이너의 **직계 자식 요소**
    - `grid-row`, `grid-column` 등 **아이템 자체**에 적용하는 속성으로 세부 배치가 가능하다.
3. **행(Row)과 열(Column)**
    - Grid는 2차원적인 행(`row`)과 열(`column`)을 동시에 다룰 수 있다.
    - “트랙(track)”이라고 부르는 행 또는 열 하나를 지정할 수 있다.

---

## Grid Container 주요 속성

### 1) `display: grid;`

자식 요소들을 Grid Item으로 만든다.

`inline-grid;`는 인라인 요소 수준의 그리드를 생성한다.

```css
.container {
  display: grid;
}
```

### 2) `grid-template-rows`, `grid-template-columns`

행(`row`), 열(`column`)의 **크기**를 정의한다.

```css
.container {
  display: grid;
  grid-template-rows: 100px 200px; /* 첫 행: 100px, 둘째 행: 200px */
  grid-template-columns: 1fr 2fr; /* 첫 열: 남은 공간의 1배, 둘째 열: 남은 공간의 2배 */
}
```

- `fr`(fraction)은 **남은 공간을 분배**하는 단위
- `px`, `%`, `auto`, `minmax()`, `fit-content()` 등 다양한 방법으로 크기를 지정할 수 있다.

### 3) `grid-template-areas`

템플릿 형태로 **영역(Area)** 이름을 지정해서 레이아웃을 구성할 수 있다.

```css
.container {
  display: grid;
  grid-template-columns: 200px 1fr;
  grid-template-rows: 100px 1fr 50px;
  grid-template-areas:
    "header  header"
    "sidebar content"
    "footer  footer";
}
```

- 각 영역은 **문자열**로 표현되며, 행마다 동일한 갯수의 셀을 적어야 한다.
- 이후 아이템에서 `grid-area` 속성으로 해당 영역 이름을 매칭한다.

### 4) `gap` (또는 `row-gap`, `column-gap`)

아이템들 사이의 **간격**을 지정한다. (이전에는 `grid-gap`으로 사용)

```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px; /* 행과 열 간격 모두 10px */
}
```

- `row-gap`, `column-gap`으로 행과 열 간격을 **개별** 설정 가능
- `gap: 10px 20px;`처럼 **행, 열** 순서로 두 값 지정 가능

### 5) `justify-items` / `align-items`

각 **셀 내부**에서 아이템을 **가로(justify)** 또는 **세로(align)** 방향으로 어떻게 정렬할지 결정한다.

- `start`, `end`, `center`, `stretch` 등을 사용할 수 있다.

```css
.container {
  display: grid;
  justify-items: center; /* 수평 중앙 정렬 */
  align-items: center;   /* 수직 중앙 정렬 */
}
```

### 6) `justify-content` / `align-content`

그리드 전체가 컨테이너 안에서 **가로(justify)** 혹은 **세로(align)** 방향으로 어떻게 배치될지 정렬한다.

```css
.container {
  display: grid;
  justify-content: space-between; /* 그리드 전체를 수평 분배 */
  align-content: center;          /* 그리드 전체를 수직 중앙 */
}
```

- 아이템 **개별** 정렬은 `justify-items`, `align-items` (또는 아이템 자체 속성 사용)
- **전체** 그리드 정렬은 `justify-content`, `align-content`

---

## 반복 구문: `repeat()`

열이나 행을 동일한 패턴으로 반복하려면 `repeat()` 함수를 사용한다.

```css
.container {
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 1fr 열을 4번 반복 */
}
```

---

## `auto-fit`, `auto-fill`, `minmax()`

반응형 레이아웃을 좀 더 쉽게 구성하기 위해 사용한다.

```css
.container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 10px;
}
```

- **`auto-fill`**: 가능한 한 많이 열을 생성(자동으로 채움)
- **`auto-fit`**: 공간이 남아도, 실제로는 아이템 수에 맞춰 열을 생성하여 **여유 공간을 늘림**
- **`minmax(min, max)`**: 최소 값과 최대 값 범위를 지정

---

## Grid Item 주요 속성

### 1) `grid-column`, `grid-row`

아이템이 **몇 번째 열**(column) 혹은 **몇 번째 행**(row)에서 시작하고 끝날지 지정한다.

```css
.item {
  grid-column: 1 / 3; /* 1번째 열에서 시작, 3번째 열 이전까지 차지 */
  grid-row: 2 / 4;    /* 2번째 행에서 시작, 4번째 행 이전까지 차지 */
}
```

- `grid-column: 1 / span 2;`처럼 **span**을 사용하면 2칸을 차지함을 의미한다.
- 시작선과 종료선을 숫자로 표현(각 열 또는 행의 선을 기준)

### 2) `grid-area`

1. `grid-template-areas`에서 지정한 영역 이름을 사용하거나,
2. `grid-row`와 `grid-column`을 간단히 한 번에 지정할 수 있다.

```css
.item1 {
  grid-area: header; /* template-areas에서 "header" 위치를 차지 */
}

.item2 {
  grid-area: 2 / 1 / 4 / 3;
  /* grid-row-start: 2, grid-column-start: 1,
     grid-row-end: 4,   grid-column-end: 3 */
}
```

---

## 예시 코드

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .container {
      display: grid;
      grid-template-columns: 200px 1fr;
      grid-template-rows: 100px 1fr 50px;
      grid-template-areas:
        "header  header"
        "sidebar content"
        "footer  footer";
      gap: 10px;
      height: 100vh;
      background-color: #f0f0f0;
    }
    .header {
      grid-area: header;
      background-color: lightblue;
    }
    .sidebar {
      grid-area: sidebar;
      background-color: lightgray;
    }
    .content {
      grid-area: content;
      background-color: #fff;
    }
    .footer {
      grid-area: footer;
      background-color: #ddd;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">Header</div>
    <div class="sidebar">Sidebar</div>
    <div class="content">Content</div>
    <div class="footer">Footer</div>
  </div>
</body>
</html>

```

위 예시에서는 다음과 같은 레이아웃을 구현할 수 있다.

- 상단(Header), 왼쪽(Sidebar), 오른쪽(Content), 하단(Footer)
- `grid-template-areas`를 통해 직관적으로 구역을 배치
- `gap`으로 영역 간 간격을 10px 부여

---

## 정리

CSS Grid는 **2차원** 레이아웃을 매우 유연하게 구성할 수 있는 강력한 방법이다.

핵심 포인트는 다음과 같다.

1. *행(row)**과 **열(column)**을 동시에 정의하여 복잡한 레이아웃을 단순화
2. **반복 구문(`repeat()`)**, **`auto-fill`, `auto-fit`, `minmax()`*로 반응형 구성이 용이
3. *`grid-template-areas`*를 통해 **시각적인 레이아웃**을 **선언형**으로 명확히 표현 가능
4. 기존의 `float` 또는 `position` 기반 레이아웃보다 **가독성**, **유지보수**성 향상