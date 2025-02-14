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