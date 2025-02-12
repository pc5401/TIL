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